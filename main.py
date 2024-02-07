from flask import *
#from fastapi import FastAPI

import json

#Textblob 
from textblob import TextBlob
from dataclasses import dataclass
from textblob_sentiment_script import Mood
from textblob_sentiment_script import get_mood

#Vader
import nltk
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
#from vader_sentiment_script import 


app = Flask(__name__)

#Homepage
@app.route('/', methods= ['GET'])
def home_page():
    data_set = {'Page': 'Home', 'Message': 'Successfully loaded the Home page'}
    json_dump = json.dumps(data_set)

    return json_dump


#Textblob
@app.route('/textblob/<text>', methods=['GET'])
def textblob_request(text):
    mood: Mood = get_mood(text, threshold=0.3)
    result = mood
    return jsonify(result)

@app.route('/vader/<text>', methods=['GET'])
def vader_request(text):
    mood: Mood = get_mood(text, threshold=0.3)
    result = mood
    return jsonify(result)

"""    

@app.route('/textblob/request', methods=['GET'])
def textblob_request():
    
    mood: Mood = get_mood(data, threshold=0.3)
    data_set = {'Message': data, 'Mood': (f' {mood.emoji}({mood.sentiment})')}
    json_dump = json.dumps(data_set)
    return json_dump
"""

"""
#Vader
@app.route('/vader/request', methods=['POST'])
def vader_request():
    data = request.data
    result = analyze_text_with_vader(data['text'])
    return jsonify(result)

#Parry
@app.route('/parry/request', methods=['POST'])
def parry_request():
    data = request.json
    result = analyze_text_with_parry(data['text'])
    return jsonify(result)
"""

if __name__ == '__main__':
    app.run(debug=True, port=7777)
   
