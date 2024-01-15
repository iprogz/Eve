import os
import librosa
import numpy as np
import matplotlib.pyplot as plt


class AIBot:
    def __init__(self):
        self.eve = Eve()

    def process_query(self, query):
        if query == "classify":
            file_path = input("Enter the file path: ")
            self.eve.classify_data(file_path)
        elif query == "help":
            self.display_help()
        elif query == "exit":
            print("Goodbye!")
            return False
        else:
            print("Invalid query. Type 'help' for a list of available commands.")
        return True

    def display_help(self):
        print("Available commands:")
        print("- classify: Classify a file and move it to the corresponding folder.")
        print("- help: Display the list of available commands.")
        print("- exit: Exit the AI bot.")


class EveTraits:
    def __init__(self, intelligence, knowledge, skills, charisma, emotional_intelligence, creativity, adaptability,
                 openness, conscientiousness, extraversion, introversion):
        self.intelligence = intelligence
        self.knowledge = knowledge
        self.skills = skills
        self.charisma = charisma
        self.emotional_intelligence = emotional_intelligence
        self.creativity = creativity
        self.adaptability = adaptability
        self.openness = openness
        self.conscientiousness = conscientiousness
        self.extraversion = extraversion
        self.introversion = introversion


class Eve(EveTraits):
    def __init__(self):
        super().__init__(intelligence=8, knowledge=9, skills=7, charisma=6, emotional_intelligence=9, creativity=8,
                         adaptability=7, openness=9, conscientiousness=8, extraversion=6, introversion=4)

    def classify_data(self, file_path):
        file_name, file_ext = os.path.splitext(file_path)

        categories = {
            ".jpg": "Photos",
            ".png": "Photos",
            ".mp4": "Videos",
            ".mov": "Videos",
            ".doc": "Documents",
            ".docx": "Documents",
            ".pdf": "Documents",
            ".txt": "Text",
            ".csv": "Data",
            ".xlsx": "Data",
            ".wav": "Audio"
        }

        if file_ext in categories:
            folder_name = categories[file_ext]
            if not os.path.exists(folder_name):
                os.makedirs(folder_name)

            os.rename(file_path, os.path.join(folder_name, file_name + file_ext))
            print(f"File {file_name}{file_ext} has been moved to {folder_name} folder.")

            if file_ext == ".wav":
                y, sr = librosa.load(os.path.join(folder_name, file_name + file_ext))

                D = np.abs(librosa.stft(y))**2
                power_spectrum = librosa.power_to_db(D)

                plt.figure(figsize=(10, 4))
                librosa.display.specshow(power_spectrum, y_axis='log', x_axis='time')
                plt.colorbar(format='%+2.0f dB')
                plt.title('Power Spectrum')
                plt.xlabel('Time (seconds)')

                rms = librosa.feature.rms(y=y)
                emotion = "Neutral"
                if np.mean(rms) > 0.01:
                    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=20)
                    mean_mfccs = np.mean(mfccs, axis=1)
                    if mean_mfccs[0] > -70:
                        emotion = "Happy"
                    elif mean_mfccs[0] > -190:
                        emotion = "Sad"
                    else:
                        emotion = "Angry"

                print(f"Emotion detected in {file_name}{file_ext}: {emotion}")

                amplification = "Low"
                if np.max(power_spectrum) > -10:
                    amplification = "High"

                print(f"Voice amplification elevation detected in {file_name}{file_ext}: {amplification}")
        else:
            print("File extension not supported.")


def main():
    print("Welcome to AI Bot!")
    bot = AIBot()

    while True:
        query = input("Enter your query: ")
        if not bot.process_query(query.lower()):
            break


if __name__ == "__main__":
    main()