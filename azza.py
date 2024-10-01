import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
import speech_recognition as sr
import pyttsx3
import threading
import time
import os
import subprocess

class VoiceAssistantApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        self.label = Label(text='Welcome to the Voice Assistant!', font_size='20sp')
        self.layout.add_widget(self.label)

        self.btn = Button(text='Listen for Commands', on_press=self.listen)
        self.layout.add_widget(self.btn)

        self.reminders = []
        self.is_running = True
        return self.layout

    def speak(self, text):
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()

    def listen(self, instance):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            self.label.text = "Please say a command now."
            audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio, language='en-US')
            self.label.text = f"You said: {command}"
            self.execute_command(command)
        except sr.UnknownValueError:
            self.label.text = "I couldn't understand what you said."
        except sr.RequestError as e:
            self.label.text = f"An error occurred: {e}"

    def execute_command(self, command):
        if 'open website' in command:
            site_name = command.replace('open website', '').strip()
            os.system(f"start {site_name}")
            self.speak(f"Opened website: {site_name}")

        elif 'close website' in command:
            site_name = command.replace('close website', '').strip()
            # Implement website closing based on your OS
            self.speak(f"Closed website: {site_name}")

        elif 'open app' in command:
            app_name = command.replace('open app', '').strip()
            os.system(f"start {app_name}")
            self.speak(f"Opened app: {app_name}")

        elif 'close app' in command:
            app_name = command.replace('close app', '').strip()
            # Implement app closing based on your OS
            self.speak(f"Closed app: {app_name}")

        elif 'reminder' in command:
            reminder_text = command.replace('reminder', '').strip()
            self.reminders.append(reminder_text)
            self.speak(f"Added reminder: {reminder_text}")

        elif 'show reminders' in command:
            if self.reminders:
                reminders_list = ", ".join(self.reminders)
                self.speak(f"Your reminders are: {reminders_list}")
            else:
                self.speak("You have no reminders.")

        elif 'wake me up' in command:
            self.speak("Get ready to wake up! I will remind you in one minute.")
            threading.Thread(target=self.remind_user).start()

        elif 'stop' in command:
            self.is_running = False
            self.speak("Voice assistant stopped.")

        # Bluetooth Control
        elif 'turn on bluetooth' in command:
            os.system("start ms-settings:bluetooth")
            self.speak("Bluetooth turned on.")

        elif 'turn off bluetooth' in command:
            # Implement Bluetooth off based on your OS
            self.speak("Bluetooth turned off.")

        # Wi-Fi Control
        elif 'turn on wifi' in command:
            os.system("start ms-settings:wifi")
            self.speak("Wi-Fi turned on.")

        elif 'turn off wifi' in command:
            # Implement Wi-Fi off based on your OS
            self.speak("Wi-Fi turned off.")

        # Airplane Mode Control
        elif 'turn on airplane mode' in command:
            # Implement Airplane mode on based on your OS
            self.speak("Airplane mode turned on.")

        elif 'turn off airplane mode' in command:
            # Implement Airplane mode off based on your OS
            self.speak("Airplane mode turned off.")

        # Eye Mode Control
        elif 'eye mode' in command:
            # Implement Eye mode control (if applicable)
            self.speak("Eye mode activated.")

        # Perform Math Operations
        elif 'calculate' in command:
            operation = command.replace('calculate', '').strip()
            result = self.perform_calculation(operation)
            self.speak(f"The result is {result}")

    def perform_calculation(self, operation):
        try:
            # Using eval for simplicity, but this is generally not safe
            return eval(operation)
        except Exception as e:
            return f"Error in calculation: {e}"

    def remind_user(self):
        self.is_running = True
        while self.is_running:
            time.sleep(60)  # Remind every minute
            self.speak("This is a reminder! Time to do something important.")

if __name__ == '__main__':
    VoiceAssistantApp().run()
