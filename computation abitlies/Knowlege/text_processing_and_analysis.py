import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tag import pos_tag
import spacy
from textblob import TextBlob
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Download necessary NLTK resources if not already available
nltk.download('punkt', quiet=True)
nltk.download('averaged_perceptron_tagger', quiet=True)

# Load the English model for spaCy
nlp = spacy.load("en_core_web_sm")

def process_text(text):
    """Processes text and extracts various features."""

    tokens = nltk.word_tokenize(text.lower())
    cleaned_tokens = [token for token in tokens if token.isalpha()]

    features = {
        "stemmed_words": [PorterStemmer().stem(word) for word in cleaned_tokens],
        "lemmatized_words": [WordNetLemmatizer().lemmatize(word) for word in cleaned_tokens],
        "pos_tags": pos_tag(cleaned_tokens),
        "named_entities": [(ent.text, ent.label_) for ent in nlp(text).ents],
        "sentiment": TextBlob(text).sentiment.polarity
    }

    return features

def batch_process_texts(texts):
    """Processes a batch of texts and returns a list of features."""

    all_features = []
    for text in texts:
        features = process_text(text)
        all_features.append(features)
    return all_features

def visualize_data(dataframe):
    """Visualizes the extracted features."""

    sns.set(style="whitegrid")
    plt.figure(figsize=(10, 6))

    # Sentiment Distribution
    plt.subplot(2, 1, 1)
    sns.histplot(dataframe['sentiment'], kde=True, color="blue")
    plt.title("Sentiment Polarity Distribution")
    plt.xlabel("Polarity")
    plt.ylabel("Frequency")

    # Part-of-Speech Tag Distribution
    pos_counts = nltk.FreqDist(tag for words, tag in dataframe['pos_tags'].explode())
    plt.subplot(2, 1, 2)
    pos_counts.plot(30, title="Part-of-Speech Tag Distribution")

    plt.tight_layout()
    plt.show()

def main():
    """Main function to execute the code."""

    try:
        texts = [
            "This is a great product! I love its features and ease of use.",
            "I'm not happy with this product. It doesn't meet my expectations.",
            "Decent quality, but the price is too high."
        ]

        batched_features = batch_process_texts(texts)
        results_df = pd.DataFrame(batched_features)

        print("\nDataFrame representation:")
        print(results_df.to_string())

        visualize_data(results_df)

        # Additional analysis can be added here
        # Example: Preparing data for a machine learning model
        # ...

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

