import pyperclip
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
from pynput import mouse
import time
from http.server import HTTPServer, BaseHTTPRequestHandler

keyboard = KeyboardController()
mouse = MouseController()


# variables for mouse corrdinates

joinCallX = -1072
joinCallY = 539

txtFieldX = -1456
txtFieldY = 987

yt1ThumbX = 515
yt1ThumbY = 327


# metadata variables

versionNumb = "0.3.0"


def v_number():
    pyperclip.copy("awaaz version " + versionNumb)

    keyboard.press(Key.ctrl_l)
    keyboard.press('v')
    keyboard.release('v')
    keyboard.release(Key.ctrl_l)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)


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

    mouse.position = (yt1ThumbX, yt1ThumbY) # move to the location of the first thumbnail on YT search page
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


def spam():
    pyperclip.copy("SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! ")
    keyboard.press(Key.ctrl_l)
    keyboard.press('v')
    keyboard.release('v')
    keyboard.release(Key.ctrl_l)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

def antifbi():
    pyperclip.copy("In case of an investigation by a federal or local authority, I do not include myself in any groups mentioned or condone any of the actions or language used in this establishment. I am simply a third-party bystander.")
    keyboard.press(Key.ctrl_l)
    keyboard.press('v')
    keyboard.release('v')
    keyboard.release(Key.ctrl_l)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

def join_call():
    mouse.position = (joinCallX, joinCallY)
    mouse.press(Button.left)
    mouse.release(Button.left)
    mouse.position = (txtFieldX, txtFieldY)
    mouse.press(Button.left)
    mouse.release(Button.left)
