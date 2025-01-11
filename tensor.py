import pyttsx3
import speech_recognition as sr
import wikipedia
import datetime
import webbrowser
import os
import tkinter as tk
from tkinter import messagebox

# Initialize the speech engine
engine = pyttsx3.init()

# Function to speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen to user input
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        text_output.insert(tk.END, "Listening...\n")
        speak("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio).lower()
            text_output.insert(tk.END, f"You said: {command}\n")
        except sr.UnknownValueError:
            text_output.insert(tk.END, "Sorry, I could not understand the audio.\n")
            speak("Sorry, I could not understand the audio.")
            return None
        except sr.RequestError:
            text_output.insert(tk.END, "Could not request results from Google.\n")
            speak("Could not request results from Google.")
            return None
    return command

# Function to perform the task based on command
def perform_task(command):
    if 'hello' in command:
        speak("Hello! How can I assist you today?")
        text_output.insert(tk.END, "Hello! How can I assist you today?\n")
    
    elif 'time' in command:
        time = datetime.datetime.now().strftime("%H:%M")
        speak(f"The current time is {time}.")
        text_output.insert(tk.END, f"The current time is {time}.\n")
    
    elif 'date' in command:
        date = datetime.datetime.now().strftime("%B %d, %Y")
        speak(f"Today's date is {date}.")
        text_output.insert(tk.END, f"Today's date is {date}.\n")
    
    elif 'wikipedia' in command:
        speak("What would you like to know?")
        text_output.insert(tk.END, "What would you like to know?\n")
        topic = listen()
        if topic:
            try:
                info = wikipedia.summary(topic, sentences=1)
                speak(info)
                text_output.insert(tk.END, f"Info from Wikipedia: {info}\n")
            except wikipedia.exceptions.DisambiguationError as e:
                speak("There are multiple topics for that search. Please be more specific.")
                text_output.insert(tk.END, "There are multiple topics for that search. Please be more specific.\n")
            except wikipedia.exceptions.HTTPTimeoutError:
                speak("Sorry, I couldn't fetch the information.")
                text_output.insert(tk.END, "Sorry, I couldn't fetch the information.\n")
    
    elif 'open' in command:
        if 'google' in command:
            webbrowser.open("https://www.google.com")
            speak("Opening Google.")
            text_output.insert(tk.END, "Opening Google...\n")
        elif 'youtube' in command:
            webbrowser.open("https://www.youtube.com")
            speak("Opening YouTube.")
            text_output.insert(tk.END, "Opening YouTube...\n")
        else:
            speak("Sorry, I didn't understand which website to open.")
            text_output.insert(tk.END, "Sorry, I didn't understand which website to open.\n")
    
    elif 'play music' in command:
        music_folder = "C:\\Users\\YourUsername\\Music"  # Adjust the path as needed
        songs = os.listdir(music_folder)
        if songs:
            os.startfile(os.path.join(music_folder, songs[0]))
            speak("Playing music.")
            text_output.insert(tk.END, "Playing music...\n")
        else:
            speak("I couldn't find any music files.")
            text_output.insert(tk.END, "I couldn't find any music files.\n")
    
    elif 'exit' in command:
        speak("Goodbye!")
        text_output.insert(tk.END, "Goodbye!\n")
        window.quit()

# Function to handle button click to listen
def on_listen_click():
    command = listen()
    if command:
        perform_task(command)

# Initialize main window
window = tk.Tk()
window.title("Jarvis AI Assistant")
window.geometry("500x500")

# Add widgets
greeting_label = tk.Label(window, text="Welcome to Jarvis AI!", font=("Arial", 14))
greeting_label.pack(pady=10)

text_output = tk.Text(window, height=15, width=50)
text_output.pack(pady=10)

listen_button = tk.Button(window, text="Listen", command=on_listen_click, font=("Arial", 12), bg="blue", fg="white")
listen_button.pack(pady=10)

exit_button = tk.Button(window, text="Exit", command=window.quit, font=("Arial", 12), bg="red", fg="white")
exit_button.pack(pady=10)

# Start the Tkinter event loop
window.mainloop()
