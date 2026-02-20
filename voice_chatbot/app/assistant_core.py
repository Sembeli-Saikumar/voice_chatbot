from app.chatbot import get_response
from app.speech import listen
from app.tts import speak
import os
import webbrowser
import datetime
import random
import pyautogui

speak("Voice assistant activated")

while True:
    text = listen()
    if not text:
        continue

    text = text.lower()
    print("You:", text)

    # -------------------------
    # OPEN APPLICATIONS
    # -------------------------
    if "chrome" in text:
        speak("Opening Google Chrome")
        os.system("start chrome")
        continue

    elif "youtube" in text:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
        continue

    elif "google" in text and "search" not in text:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
        continue

    elif "file explorer" in text:
        speak("Opening File Explorer")
        os.system("explorer")
        continue

    elif "notepad" in text:
        speak("Opening Notepad")
        os.system("start notepad")
        continue

    elif "calculator" in text:
        speak("Opening Calculator")
        os.system("start calc")
        continue

    # -------------------------
    # TIME & DATE
    # -------------------------
    elif "time" in text:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}")
        continue

    elif "date" in text:
        today = datetime.datetime.now().strftime("%d %B %Y")
        speak(f"Today's date is {today}")
        continue

    # -------------------------
    # GOOGLE SEARCH
    # -------------------------
    elif "search" in text:
        speak("What should I search?")
        query = listen()
        if query:
            webbrowser.open(f"https://www.google.com/search?q={query}")
            speak("Here are the search results")
        continue

    # -------------------------
    # PLAY MUSIC
    # -------------------------
    elif "play music" in text:
        speak("Playing music")
        os.startfile("C:\\Users\\Admin\\Music")  # change if needed
        continue

    # -------------------------
    # JOKES
    # -------------------------
    elif "joke" in text:
        jokes = [
            "Why do programmers hate nature? Too many bugs.",
            "Why was the computer cold? Because it left its Windows open.",
            "Why did the computer go to the doctor? It caught a virus."
        ]
        speak(random.choice(jokes))
        continue

    # -------------------------
    # SCREENSHOT
    # -------------------------
    elif "screenshot" in text or "screen shot" in text:
        speak("Taking screenshot")
        screenshot = pyautogui.screenshot()
        screenshot.save("screenshot.png")
        speak("Screenshot saved")
        continue

    # -------------------------
    # LOCK SCREEN
    # -------------------------
    elif "lock screen" in text:
        speak("Locking the system")
        os.system("rundll32.exe user32.dll,LockWorkStation")
        continue

    # -------------------------
    # SHUTDOWN
    # -------------------------
    elif "shutdown" in text:
        speak("Are you sure you want to shut down?")
        confirm = listen()
        if confirm and "yes" in confirm.lower():
            speak("Shutting down the system")
            os.system("shutdown /s /t 5")
            break
        else:
            speak("Shutdown cancelled")
        continue

    # -------------------------
    # RESTART
    # -------------------------
    elif "restart" in text:
        speak("Are you sure you want to restart?")
        confirm = listen()
        if confirm and "yes" in confirm.lower():
            speak("Restarting system")
            os.system("shutdown /r /t 5")
            break
        else:
            speak("Restart cancelled")
        continue

    # -------------------------
    # EXIT ASSISTANT
    # -------------------------
    elif "exit" in text or "bye" in text:
        speak("Goodbye. Have a nice day.")
        break

    # -------------------------
    # DEFAULT CHATBOT RESPONSE
    # -------------------------
    else:
        response = get_response(text)
        print("Bot:", response)
        speak(response)
