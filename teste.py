import pyautogui as pyau
import time
import cv2
import os

while True:
    try:
        email = pyau.locateOnScreen("images\\email.png", confidence=0.8)
        if email:
            pyau.click(email)
            break
    except Exception as e:
        pass
    time.sleep(1)