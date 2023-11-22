# Implement a basic natural language processing (NLP) pipeline.
print("\nRuban Gino Singh - Day 57 of #100DaysOfCode\n")

print("Python program to Implement a basic Natural Language Processing (NLP)\n")

import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag, ne_chunk

nltk.download('punkt')
nltk.download('maxent_ne_chunker')
nltk.download('words')

def nlp_pipeline(text):
    # Tokenization
    tokens = word_tokenize(text)
    print("Tokenization:")
    print(tokens)
    print("\n")

    # Part-of-speech tagging
    pos_tags = pos_tag(tokens)
    print("Part-of-speech tagging:")
    print(pos_tags)
    print("\n")

    # Named Entity Recognition (NER)
    ner_result = ne_chunk(pos_tags)
    print("Named Entity Recognition:")
    print(ner_result)
    print("\n")

if __name__ == "__main__":
    text = "Natural Language Processing is a fascinating field of study."

    nlp_pipeline(text)

# --------------------------------------------------------- #