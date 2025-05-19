# importing necessary modules and libraries of python
import time

import instadownloader
import instaloader
import pyttsx3  # text to speech conversion library in python
import datetime  # class to manipulate and store date and time
import speech_recognition as sr  # converts the spoken words to text
import wikipedia  # allows to search a self.query supplied as an argument
import webbrowser  # allows displaying web browsers
import os  # provides funtions to interact with operating system
import cv2  # provides interface for working with image and video processing functions
import requests  # allows you to send HTTP requests using python
import psutil  # python system and process utilities
import geocoder
import random
import pywhatkit as kit
from requests import get
import pyjokes
import pyautogui
import instadownloader as Instaloader
import PyPDF2
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


# function to convert text to speech
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# function to terminate TARS
def terminate_TARS():
    speak("See you soon sir! Have a great day.")
    exit()


# functon to play music
def play_random_music(music_dir):
    # List all files in the specified directory
    music_files = [f for f in os.listdir(music_dir) if os.path.isfile(os.path.join(music_dir, f))]

    # Filter out non-music files (you may need to adjust this based on your music file extensions)
    music_files = [f for f in music_files if f.endswith(('.mp3', '.wav', '.ogg', '.flac'))]

    if not music_files:
        print("No music files found in the directory.")
        return

    # Select a random music file
    random_music = random.choice(music_files)

    # Get the full path to the selected music file
    music_path = os.path.join(music_dir, random_music)

    # Open the music file using the default media player
    os.startfile(music_path)


# function to get current location
def get_current_location():
    location = geocoder.ip('me')
    return location.address


# function to make ECHO wish the operator
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir!")
    else:
        speak("Good Evening Sir!")

    speak("Hello, I am ECHO , Sir, your personal voice assistant. Please tell me how may i help you?")


# function to convert voice into text
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=5,phrase_time_limit=8)

    try:
        print("recognixing...")
        self.query = r.recognize_google(audio, language='en-in')
        print(f"User said: {self.query}\n")
    except Exception as e:
        print("Say That Again Please...")
        return "None"
    return self.query

def pdf_reader():
        book_path = 'C://Users//shrey//OneDrive//Documents//Turtles_All_the_Way_Down_by_John_Green.pdf'
        with open(book_path, 'rb') as book:
            pdf_reader = PyPDF2.PdfReader(book)
            total_pages = len(pdf_reader.pages)
            speak(f'Total number of pages in this book: {total_pages}')

            # Ask the user to specify the page number using voice input
            speak('Please tell me the page number I have to read')
            page_number = int(takeCommand())  # Assuming takeCommand() returns the spoken page number

            # Ensure the page number is within the valid range
            if 0 < page_number <= total_pages:
                page = pdf_reader.pages[page_number - 1]  # Adjust for 0-based indexing
                text = page.extract_text()
                speak(text)
            else:
                speak('Invalid page number. Please try again.')


# function to access webcam
def capture_webcam():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        cv2.imshow('Webcam', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()


# function to close web browser
def close_browser(browser_name):
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] == browser_name:
            proc.terminal()


# function to get current weather of a city using API
def get_weather_forecast(city):
    api_key = "158ebc6ecf9d2937e44d45fba71c568f"
    base_url = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + api_key
    try:
        response = requests.get(base_url)
        response.raise_for_status()  # Raise HTTPError for bad responses
        data = response.json()  # javascript object notation
        # Parse weather data and extract relevant information
        weather_description = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        temperature = (int)(temp - 273.15)
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        return weather_description, temperature, humidity, wind_speed
    except requests.exceptions.HTTPError as err:
        print(f"HTTP Error: {err}")
        speak("Sorry, there was a problem fetching the weather forecast.")
    except requests.exceptions.RequestException as err:
        print(f"Request Exception: {err}")
        speak("Sorry, there was an error in processing your request.")
    except KeyError as err:
        print(f"KeyError: {err}")
        speak("Sorry, the weather data received is incomplete or invalid.")
    return None, None, None, None


def speak_weather_forecast(city):
    weather_description, temperature, humidity, wind_speed = get_weather_forecast(city)
    speak(f"The weather in {city} is {weather_description}.")
    speak(f"The temperature is {temperature} degrees Celsius.")
    speak(f"The humidity is {humidity}%.")
    speak(f"The wind speed is {wind_speed} meters per second.")


def news():
    main_url = 'http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=348bf55f43a245f092b269795f5514d0'

    main_page = requests.get(main_url).json()
    articles = main_page["articles"]
    head = []
    day = ['first','second','third','fourth','fifth','sixth','seventh','eighth','ninth','tenth']
    for ar in articles:
        head.append(ar['title'])
    for i in range(len(day)):
        print(f" today's {day[i]} news is:",head[i])
        speak(f"today's {day[i]} news is: {head[i]}")

if __name__ == "__main__":

    wishMe()

    while True:
        # if 1:
        self.query = takeCommand().lower()

        # building logic for commands

        if 'wikipedia' in self.query:
            speak("Searching Wikipedia...")
            self.query = self.query.replace("wikipedia", "")
            results = wikipedia.summary(self.query, sentences=4)
            speak("According To Wikipedia")
            print(results)
            speak(results)

        # opening websites

        elif 'open youtube' in self.query:
            webbrowser.open("youtube.com")
            speak("opening youtube sir")

        elif 'open google' in self.query:
            speak("sir, what should i search?")
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")
            # speak("opening google sir")

        elif 'open wiki' in self.query:
            webbrowser.open("wikipedia.org")
            speak("opening wikipedia sir")

        elif 'open stack overflow' in self.query:
            webbrowser.open("stackoverflow.com")
            speak("opening stackoverflow sir")

        elif 'open chat gpt' in self.query:
            webbrowser.open("chatgpt.com")
            speak("opening chatgpt sir")
        elif 'open geeksforgeeks' in self.query:
            webbrowser.open("geeksforgeeks.com")
            speak("opening geeksforgeeks sir")

        elif 'open chrome' in self.query:
            webbrowser.open("chrome.com")
            speak("opening chrome sir")

        elif 'open github' in self.query:
            webbrowser.open("github.com")
            speak("opening github sir")

        elif 'open Java T Point' in self.query:
            webbrowser.open("javatpoint.com")
            speak("opening java t point sir")

        elif 'open reddit' in self.query:
            webbrowser.open("reddit.com")
            speak("opening reddit sir")

        elif 'open amazon' in self.query:
            webbrowser.open('amazon.in')
            speak("opening amazon sir")

        elif 'open LinkedIn' in self.query:
            webbrowser.open("https://www.linkedin.com/")
            speak("opening linked in sir")

        elif 'facebook' in self.query:
            webbrowser.open('facebook.com')
            speak('opening facebook sir')

        elif 'whatsApp web' in self.query:
            webbrowser.open("web.whatsapp.com")
            speak('opening whatsapp web sir')

        elif 'news' in self.query:
            webbrowser.open('news.google.com')
            speak('opening google news sir')

        # terminating websites
        elif 'close chrome' in self.query:
            speak('closing chrome')
            close_browser('chrome')

        elif 'close github' in self.query:
            speak('closing github')
            close_browser('github')

        # opening applications
        elif 'adobe acrobat' in self.query:
            codepath = "C:\\Program Files\\Adobe\\Acrobat DC\\Acrobat\\Acrobat.exe"
            os.startfile(codepath)

        elif 'open calendar' in self.query:
            os.system("start outlookcal:")

        # elif 'open notepad' in self.query:
        # os.system("start notepad")

        elif 'open command prompt' in self.query:
            os.system("start cmd")


        elif 'open downloads' in self.query:
            downloads_dir = 'C:\\Users\\shrey\\Downloads'
            down = os.listdir(downloads_dir)
            print(down)
            os.startfile(os.path.join(downloads_dir, down[0]))

        elif 'the current time' in self.query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'the current date' in self.query:
            strDate = datetime.datetime.now().strftime("%B %d, %Y")
            speak(f"The current date is {strDate}")

        elif 'open code' in self.query:
            codePath = "C:\\Users\\shrey\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'webcam' in self.query:
            speak('Opening Webcam Master')
            capture_webcam()

        elif 'shutdown' in self.query:
            speak("shutting down the laptop")
            os.system("shutdown /s /t 1")

        elif 'sleep the system' in self.query:
            speak('putting system to sleep')
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

        elif 'current weather' in self.query:
            speak("Please tell me the city for weather forecast")
            city = takeCommand()
            speak_weather_forecast(city)


        # playing music
        elif 'play music' in self.query:
            music_directory = 'C:\\Users\\shrey\\Music'
            play_random_music(music_directory)



        # terminating TARS
        elif 'thank you' in self.query or 'thankyou' in self.query:
            terminate_TARS()

        # accessing current location
        elif 'current location' in self.query:
            current_location = get_current_location()
            speak(f'your current location is {current_location}')

        # getting your ip address
        elif 'my ip address' in self.query:
            ip = get('https://api.ipify.org').text
            print(ip)
            speak(f"Your IP address is {ip}")

        # fetching news
        elif 'tell me news' in self.query:
            speak('Please Wait Sir, Fetching the latest news')
            news()

        # play song on youtube
        elif 'play song on youtube' in self.query:
            speak('Sir, which song would you like to enjoy at the moment?')
            cm = takeCommand().lower()
            kit.playonyt(f"{cm}")

        # switching between windows
        elif 'switch the window' in self.query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")


        # play video on youtube
        elif 'play video on youtube' in self.query:
            speak('Sir, which video would you like me to play?')
            cm = takeCommand().lower()
            kit.playonyt(f"{cm}")

        # to find a joke
        elif 'tell me a joke' in self.query:
            joke = pyjokes.get_joke()
            print(joke)
            speak(joke)

        # to check an instagram profile
        elif 'instagram profile' in self.query or 'profile on instagram' in self.query:
            speak('Sure, please provide the username of the profile.')
            username = input("Enter username here:")

            if username:
                try:
                    profile_url = f'https://www.instagram.com/{username}/'
                    response = requests.get(profile_url)
                    if response.status_code == 200:
                        speak(f'Here is the profile of the user {username}')
                        webbrowser.open(profile_url)
                        time.sleep(5)
                        speak('Would you like to download the profile picture of this account?')
                        condition = takeCommand().lower()
                        print(condition)
                        if 'yes please' in condition or 'yeah' in condition or 'do it' in condition:
                            mod = instaloader.Instaloader()
                            mod.download_profile(username, profile_pic_only=True)
                            speak("The profile picture has been saved in our main folder.")
                        else:
                            speak("Okay, I won't download the profile picture.")
                    else:
                        speak('Sorry, the profile does not exist. Please enter a valid username.')
                except Exception as e:
                    speak('Sorry, I encountered an error while fetching the profile. Please try again later.')
                    print(e)
            else:
                speak('Sorry, I didn\'t catch the username. Please try again.')

        elif 'take screenshot' in self.query or 'take a screenshot' in self.query:
            speak("Sure, please tell me the name for the screenshot file")
            name = takeCommand().lower()

            if name:
                try:
                    speak("Please hold the screen for a few seconds, I am taking the screenshot")
                    time.sleep(3)
                    img = pyautogui.screenshot()
                    img.save(f"{name}.png")
                    speak("I have taken the screenshot and saved it in our main folder.")
                except Exception as e:
                    speak("Sorry, I encountered an error while taking the screenshot. Please try again later.")
                    print(e)
            else:
                speak("Sorry, I didn't catch the file name. Please try again.")

        elif 'read pdf' in self.query or 'read PDF' in self.query:
            pdf_reader()






       # speak('Sir, do you have any other work?')

