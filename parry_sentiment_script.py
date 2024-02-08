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
    'kys': -2.0
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
            update_unknown_words_file(word, "parry_unknown_words.txt")

def update_unknown_words_file(word, file_path = "parry_unknown_words.txt"):
    # Load existing data into a dictionary
    word_tally = {}
    try:
        with open(file_path, "r") as file:
            for line in file:
                word, count = line.strip().split(':')
                word_tally[word] = int(count)
    except FileNotFoundError:
        pass  # If the file doesn't exist, proceed with an empty dictionary

    # Update the dictionary with the new word
    word = word.lower()  # Ensure consistency in casing
    if word in word_tally:
        word_tally[word] += 1
    else:
        word_tally[word] = 1

    # Write the updated dictionary back to the file
    with open(file_path, "w") as file:
        for word, count in word_tally.items():
            file.write(f"{word}:{count}\n")

if __name__ == '__main__':
    vader_update()
    while True:
        #testing()
        training()
    