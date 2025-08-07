import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import pyjokes

engine = pyttsx3.init()

def speak(text):
    print("🤖 PyBuddy:", text)
    engine.say(text)
    engine.runAndWait()

def wish_user():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good Morning!")
    elif hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am PyBuddy, your virtual assistant. How can I help you?")

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print("🔍 Recognizing...")
        command = r.recognize_google(audio)
        print(f"🗣️ You said: {command}\n")
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that.")
        return "None"
    except sr.RequestError:
        speak("Sorry, my speech service is down.")
        return "None"
    return command.lower()

def run_pybuddy():
    wish_user()
    while True:
        command = take_command()

        if 'time' in command:
            time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The time is {time}")

        elif 'date' in command:
            date = datetime.datetime.now().strftime("%B %d, %Y")
            speak(f"Today is {date}")

        elif 'open youtube' in command:
            webbrowser.open("https://www.youtube.com")
            speak("Opening YouTube")

        elif 'open google' in command:
            webbrowser.open("https://www.google.com")
            speak("Opening Google")

        elif 'search' in command:
            speak("What should I search for?")
            query = take_command()
            url = f"https://www.google.com/search?q={query}"
            webbrowser.open(url)
            speak(f"Searching for {query}")

        elif 'joke' in command:
            joke = pyjokes.get_joke()
            speak(joke)

        elif 'exit' in command or 'bye' in command or 'goodbye' in command:
            speak("Goodbye! Have a nice day!")
            break

        elif 'none' in command:
            continue

        else:
            speak("I didn’t understand that. Please try again.")

if __name__ == "__main__":
    run_pybuddy()
