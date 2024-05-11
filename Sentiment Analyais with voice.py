# Import necessary libraries
import speech_recognition as sr
from textblob import TextBlob
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play

# Function to convert text to speech and play it
def text_to_speech(text):
    tts = gTTS(text)
    tts.save("output.mp3")
    sound = AudioSegment.from_mp3("output.mp3")
    play(sound)

# Initialize the speech recognition engine
recognizer = sr.Recognizer()

# Capture voice input
with sr.Microphone() as source:
    print("Please speak:")
    audio = recognizer.listen(source)

try:
    # Recognize speech using Google Web Speech API
    text = recognizer.recognize_google(audio)
    print(f"You said: {text}")

    # Analyze the text using TextBlob (NLU)
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity
    analysis = ""
    if sentiment > 0:
        analysis = "positive"
    elif sentiment < 0:
        analysis = "negative"
    else:
        analysis = "neutral"

    print(f"Sentiment: {analysis} (Polarity: {sentiment}, Subjectivity: {subjectivity})")

    # Convert the analysis to speech
    text_to_speech(f"You said: {text}. The sentiment analysis is {analysis}.")

except sr.UnknownValueError:
    print("Google Web Speech API could not understand audio")
except sr.RequestError as e:
    print(f"Could not request results from Google Web Speech API; {e}")

# Clean up
try:
    text_to_speech("Output text to speech.")
except Exception as e:
    print(f"Error playing audio: {e}")
