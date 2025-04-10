import os
import re
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def normalize_obfuscated_text(text):
    substitutions = {
        '@': 'a',
        '4': 'a',
        '3': 'e',
        '!': 'i',
        '1': 'i',
        '|': 'i',
        '$': 's',
        '5': 's',
        '0': 'o',
        '*': '',
        '#': 'h',
        '+': 't'
    }

    pattern = re.compile('|'.join(re.escape(k) for k in substitutions.keys()))

    def replace(match):
        return substitutions[match.group(0)]

    return pattern.sub(replace, text.lower())

def load_analyzer(custom_lexicon_path="custom_lexicon.txt"):
    analyzer = SentimentIntensityAnalyzer()
    if os.path.exists(custom_lexicon_path):
        with open(custom_lexicon_path, "r") as file:
            for line in file:
                if line.strip() and not line.startswith("#"):
                    try:
                        word, score = line.strip().split()
                        analyzer.lexicon[word] = float(score)
                    except ValueError:
                        print(f"Skipping malformed line: {line.strip()}")
        print("✅ Custom lexicon loaded.")
    else:
        print("⚠️ No custom lexicon found.")
    return analyzer

# Initialize analyzer with custom terms
analyzer = load_analyzer()

def analyze_text(text):
    normalized = normalize_obfuscated_text(text)
    return analyzer.polarity_scores(normalized)

if __name__ == "__main__":
    while True:
        raw = input("Text: ")
        result = analyze_text(raw)
        print(result)