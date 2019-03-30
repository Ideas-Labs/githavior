"""
Analyzes user data using IBM Watson Personality Insights
and Natural Language Understanding APIs.
"""
import json
from ibm_watson import PersonalityInsightsV3, NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import Features, ConceptsOptions, EntitiesOptions, KeywordsOptions
from credentials import NLU_KEY, PERSONALITY_INSIGHTS_KEY

personality_service = PersonalityInsightsV3(
    version='2017-10-13',
    url='https://gateway-lon.watsonplatform.net/personality-insights/api',
    username='apikey',
    password=PERSONALITY_INSIGHTS_KEY)

with open('profile.json') as profile_json:
    profile = personality_service.profile(
        profile_json.read(),  # behavior not returned even for temporal data!
        'application/json',
        raw_scores=True,
        consumption_preferences=True).get_result()
print(json.dumps(profile, indent=4))

naturalLanguageUnderstanding = NaturalLanguageUnderstandingV1(
    version='2018-11-16',
    url='https://gateway-lon.watsonplatform.net/natural-language-understanding/api',
    username='apikey',
    password=NLU_KEY)

nlu_response = naturalLanguageUnderstanding.analyze(
    text='IBM is an American multinational technology company '
    'headquartered in Armonk, New York, United States, '
    'with operations in over 170 countries.',
    features=Features(
        entities=EntitiesOptions(emotion=True, sentiment=True, limit=5),
        keywords=KeywordsOptions(emotion=True, sentiment=True),
        concepts=ConceptsOptions(limit=5)
        )
    ).get_result()

print(json.dumps(nlu_response, indent=4))
