from flask import Flask, jsonify
from flask_cors import CORS
from parry_sentiment_script import load_analyzer
from parry_sentiment_script import load_analyzer

app = Flask(__name__)
CORS(app)

analyzer = load_analyzer()

@app.route('/analyze/<text>', methods=['GET'])
def analyze_text(text):
    result = analyzer.polarity_scores(text)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)

'''
from flask import Flask, request, jsonify, send_from_directory

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

app = Flask(__name__, static_url_path='', static_folder='website')

# WEBSITE START
# Homepage
@app.route('/')
def serve_homepage():
    return send_from_directory('website', 'index.html')

# Serving the demo page
@app.route('/demo')
def serve_demo_page():
    return send_from_directory('website', 'demo.html')

# Serving the documentation page
@app.route('/documentation')
def serve_documation_page():
    return send_from_directory('website', 'documentation.html')


#WEBSITE END

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
    app.run(debug=True, port=5500)
   
'''