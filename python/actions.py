import pyperclip
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
from pynput import mouse
import time
from http.server import HTTPServer, BaseHTTPRequestHandler

keyboard = KeyboardController()
mouse = MouseController()


def v_number():
    pyperclip.copy("awaaz version 0.1")

    keyboard.press(Key.ctrl_l)
    keyboard.press('v')
    keyboard.release('v')
    keyboard.release(Key.ctrl_l)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)


#def oprint(msg):
#    print("The latest message is " + msg)

def play_music(song):
        time.sleep(1)

        print(song)

        keyboard.press(Key.ctrl_l)
        keyboard.press('t')
        keyboard.release('t')
        keyboard.release(Key.ctrl_l)

        pyperclip.copy("!yt " + song)

        keyboard.press(Key.ctrl_l)
        keyboard.press('v')
        keyboard.release('v')
        keyboard.release(Key.ctrl_l)
        time.sleep(1)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

        time.sleep(10)

        mouse.position = (10, 20)
        mouse.press(Button.left)
        mouse.release(Button.left)

        time.sleep(5)

        keyboard.press(Key.ctrl_l)
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
        keyboard.release(Key.ctrl_l)

        time.sleep(1)

        pyperclip.copy("playing " + song)
        keyboard.press(Key.ctrl_l)
        keyboard.press('v')
        keyboard.release('v')
        keyboard.release(Key.ctrl_l)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
