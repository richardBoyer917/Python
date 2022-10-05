# MODULES
import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import os
import random
from requests import get
import pyjokes

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# WISH ME
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir!")

    else:
        speak("Good Evening Sir!")

    speak("ALPHA Here,How may i help you?")


def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


def run_alpha():
    wishMe()
    query = takeCommand()
    print(query)

    # SEARCH SOMETHING ON GOOGLE
    if 'search on google' in query:
        speak("What would you like to search on google?")
        cm = takeCommand().lower()
        webbrowser.open(f"{cm}")

# WHATS THE TIME
    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The Time is {strTime}")

# SIMPLE TALKS
    elif "what\'s up" in query or 'how are you' in query:
        stMsgs = [
            'Just doing my thing!', 'I am fine!', 'Nice!',
            'I am nice and full of energy', 'i am okey ! How are you'
        ]
        ans_q = random.choice(stMsgs)
        speak(ans_q)
        ans_take_from_user_how_are_you = takeCommand()
        if 'fine' in ans_take_from_user_how_are_you or 'happy' in ans_take_from_user_how_are_you or 'okey' in ans_take_from_user_how_are_you:
            speak('okey..')
        elif 'not' in ans_take_from_user_how_are_you or 'sad' in ans_take_from_user_how_are_you or 'upset' in ans_take_from_user_how_are_you:
            speak('oh sorry..')
    elif 'make you' in query or 'created you' in query or 'develop you' in query:
        ans_m = " For your information Sachin Lohar AKA ALPHA Created me ! I give Lot of Thannks to Him "
        print(ans_m)
        speak(ans_m)
    elif "who are you" in query or "about you" in query or "your details" in query:
        about = "I am ALPHA an A I based computer program but i can help you lot like a your close friend ! i promise you ! Simple try me to give simple command ! like playing music or video from your directory i also play video and song from web or online ! i can also entain you i so think you Understand me ! ok Lets Start "
        print(about)
        speak(about)
    elif "hello" in query or "hello ALPHA" in query:
        hel = "Hello Sir ! How May i Help you.."
        print(hel)
        speak(hel)
    elif "your name" in query or "sweat name" in query:
        na_me = "Thanks for Asking my name my self ! ALPHA"
        print(na_me)
        speak(na_me)
    elif "you feeling" in query:
        print("feeling Very sweet after meeting with you")
        speak("feeling Very sweet after meeting with you")
#IP ADDRESS
    elif "ip address" in query:
        ip = get('https://api.ipify.org').text
        speak(f"Your IP address is {ip}")
# JOKE
    elif "Tell me a joke" in query:
        joke = pyjokes.get_joke()
        speak(joke)

# SHUTDOWN
    elif "shut down the system" in query:
        os.system("shutdown /s /t 5")
# RESTART
    elif "restart the system" in query:
        os.system("shutdown /r /t 5")


# SLEEP
    elif "sleep the system" in query:
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

while True:
    run_alpha()
