#importing necessary libraries
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import smtplib

  #initializing the voice engine 
engine = pyttsx3.init('sapi5') 

  #setting the voice rate 
rate = engine.getProperty('rate')   # getting details of current speaking rate 
engine.setProperty('rate', 150)     # setting up new voice rate

  #getting the voices available in the system 
voices = engine.getProperty('voices')       #getting details of current voice 

  #changing index, changes voices. 1 for female and 0 for male  
engine.setProperty('voice', voices[1].id)  

    #function to speak text through the system's speaker  
def speak(text):  
    engine.say(text)  
    engine.runAndWait()  

    #function to wish according to time of day  
def wishMe():  

    hour = int(datetime.datetime.now().hour)  

    if hour>=0 and hour<12:  
        speak("Good Morning!")  

    elif hour>=12 and hour<18:  
        speak("Good Afternoon!")   

    else:  
        speak("Good Evening!")  

    speak("I am badge your assistant, How may I help you?")      

     #function to take command from user using microphone    
def takeCommand():     

     r = sr.Recognizer()                                                                                   

     with sr.Microphone() as source:                                                                       

         print("Listening...")  
          #waiting for user input through microphone     
          r.pause_threshold = 1     
          r.adjust_for_ambient_noise(source, duration=1)    
          audio = r.listen(source)     
          try:          print("Recognizing...")         
            query = r.recognize_google(audio, language='en-in')        
            print(f"User said: {query}\n")     
            except Exception as e:         
              print("Say that again please...")        
              return "None"     
            return query    
          def sendEmail(to, content):    
            server = smtplib.SMTP('smtp.gmail.com', 587)        
            server.ehlo()         
            server.starttls()          
            server.login('youremail@gmail.com', 'your-password')         
            server
