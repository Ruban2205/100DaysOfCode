# Create a program to perform text summarization using natural language processing.
print("\nRuban Gino Singh - Day 72 of #100DaysOfCode\n")

print("Python program to perform text summarization using Natural Language Processing\n")

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.probability import FreqDist

nltk.download('punkt')
nltk.download('stopwords')

def get_text_summary(text, num_sentences=5):
    sentences = sent_tokenize(text)

    words = word_tokenize(text)

    stop_words = set(stopwords.words('english'))
    words = [word.lower() for word in words if word.isalnum() and word.lower() not in stop_words]

    word_freq = FreqDist(words)

    sentence_scores = {}
    for sentence in sentences:
        for word, freq in word_freq.items():
            if word in sentence.lower():
                if sentence in sentence_scores:
                    sentence_scores[sentence] += freq
                else:
                    sentence_scores[sentence] = freq

    summary_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:num_sentences]

    return ' '.join(summary_sentences)

if __name__ == "__main__":
    input_text = """
    Natural language processing (NLP) is a subfield of artificial intelligence (AI) that focuses on the interaction
    between computers and humans using natural language. It involves the development of algorithms and models that
    enable computers to understand, interpret, and generate human-like text. NLP has applications in various domains,
    including machine translation, sentiment analysis, and text summarization.

    Text summarization is the process of distilling the most important information from a source text while retaining its
    core meaning. It is useful for generating concise summaries of lengthy articles, documents, or other textual content.
    In this program, we will use the Natural Language Toolkit (nltk) to perform extractive text summarization.

    To use this program, provide the input text that you want to summarize. The program will output a summary containing
    the most relevant sentences from the original text.

    Let's test the program with a sample text. You can replace this text with your own input.
    """

    num_summary_sentences = 3

    summary = get_text_summary(input_text, num_summary_sentences)

    print("Original Text:\n", input_text)
    print("\nText Summary:\n", summary)

# --------------------------------------------------------- #