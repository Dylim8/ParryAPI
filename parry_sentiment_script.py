import nltk
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

# custom words and sentiment scores (-4.0-4.0)
additional_terms = {
    'nt': 1.0,  
    'gg': 1.3,  
    'gl': 1.0,
    'hf': 1.0,
    'wp': 1.1,
    'ns': 1.0,
    'ggwp': 1.0,
    'kys': -2.0
}

def vader_update():
    analyzer.lexicon.update(additional_terms)
    print('updated')


if __name__ == '__main__':
    vader_update()
    while True:
        text: str = input('Text: ')
        vs = analyzer.polarity_scores(text)
        print('{:-<65} {}'.format(text, str(vs)))