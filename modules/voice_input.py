# voice_input.py
import speech_recognition as sr

def listen_for_audio():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for audio...")
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Sorry, I didn't understand that.")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return ""
