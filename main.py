from flask import *

import json

# Textblob 
from textblob import TextBlob
from dataclasses import dataclass
from textblob_sentiment_script import Mood
from textblob_sentiment_script import get_mood

# Vader
import nltk
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Parry
from parry_sentiment_script import additional_terms

app = Flask(__name__)

# Homepage
@app.route('/', methods= ['GET'])
def home_page():
    data_set = {'Page': 'Home', 'Message': 'Successfully loaded the Home page'}
    json_dump = json.dumps(data_set)

    return json_dump

# Textblob
@app.route('/textblob/<text>', methods=['GET'])
def textblob_request(text):
    mood: Mood = get_mood(text, threshold=0.3)
    result = mood
    return jsonify(result)

# Vader
@app.route('/vader/<text>', methods=['GET'])
def vader_request(text):
    vs = vader.polarity_scores(text)
    result = vs
    return jsonify(result)

# Parry
@app.route('/parry/<text>', methods=['GET'])
def parry_request(text):
    ps = parry.polarity_scores(text)
    result = ps
    return jsonify(result)

if __name__ == '__main__':
    vader = SentimentIntensityAnalyzer()
    parry = SentimentIntensityAnalyzer()
    parry.lexicon.update(additional_terms)
    app.run(debug=True, port=7777)
   
