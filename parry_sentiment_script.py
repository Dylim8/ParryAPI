import nltk
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

# custom words and sentiment scores (-4.0-4.0)
additional_terms = {
    'nt': 1.0,  
    'gg': 1.3,  
    'gl': 1.0,
    'wp': 1.1,
    'ns': 1.0,
    'kys': -2.0
}


if __name__ == '__main__':
    analyzer.lexicon.update(additional_terms)
    print('updated')
    while True:
        text: str = input('Text: ')
        vs = analyzer.polarity_scores(text)
        print('{:-<65} {}'.format(text, str(vs)))