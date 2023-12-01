# Create a program for sentiment analysis using a machine learning model.
print("\nRuban Gino Singh - Day 66 of #100DaysOfCode\n")

print("Create a python program for sentiment analysis using a machine learning model\n")

# pip install textblob
from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    
    polarity = blob.sentiment.polarity
    
    if polarity > 0:
        return 'Positive'
    elif polarity < 0:
        return 'Negative'
    else:
        return 'Neutral'

def main():
    text = input("Enter the text for sentiment analysis: ")
    
    sentiment = analyze_sentiment(text)

    print(f"Sentiment: {sentiment}")

if __name__ == "__main__":
    main()

# --------------------------------------------------------- #