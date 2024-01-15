import speech_recognition as sr
import subprocess
from textblob import TextBlob

# Voice recognition setup
r = sr.Recognizer()

def execute_command(command):
    try:
        subprocess.run(command, shell=True, check=True, text=True)
        return "Command executed successfully."
    except subprocess.CalledProcessError as e:
        return f"Error executing command: {str(e)}"

def perform_sentiment_analysis(text):
    sentiment = TextBlob(text).sentiment.polarity
    if sentiment > 0:
        return "Positive"
    elif sentiment < 0:
        return "Negative"
    else:
        return "Neutral"

# Main loop for listening to voice commands
while True:
    with sr.Microphone() as source:
        print("Listening for voice commands...")
        audio = r.listen(source)

    try:
        # Convert audio to text using speech recognition
        user_input = r.recognize_google(audio)
        print("User:", user_input)

        # Perform segmentation to identify and parse user commands
        commands = user_input.split(';')  # Assuming commands are separated by semicolons
        responses = []

        for command in commands:
            # Execute the Linux command
            response = execute_command(command)
            responses.append(response)

        # Perform sentiment analysis on user commands and responses
        user_sentiment = perform_sentiment_analysis(user_input)
        response_sentiments = [perform_sentiment_analysis(response) for response in responses]

        print("User Sentiment:", user_sentiment)
        print("Response Sentiments:", response_sentiments)
        print("Responses:")
        for i, response in enumerate(responses):
            print(f"Response {i + 1}: {response}")

    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
    except sr.RequestError as e:
        print("An error occurred with the speech recognition service:", e)

