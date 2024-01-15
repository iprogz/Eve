# Import necessary libraries
import speech_recognition as sr
from textblob import TextBlob
from bard import *  # Import Bard class for API access

# Voice recognition setup
r = sr.Recognizer()

def parse_commands(user_input):
    """
    Segment user input based on semicolons and handle potential errors.
    """
    try:
        commands = user_input.split(';')
        return commands
    except Exception as e:
        print(f"Error parsing commands: {e}")
        return None

def execute_command(command):
    """
    Execute Linux commands or call Bard functionality based on command type.
    """
    try:
        # Check if command starts with "bard:"
        if command.startswith("bard:"):
            # Extract specific functionality and arguments
            action, *args = command[5:].split(' ')
            return Bard().action(action, *args)  # Call Bard API based on action

        # Otherwise, execute as a shell command
        else:
            subprocess.run(command, shell=True, check=True, text=True)
            return "Command executed successfully."
    except subprocess.CalledProcessError as e:
        return f"Error executing command: {str(e)}"

def perform_sentiment_analysis(text):
    """
    Analyze sentiment of text using TextBlob
    """
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

        # Parse commands and handle errors
        commands = parse_commands(user_input)
        if not commands:
            continue

        # Analyze user sentiment
        user_sentiment = perform_sentiment_analysis(user_input)

        # Process and execute each command
        responses = []
        for command in commands:
            response = execute_command(command)
            responses.append(response)

        # Analyze response sentiment
        response_sentiments = [perform_sentiment_analysis(response) for response in responses]

        # Print feedback and results
        print("User Sentiment:", user_sentiment)
        print("Response Sentiments:", response_sentiments)
        print("Responses:")
        for i, response in enumerate(responses):
            print(f"Response {i + 1}: {response}")

    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
    except sr.RequestError as e:
        print("An error occurred with the speech recognition service:", e)

