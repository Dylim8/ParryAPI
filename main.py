from flask import *
import json


from textblob import TextBlob
from dataclasses import dataclass
from textblob_sentiment_script import Mood
from textblob_sentiment_script import get_mood

app = Flask(__name__)

@app.route('/', methods= ['GET'])
def home_page():
    data_set = {'Page': 'Home', 'Message': 'Successfully loaded the Home page'}
    json_dump = json.dumps(data_set)

    return json_dump

@app.route('/request/', methods= ['GET'])
def request_page():
    textblob_query = str(request.args.get('request'))
    mood: Mood = get_mood(textblob_query, threshold=0.3)

    data_set = {'Page': 'Textblob request', 'Message': textblob_query, 'Mood': (f' {mood.emoji}({mood.sentiment})')}
    json_dump = json.dumps(data_set)

    return json_dump

if __name__ == '__main__':
    app.run(port=7777)