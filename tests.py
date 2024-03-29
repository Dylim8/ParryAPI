# Textblob 
from textblob import TextBlob
from dataclasses import dataclass
from textblob_sentiment_script import Mood
from textblob_sentiment_script import get_mood

# Vader
import nltk
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
vader = SentimentIntensityAnalyzer()
    
# Parry
from parry_sentiment_script import additional_terms
parry = SentimentIntensityAnalyzer()
parry.lexicon.update(additional_terms)

# test parameters

# basic texts and phrases (including quotes)
standard_phrases = [
    # positive
    "You did an amazing job on this project!",
    "I'm thrilled with the results we achieved together.",
    "This experience has been incredibly rewarding.",
    "Your support has been a key factor in our success.",

    # neutral
    "The meeting is scheduled for tomorrow afternoon.",
    "Please update the document with the latest figures.",
    "The weather forecast predicts rain later this week.",
    "We need to check the inventory before our next order.",

    # negative
    "I'm disappointed with the lack of progress.",
    "This mistake has set us back several weeks.",
    "I'm unhappy with the quality of the work presented.",
    "The feedback on this has been predominantly negative."
]

# game phrases
game_phrases = [
    "good game",
    "nice try",
    "nice shot",
    "good luck",
    "well played",
    "good luck have fun",
    "good game well played"
]
game_phrases_abr = [
    "gg",
    "nt",
    "ns",
    "gl",
    "wp",
    "glhf",
    "ggwp"
]

# standard phrases 
def standard_test():
    print('basic texts and phrases:')
    print('--------------------------------------------------------------------------------------------')
    for phrase in standard_phrases:
        print("phrase: ", phrase)

        # textblob
        mood: Mood = get_mood(phrase, threshold=0.3)
        print("textblob: ", mood)

        # vader
        vs = vader.polarity_scores(phrase)
        print("vader: ", vs)

        # parry
        ps = parry.polarity_scores(phrase)
        print("parry: ", ps)
        print('')
    print('--------------------------------------------------------------------------------------------')

# game phrases
def game_test():
    print('basic game phrases:')
    print('--------------------------------------------------------------------------------------------')
    for phrase in game_phrases:
        print("phrase: ", phrase)

        # textblob
        mood: Mood = get_mood(phrase, threshold=0.3)
        print("textblob: ", mood)

        # vader
        vs = vader.polarity_scores(phrase)
        print("vader: ", vs)

        # parry
        ps = parry.polarity_scores(phrase)
        print("parry: ", ps)
        print('')
    print('--------------------------------------------------------------------------------------------')

# abreviated game phrases
def abr_game_test():
    print('basic abreviated game phrases:')
    print('--------------------------------------------------------------------------------------------')
    for phrase in game_phrases_abr:
        print("phrase: ", phrase)

        # textblob
        mood: Mood = get_mood(phrase, threshold=0.3)
        print("textblob: ", mood)

        # vader
        vs = vader.polarity_scores(phrase)
        print("vader: ", vs)

        # parry
        ps = parry.polarity_scores(phrase)
        print("parry: ", ps)
        print('')
    print('--------------------------------------------------------------------------------------------')

if __name__ == '__main__':
    # test start
    print('')
    print('the following are tests that compare the results of the 3 models(textblob, vader, and parry)')
    print('--------------------------------------------------------------------------------------------')
    standard_test()
    game_test()
    abr_game_test()