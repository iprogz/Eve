import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QTextEdit, QLabel, QVBoxLayout, QHBoxLayout, QFileDialog
import pandas as pd
import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tag import pos_tag
from textblob import TextBlob
import test
import tasks
# Download necessary NLTK resources
nltk.download('punkt', quiet=True)
nltk.download('averaged_perceptron_tagger', quiet=True)

# Define process_text function with categorization & contextualization
def process_text(text, context):
    tokens = nltk.word_tokenize(text.lower())
    cleaned_tokens = [token for token in tokens if token.isalpha()]

    features = {
        "stemmed_words": [PorterStemmer().stem(word) for word in cleaned_tokens],
        "lemmatized_words": [WordNetLemmatizer().lemmatize(word) for word in cleaned_tokens],
        "pos_tags": pos_tag(cleaned_tokens),
        "named_entities": [],  # SpaCy named entities can be added here
        "sentiment": TextBlob(text).sentiment.polarity,
        "tags": []  # For user-defined tags
    }

    # Sentiment-based categorization
    if features["sentiment"] > 0.5:
        features["tags"].append("positive")
    elif features["sentiment"] < -0.5:
        features["tags"].append("negative")
    else:
        features["tags"].append("neutral")

    # Contextualization based on previous interactions (replace with your logic)
    if context["previously_mentioned_keywords"]:
        for keyword in context["previously_mentioned_keywords"]:
            if keyword in text:
                features["tags"].append("relevant")

    return features

# Function to display processed features with categorization and context
def display_processed_features(features, context):
    output_text = ""
    output_text += f"Sentiment: {features['sentiment']}\n"
    output_text += f"Tags: {', '.join(features['tags'])}\n"
    output_text += f"Contextually relevant keywords: {', '.join(context['previously_mentioned_keywords'])}"
    output_display.setText(output_text)

# Functions for data export with categorization and context
def export_raw_text():
    text = text_input.text()
    categories = ["sentiment", "tags", "context"]

    data = {category: [] for category in categories}
    data["sentiment"].append(process_text(text, context)["sentiment"])
    data["tags"].append(", ".join(process_text(text, context)["tags"]))
    data["context"].append(", ".join(context["previously_mentioned_keywords"]))

    file_path, _ = QFileDialog.getSaveFileName(window, "Export Raw Text", "", "Text Files (*.txt)")
    if file_path:
        with open(file_path, "w") as f:
            for category, values in data.items():
                f.write(f"{category}:\n")
                f.write("\t" + "\n\t".join(values) + "\n")

def export_processed_features():
    text = text_input.text()
    features = process_text(text, context)

    file_path, _ = QFileDialog.getSaveFileName(window, "Export Processed Features", "", "Excel Files (*.xlsx)")
    if file_path:
        pd.DataFrame(features, index=[0]).to_excel(file_path, index=False)

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Text Processing and Categorization")
window.setGeometry(100, 100, 800, 600)

# Create widgets
text_input = QLineEdit()
output_display = QTextEdit()
output_display.setReadOnly(True)

context = {"previously_mentioned_keywords": []}  # Replace with actual context data

# Create buttons
export_raw_text_button = QPushButton("Export Raw Text")
export_processed_features_button = QPushButton("Export Processed Features")

# Connect buttons to functions
export_raw_text_button.clicked.connect(export_raw_text)
export_processed_features_button.clicked.connect(export_processed_features)

# Create layouts
input_layout = QVBoxLayout()
input_layout.addWidget(QLabel("Enter Text:"))
input_layout.addWidget(text_input)
input_layout.addWidget(export_raw_text_button)
input_layout.addWidget(export_processed_features_button)

output_layout = QVBoxLayout()
output_layout.addWidget(QLabel("Processed Features:"))
output_layout.addWidget(output_display)

main_layout = QHBoxLayout()
main_layout.addLayout(input_layout)
main_layout.addLayout(output_layout)

window.setLayout(main_layout)
window.show()
sys.exit(app.exec_())