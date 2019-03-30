"""
Analyzes user data using IBM Watson Personality Insights
and Natural Language Understanding APIs.
"""

import json
import os

from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

from ibm_watson import PersonalityInsightsV3, NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import Features, ConceptsOptions, EntitiesOptions, KeywordsOptions

try:
    from credentials import NLU_KEY, PERSONALITY_INSIGHTS_KEY
except ModuleNotFoundError:  # For Heroku
    NLU_KEY = os.environ['NLU_KEY']
    PERSONALITY_INSIGHTS_KEY = os.environ['PERSONALITY_INSIGHTS_KEY']

from fetch_repos import get_commits, get_pr_issues_body, get_avatar

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

@app.route('/', methods=['POST'])
def index():
    username = request.form['username']

    commits = get_commits(username)
    body = get_pr_issues_body(username)

    body_list = [{
            "content": text,
            "contenttype": "text/plain",
            "language": "en"
        } for text in body
        ]

    aug_content_list = commits.copy()
    aug_content_list["contentItems"] += body_list

    aug_body = body + [comm["content"] for comm in commits["contentItems"]]

    profile = personality_service.profile(
        str(aug_content_list),  # behavior not returned even for temporal data!
        'application/json',
        raw_scores=True,
        consumption_preferences=True).get_result()
    print('Personality Insights done')
    nlu_response = naturalLanguageUnderstanding.analyze(
        text=' '.join(aug_body),
        features=Features(
            entities=EntitiesOptions(emotion=True, sentiment=True, limit=5),
            keywords=KeywordsOptions(emotion=True, sentiment=True),
            concepts=ConceptsOptions(limit=5)
            )
        ).get_result()
    print('NLU done')

    response = {
        'username': username, 'avatar-url': get_avatar(username), 'profile': profile,
        'nlu_response': nlu_response}  # Also, avatar url to be computed on FE.
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
