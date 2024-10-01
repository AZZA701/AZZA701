
def show_media(media_type):
    if media_type == "image":
        images = [img for img in os.listdir() if img.endswith(".png")]
        for img in images:
            img_window = tk.Toplevel()
            img_display = Image.open(img)
            img_display.show()
            speak(f"Showing image: {img}")
            time.sleep(2)

    elif media_type == "video":
        videos = [vid for vid in os.listdir() if vid.endswith(".avi")]
        for vid in videos:
            os.startfile(vid)
            speak(f"Playing video: {vid}")
            time.sleep(5)

def set_reminder(task, time_str):
    speak(f"Reminder set for {task} at {time_str}.")

def perform_calculation(expression):
    try:
        result = eval(expression)
        speak(f"The result is {result}.")
    except Exception:
        speak("Error in calculation.")

def main():
    speak("Welcome! I am your voice assistant. How can I assist you today?")
    
    while True:
        command = listen()
        
        if "open camera" in command:
            open_camera()
        elif "show images" in command:
            show_media("image")
        elif "show videos" in command:
            show_media("video")
        elif "set reminder" in command:
            task = input("Please enter the task: ")
            time_str = input("Please enter the time (e.g., 10:30): ")
            set_reminder(task, time_str)
        elif "calculate" in command:
            expression = input("Please enter the expression: ")
            perform_calculation(expression)
        elif "close the application" in command:
            speak("Closing the application. Goodbye!")
            break

def start_assistant():
    Thread(target=main).start()

# إنشاء واجهة المستخدم
root = tk.Tk()
root.title("Voice Assistant")
root.geometry("300x200")
root.configure(bg='white')

# أيقونة الميكروفون
mic_icon = PhotoImage(file='mic_icon.png')  # تأكد من وجود ملف صورة الميكروفون
mic_button = tk.Button(root, image=mic_icon, bg='white', command=start_assistant)
mic_button.pack(pady=20)

# بدء الواجهة
root.mainloop()
