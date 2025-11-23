import speech_recognition as sr 
import pyttsx3
import logging
import os
import datetime
import wikipedia
import webbrowser 
import random 
import subprocess 


 # logging configuration 
LOG_DIR = "logs" 
LOG_FILE_NAME = "application.log"

os.makedirs(LOG_DIR,exist_ok=True) 
log_path = os.path.join(LOG_DIR,LOG_FILE_NAME) 

logging.basicConfig(
    filename = log_path,
    format= "[%(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level= logging.INFO
) 

# Activating voice from our system 
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty('voice',voices[0].id) 

# This is speak function 
def speak(text):
    """ This function converts text to voice
    Args:
        text
    returns:
        voices
    """ 
    engine.say(text)
    engine.runAndWait()

speak("Hello My name is Aman")    