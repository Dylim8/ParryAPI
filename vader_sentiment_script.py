import nltk
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

if __name__ == '__main__':
    while True:
        text: str = input('Text: ')
        ps = analyzer.polarity_scores(text)
        print('{:-<65} {}'.format(text, str(ps)))