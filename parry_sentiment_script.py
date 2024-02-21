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
    'glhf': 1.0,
    'kys': -2.0,
    'uninstall':-1.0
}

def vader_update():
    analyzer.lexicon.update(additional_terms)
    print('updated')

def testing():
    print('testing')
    text: str = input('Text: ')
    vs = analyzer.polarity_scores(text)
    print('{:-<65} {}'.format(text, str(vs)))

def training():
    print('training')
    text: str = input('Text: ')
    words = text.split()
    for word in words:
        if word.lower() in analyzer.lexicon:  # Convert to lowercase to match the lexicon's format
            print(f"'{word}' is in the lexicon with a sentiment score of {analyzer.lexicon[word.lower()]}")
        else:
            print(f"'{word}' is not in the lexicon ")
            update_unknown_words(word)
            
def update_unknown_words(word, file_path="parry_unknown_words.txt"):
    found = False
    updated_lines = []
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
            for line in lines:
                existing_word, count = line.strip().split(':')
                if existing_word == word.lower():
                    count = int(count) + 1
                    line = f"{existing_word}:{count}\n"
                    found = True
                updated_lines.append(line)
        if not found:
            updated_lines.append(f"{word.lower()}:1\n")                                                         
        with open(file_path, "w") as file:
            file.writelines(updated_lines)
    except FileNotFoundError:
        with open(file_path, "w") as file:
            file.write(f"{word.lower()}:1\n")

if __name__ == '__main__':
    vader_update()
    while True:
        #testing()
        training()
    