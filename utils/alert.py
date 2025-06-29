from playsound import playsound
import threading

def play_alert():
    threading.Thread(target=lambda: playsound("assets/alert.wav"), daemon=True).start()
# This function plays an alert sound in a separate thread to avoid blocking the main thread.
# It uses the playsound library to play the sound file "assets/alert.wav".      