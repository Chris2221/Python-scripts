import speech_recognition as sr
import pyttsx3

# Define the function that responds to the user's message
def respond(message):
    if message == "Hello":
        return "Hi"
    elif message == "What are you?" or message == "Tell me about you":
        return "I'm the future"
    elif message == "Can you do math":
        return "No I'm too dumb to do Math"
    else:
        return "I don't understand what you're saying."

# speech recognizer and TTS engine
r = sr.Recognizer()
engine = pyttsx3.init()

# default microphone as the audio input source
with sr.Microphone(device_index=0) as source:
    print("Speak your message...")
    audio = r.listen(source)
    print("Processing...")

# Convert the audio to text using Google Cloud Speech-to-Text API
try:
    message = r.recognize_google(audio)
    print("You said:", message)
    response = respond(message)
    print("Chatbot:", response)
    engine.say(response)
    engine.runAndWait()
except sr.UnknownValueError:
    print("Sorry, I could not understand your message.")
except sr.RequestError:
    print("Sorry, I could not connect to the speech recognition service.")
    
