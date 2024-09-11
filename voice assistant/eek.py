import speech_recognition as sr
import pyttsx3
import subprocess
import webbrowser


recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return None
        except sr.RequestError:
            print("Sorry, there was an issue with the speech recognition service.")
            return None

def open_application(app_name):
    try:
        if app_name == 'chrome':
            subprocess.run(['google-chrome'])
        elif app_name == 'rhythmbox':
            subprocess.run(['rhythmbox'])
        elif app_name == 'cheese':
            subprocess.run(['cheese'])
        elif app_name == 'terminal':
            subprocess.run(['gnome-terminal'])
        elif app_name == 'brave':
            subprocess.run(['brave'])
        elif app_name == 'chatgpt':
            webbrowser.open('https://chat.openai.com')
        else:
            speak("I don't know how to open that application.")
    except Exception as e:
        print(f"An error occurred: {e}")
        speak("There was an error opening the application.")

def main():
    speak("Hello, how can I assist you today?")
    #speak("mai aapki kya maddat kar sakta hu ")
    while True:
        command = listen()
        if command:
            command = command.lower()
            if 'exit' in command:
                speak("Goodbye!")
                break
            elif 'open music' in command or 'rhythmbox' in command:
                open_application('rhythmbox')
            elif 'open camera' in command or 'cheese' in command:
                open_application('cheese')
            elif 'open terminal' in command:
                open_application('terminal')
            elif 'open chatgpt' in command:
                open_application('chatgpt')
            elif 'open chrome' in command:
                open_application('chrome')
            elif 'open brave' in command:
                open_application('brave')
            else:
                speak("I did not understand your command.")

if __name__ == "__main__":
    main()
