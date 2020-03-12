from selenium import webdriver
import pyttsx3
import speech_recognition as sr
import wikipedia
import datetime
import webbrowser
import os
import time

engine = pyttsx3.init('nsss')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")
    else:
        speak("Welcome back")
    speak("How may I help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f'You: {query}')
    except Exception as e:
        print(e)
        print("Sorry, say that again...")
        return "None"

    return query

if __name__ == "__main__":

    wishMe()
    info = """***************************************
    command:
        * What is ____? (Wikipedia)
        * Search ____?  (Google)
        * Open Udemy
        * Open Amazon
        * Show map of ____?
        * Open my repository (Github)
***************************************"""

    print(info)
    time.sleep(5)
    ask = True
    while ask:
        query = takeCommand().lower()

        if 'what' in query:
            speak("Searching in Wikipedia")
            query = query.split()[2:]
            query = " ".join(query)
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'search' in query:
            driver = webdriver.Chrome('/Users/hachimannoboruju/Documents/Python/Project/Selenium/chromedriver')
            speak("Searching on Google")
            query = query.split()[1:]
            query = " ".join(query)
            driver.get("https://www.google.com")
            google_search = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
            google_search.send_keys(query)
            google_search.submit()

        elif 'open udemy' in query:
            webbrowser.open("https://www.udemy.com")

        elif 'open amazon' in query:
            webbrowser.open("https://www.amazon.com")

        elif 'show map' in query:
            driver = webdriver.Chrome('/Users/hachimannoboruju/Documents/Python/Project/Selenium/chromedriver')
            query = query.split()[3:]
            query = " ".join(query)
            speak("Searching " + query)
            driver.get("https://www.google.com/maps/@38.8285395,-94.4902875,15z")
            map_search = driver.find_element_by_xpath('//*[@id="searchboxinput"]')
            map_search.send_keys(query)
            driver.find_element_by_xpath('//*[@id="searchbox-searchbutton"]').click()

        elif 'open my repository' in query:
            speak("Type your email")
            EMAIL = str(input("Type your Email Address: "))
            speak("Type your password")
            PASSWORD = str(input("Type your password: "))
            driver = webdriver.Chrome('/Users/hachimannoboruju/Documents/Python/Project/Selenium/chromedriver')
            driver.get('https://github.com/login')
            driver.find_element_by_xpath('//*[@id="login_field"]').send_keys(EMAIL)
            driver.find_element_by_xpath('//*[@id="password"]').send_keys(PASSWORD)
            driver.find_element_by_xpath('/html/body/div[3]/main/div/form/div[4]/input[9]').click()

        elif 'open khan academy' in query:
            speak("Studying will enrich your life")
            speak("Type your Username: ")
            USERNAME = str(input("Type your Username: "))
            speak("Type your Password")
            KPASSWORD = str(input("Type your Password: "))
            driver = webdriver.Chrome('/Users/hachimannoboruju/Documents/Python/Project/Selenium/chromedriver')
            driver.get("https://www.khanacademy.org/login?continue=%2F")
            driver.find_element_by_xpath('//*[@id="uid-identity-text-field-0-email-or-username"]').send_keys(USERNAME)
            driver.find_element_by_xpath('//*[@id="uid-identity-text-field-1-password"]').send_keys(KPASSWORD)
            driver.find_element_by_xpath('//*[@id="login-signup-root"]/div/div[3]/section[2]/div/div/div[2]/button').click()


        time.sleep(5)

