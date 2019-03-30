"""
Analyzes user data using IBM Watson Personality Insights
and Natural Language Understanding APIs.
"""

from ibm_watson import PersonalityInsightsV3
from credentials import PERSONALITY_INSIGHTS_KEY

service = PersonalityInsightsV3(
    version='2017-10-13',
    url='https://gateway-lon.watsonplatform.net/personality-insights/api',
    username='apikey',
    password=PERSONALITY_INSIGHTS_KEY)

with open('profile.json') as profile_json:
    profile = service.profile(
        profile_json.read(),
        'application/json',
        raw_scores=True,
        consumption_preferences=True).get_result()
