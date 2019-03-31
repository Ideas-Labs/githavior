# githavior
Project for HINT 4.0

## Development
First, create a `virtualenv` using `python3 -m venv venv`. Now install the dependencies using `pip3 install -r requirements.txt`. Next, add your API keys in `credentials.py` in `githavior/`:

```
PERSONALITY_INSIGHTS_KEY='Personality Insights API Key'
NLU_KEY='Natual Language Understanding  API Key'
```

Then, for profile analysis, run `githavior/analyzer.py <username>`.

See our [Devfolio submission](https://devfolio.co/submissions/githavior) for more information on the purpose and implementation challenges of this project.

See the project live @ [githavior.heroku.com](https://githavior.heroku.com)
