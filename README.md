# JARVIS-voice-assistant-system 
JARVIS is a Python-based voice assistant that can interact with the user through speech recognition,perform tasks like openin applications,searching on Google or wikipedia, playing music randomly, telling jokes,and having small talk. 

This project uses speech recognition and text-to-speech (TTS) to provide a hands-free assistant experience similar to Iron Man's JARVIS 

## 😁😀🛠 Features

- Greet the user according to the time of day (morning, afternoon, evening)

- Recognize voice commands using Google Speech Recognition

- Speak responses using pyttsx3

- Time & Date announcements

- Wikipedia search with spoken summary

- Open websites like Google, Facebook, YouTube

- Play random music from a specified folder

- Open system applications: Calculator, Notepad, CMD

- Open Calendar (Google Calendar via browser)

- Tell jokes and respond to basic small talk

- Exit gracefully with a voice command


## 💻 Requirements 

- Python 3.11 or higher 


## How to run? 

1. Create a virtual environment:

   ```bash
   conda create -n jarvis python=3.11 -y
   ```
1.1 virtual environment for D drives

  ```bash 
  conda create --prefix .\jarvis python=3.11 -y
  ``` 

1.2 for removing virtual environment 

  ```bash 
conda remove --prefix .\jarvis --all
  ```
1.3 for environment activation 

 ```bash
conda activate D:\inceptionBD\Assignments\JARVIS-voice-assistant-system\jarvis
 ```


2. Activate virtual environment:

   ```bash
   conda activate jarvis
   ```

3. Install required packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the JARVIS script:

   ```bash
   python jarvis.py
   ```

## 👨‍💻 Author

**Aman Ullah**

Inspired by Tony Stark's JARVIS


### 📜 License

This project is open-source and free to use for learning purposes.