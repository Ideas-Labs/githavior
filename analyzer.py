"""
Analyzes user data using IBM Watson Personality Insights
and Natural Language Understanding APIs.
"""
from io import BytesIO
import json
import os
import requests

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os

from wordcloud import WordCloud, STOPWORDS

from flask import Flask, request, jsonify, render_template
from flask_cors import CORS, cross_origin

from ibm_watson import PersonalityInsightsV3, NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import Features, EmotionOptions

try:
    from githavior.credentials import NLU_KEY, PERSONALITY_INSIGHTS_KEY
except ModuleNotFoundError:  # For Heroku
    NLU_KEY = os.environ['NLU_KEY']
    PERSONALITY_INSIGHTS_KEY = os.environ['PERSONALITY_INSIGHTS_KEY']

from githavior.fetch_repos import get_commits, get_pr_issues_body, get_avatar

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


personality_service = PersonalityInsightsV3(
    version='2017-10-13',
    url='https://gateway-lon.watsonplatform.net/personality-insights/api',
    username='apikey',
    password=PERSONALITY_INSIGHTS_KEY)

naturalLanguageUnderstanding = NaturalLanguageUnderstandingV1(
    version='2018-11-16',
    url='https://gateway-lon.watsonplatform.net/natural-language-understanding/api',
    username='apikey',
    password=NLU_KEY)


stopwords = set(STOPWORDS)
stopwords.add("said")


wc = WordCloud(background_color="black", mask=mask,
               stopwords=stopwords, contour_width=10, contour_color='steelblue')

"""
@app.route('/', methods=['GET'])
def base():
    return render_template('landing.html', title='Home')
"""
@app.route('/', methods=['GET'])
def index():
    
    username = "prakhar897"

    commits = get_commits(username)
    body = get_pr_issues_body(username)

    body_list = [{
            "content": text,
            "content-type": "text/plain",
            "language": "en",
            "id": str(i)
        } for i, text in enumerate(body)
        ]

    aug_content_list = commits.copy()
    aug_content_list["contentItems"] += body_list

    aug_body = body + [comm["content"] for comm in commits["contentItems"]]
    text = ' '.join(aug_body)

    profile = personality_service.profile(
        str(aug_content_list),  # behavior not returned even for temporal data!
        'application/json',
        raw_scores=True,
        consumption_preferences=True).get_result()
    
    del profile["processed_language"]
    del profile["consumption_preferences"]
    del profile["warnings"]

    profile["personality"] = sorted(profile["personality"], key=lambda x: x["percentile"], reverse=True)
    
    for item in profile["personality"]:
        del item["trait_id"]
        del item["raw_score"]
        del item["significant"]
        del item["category"]
        for child in item["children"]:
            del child["trait_id"]
            del child["raw_score"]
            del child["significant"]
            #del item["category"]

    
    for key in ["needs", "values"]:
        for item in profile[key]:
            del item["trait_id"]
            del item["raw_score"]
            del item["significant"]
            del item["category"]
    
    profile["needs"] = sorted(profile["needs"], key=lambda x: x["percentile"], reverse=True)[:5]
    profile["values"] = sorted(profile["values"], key=lambda x: x["percentile"], reverse=True)[:5]


    print('Personality Insights done')


    avatar_url = get_avatar(username)

    response = requests.get(avatar_url)

    mask = np.array(Image.open(BytesIO(response.content)))
    wc = WordCloud(background_color="white", mask=mask,
               stopwords=stopwords, contour_width=10, contour_color='steelblue')
    # generate word cloud
    
    wc.generate(text)

    # store to file
    wc.to_file('static/cloud.jpg')

    nlu_response = naturalLanguageUnderstanding.analyze(
        text=' '.join(aug_body),
        features=Features(
            emotion=EmotionOptions(document=True)
            )
        ).get_result()

    response = {
        "username": username, "avatar-url": avatar_url, "profile": profile
        }
    response["profile"]["emotion"] = nlu_response["emotion"]["document"]["emotion"]

    return render_template('result.html', title='Home', resp=response)
    #return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
