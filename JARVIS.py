"""
1. able to speak: text to speech (tts) - gtts, pyttsx3
2. understand: speech recognition (voice to text)


Good bye
Jokes
Sites
Message on whatsapp 
Screenshot 
Greetings
Hi/hello
Date and day
Opening app
Weather 
current Location
"""

import pyttsx3
import speech_recognition as sr
from random import choice
import webbrowser
import pywhatkit
import datetime
from AppOpener import open,close
import requests, json
import geocoder
from PIL import ImageGrab ,Image
import time
import playsound

jokes = [
    """Why did an old man fall in a well?
    Because he couldn’t see that well!""",
    """Why did the actor fall through the floorboards?
They were going through a stage!""",
    """Why did a scarecrow win a Nobel prize?
He was outstanding in his field!""",
    """Why are peppers the best at archery?
Because they habanero!""",
    """What did the duck say after she bought chapstick?
Put it on my bill!""",
    """What do you call a fake noodle?
An impasta!""",
    """What did the three-legged dog say when he walked into a saloon?
“I’m looking for the man who shot my paw!”""",
    """How do you tell the difference between a bull and a cow?
It is either one or the udder!""",
    """What’s red and smells like blue paint?
Red paint!""",
    """What’s the difference between a hippo and a Zippo?
One is very heavy, the other is a little lighter!""",
]

greetings = ["""I'm fine   You are very kind to ask""",
             """Excellent""",
             """I'm good""",
             """I'm doing Great""",
             """I'm doing really well,Thank you""",
             """The best i can be. Assuming you're at your best too""",
             """Very well , thanks""",
             """Pretty good!!""",
             """Well enough to help you""",
             """Much better now that you are with me!!""",
             """Imagining myself having a fabulous vacation, but you disturbed it""",
             """Horrible, now that I've met you."""]

greets = ["""Hello how can i help you ? """, """Hello, Nice to see you!!"""]

engine = pyttsx3.init()
engine.setProperty("rate", 170)


voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def welcome():
    # write your code here
    pass


def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    # print(audio)
    # recognize speech using Google Speech Recognition
    try:
        text = r.recognize_google(audio)
        print("I think you said:- " + text)

    except sr.UnknownValueError:
        print(
            "Sorry, I can't understand what you just said. Could you speak that again?"
        )
        text = ""

    except sr.RequestError as e:
        print(
            "Could not request results from Google Speech Recognition service; {0}".format(
                e
            )
        )
        text = ""

    return text


# talk("Good Morning! Say something...")
HOUR = datetime.datetime.now().hour  # the current hour
if HOUR < 12 and HOUR >= 5:
    talk("Hey , i am Jarvis , Good Morning! How can i help you?")
elif HOUR < 17 and HOUR >= 12:
    talk("Hey , i am Jarvis , Good Afternoon! How can i help you?")
elif HOUR <= 23 and HOUR >= 17:
    talk("Hey , i am Jarvis , Good Evening! How can i help you?")
elif HOUR < 5 and HOUR >= 0:
    talk("Hey , i am Jarvis , I think it was a hactic day for you,You should go to sleep....")


"""
5am to 12pm: Good Morning
12pm to 5pm: Good Afternoon
5pm to 12am: Good Evening
12am to 5am: You should go to sleep
"""
count=0
while True:
    query = listen().lower()
#---------------------------------------GOOD BYE-------------------------------------------------
    if "bye" in query or "see you" in query:
        talk("Good bye Yashvi")
        break
#---------------------------------------JOKES-------------------------------------------------
    elif "joke" in query or "make me laugh" in query:
        joke = choice(jokes)
        print(joke)
        talk(joke)
#---------------------------------------SITES-------------------------------------------------
    elif "." in query:  # please open google.com
        for string in query.split():
            if "." in string:
                url = string
        if "www." not in url:
            url = "www." + url
        webbrowser.open(url)


#---------------------------------------MESSAGE ON WHATSAPP-------------------------------------------------
    elif "whatsapp" in query:
        if "send" in query:
            query = query.replace("send", "")
        if "whatsapp" in query:
            query = query.replace("whatsapp", "")
        n=input("Enter the number:")
        pywhatkit.sendwhatmsg_instantly(n   , query)

#---------------------------------------SCREENSHOT-------------------------------------------------
    elif "screenshot" in query:
        ss_img = ImageGrab.grab()
        count+=1
        ss_img.save()
        ss_img.show()
#---------------------------------------GREETINGS-------------------------------------------------
    elif "how are you" in query:
        greet = choice(greetings)
        print(greet)
        talk(greet)
#---------------------------------------HII/HELLO-------------------------------------------------
    elif "hi" in query or "hello" in query:
        hi = choice(greets)
        print(hi)
        talk(hi)
#---------------------------------------DATE AND DAY-------------------------------------------------
    elif "today's date" in query or "today's day" in query:

        day = (datetime.datetime.today().strftime("%B %d, %Y")) + "   "+(datetime.datetime.now().strftime("%A"))
        print(day)
        talk(day)
#---------------------------------------OPENING APP-------------------------------------------------
    elif "open" in query:
        i=query[5:]
        print("OPENING",i)
        open(i)
            
    elif "close" in query:
        i=query[6:]
        print("CLOSING",i)
        close(i) 
#---------------------------------------WEATHER-------------------------------------------------
    elif "weather" in query:
        BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
        CITY = "Ahmedabad"
        API_KEY = "276b3203abf95b16dba5542e7744ed20"
        # upadting the URL
        URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
        # HTTP request
        response = requests.get(URL)
        # checking the status code of the request
        if response.status_code == 200:
        # getting data in the json format
            data = response.json()
        # getting the main dict block
            main = data['main']
        # getting temperature
            temperature = main['temp']
        # weather report
            report = data['weather']
            print(f"{CITY:-^30}")
            print(f"Temperature: {temperature}")#remaining to convert to degree celsuis
            print(f"Weather Report: {report[0]['description']}")
            talk(f"Temperature: {temperature}")
            talk(f"Weather Report: {report[0]['description']}")
        else:
        # showing the error message
            print("Error in the HTTP request")

#---------------------------------------LOCATION-------------------------------------------------

    elif "location" in query:
        g = geocoder.ip('me')
        lat=str(g.latlng[0])
        lng=str(g.latlng[1])
        s="https://www.google.com/maps/@"+lat+lng+"18z"
        webbrowser.open(s)

 #---------------------------------------Alarm-------------------------------------------------
    elif "alarm" in query:
        n=input("Enter the time of alarm:")
        alarmTime = n.split(":")
        HOUR = datetime.datetime.now().hour
        min = datetime.datetime.now().minute
        rem_hr=abs(int(alarmTime[0])-HOUR)
        rem_min=abs(int(alarmTime[1])-min)
        rem_sec=(rem_hr*60*60)+(rem_min*60)
        print(rem_sec)
        time.sleep(rem_sec)
        playsound.playsound()

    talk("What next?")
