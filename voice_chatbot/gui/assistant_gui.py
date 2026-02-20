import tkinter as tk
from tkinter import scrolledtext
from PIL import Image, ImageTk
import threading
import os
import datetime
import random
import pyautogui

from app.speech import listen
from app.tts import speak
from app.chatbot import get_response


# -------------------------
# ASSISTANT LOGIC
# -------------------------
def run_assistant():
    update_status("Listening...", "#00ffcc")
    speak("Voice assistant activated")
    add_message("Assistant", "Voice assistant activated")

    while True:
        text = listen()
        if not text:
            continue

        text = text.lower()
        add_message("You", text)

        if "chrome" in text:
            speak("Opening Chrome")
            os.system("start chrome")
            add_message("Assistant", "Opening Chrome")

        elif "time" in text:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The time is {current_time}")
            add_message("Assistant", f"The time is {current_time}")

        elif "exit" in text or "bye" in text:
            speak("Goodbye")
            add_message("Assistant", "Goodbye")
            break

        else:
            response = get_response(text)
            speak(response)
            add_message("Assistant", response)

    update_status("Stopped", "red")


def start_assistant():
    threading.Thread(target=run_assistant).start()


def add_message(sender, message):
    chat_box.config(state=tk.NORMAL)

    if sender == "You":
        chat_box.insert(tk.END, f"\n🧑 You: {message}\n", "user")
    else:
        chat_box.insert(tk.END, f"\n🤖 Assistant: {message}\n", "bot")

    chat_box.config(state=tk.DISABLED)
    chat_box.see(tk.END)


def update_status(text, color):
    status_label.config(text=f"Status: {text}", fg=color)


# -------------------------
# GUI DESIGN
# -------------------------
root = tk.Tk()
root.title("AI Voice Assistant")
root.geometry("950x600")
root.configure(bg="#0f0f0f")

# TOP TITLE
title = tk.Label(
    root,
    text="🤖 AI Voice Assistant",
    font=("Segoe UI", 24, "bold"),
    fg="#00ffcc",
    bg="#0f0f0f"
)
title.pack(pady=10)

subtitle = tk.Label(
    root,
    text="Intelligent Voice Assistant using Machine Learning & NLP",
    font=("Segoe UI", 11),
    fg="gray",
    bg="#0f0f0f"
)
subtitle.pack()

status_label = tk.Label(
    root,
    text="Status: Idle",
    font=("Segoe UI", 12),
    fg="gray",
    bg="#0f0f0f"
)
status_label.pack(pady=5)

# MAIN FRAME (LEFT + RIGHT SPLIT)
main_frame = tk.Frame(root, bg="#0f0f0f")
main_frame.pack(fill="both", expand=True, padx=20, pady=10)

# LEFT CHAT SECTION
chat_frame = tk.Frame(main_frame, bg="#1a1a1a")
chat_frame.pack(side="left", fill="both", expand=True, padx=10)

chat_box = scrolledtext.ScrolledText(
    chat_frame,
    wrap=tk.WORD,
    font=("Segoe UI", 11),
    bg="#1a1a1a",
    fg="white",
    insertbackground="white",
    bd=0,
    padx=10,
    pady=10
)
chat_box.pack(fill="both", expand=True)
chat_box.config(state=tk.DISABLED)

chat_box.tag_config("user", foreground="#00ffff")
chat_box.tag_config("bot", foreground="#00ff99")

# RIGHT IMAGE SECTION
image_frame = tk.Frame(main_frame, bg="#0f0f0f")
image_frame.pack(side="right", padx=20)

try:
    img = Image.open("ai_image.png")
    img = img.resize((250, 250))
    img = ImageTk.PhotoImage(img)

    image_label = tk.Label(image_frame, image=img, bg="#0f0f0f")
    image_label.pack(pady=20)
except:
    placeholder = tk.Label(
        image_frame,
        text="AI SYSTEM ACTIVE",
        font=("Segoe UI", 16, "bold"),
        fg="#00ffcc",
        bg="#0f0f0f"
    )
    placeholder.pack(pady=50)

# BUTTON SECTION
button_frame = tk.Frame(root, bg="#0f0f0f")
button_frame.pack(pady=15)

start_btn = tk.Button(
    button_frame,
    text="🎤 Start Listening",
    font=("Segoe UI", 14, "bold"),
    bg="#00ff99",
    fg="black",
    width=18,
    command=start_assistant
)
start_btn.grid(row=0, column=0, padx=20)

exit_btn = tk.Button(
    button_frame,
    text="❌ Exit",
    font=("Segoe UI", 14, "bold"),
    bg="#ff4d4d",
    fg="white",
    width=12,
    command=root.destroy
)
exit_btn.grid(row=0, column=1, padx=20)

root.mainloop()
