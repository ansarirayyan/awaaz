
from pynput.mouse import Button, Controller
from pynput import mouse

mouse = Controller()

print('The current pointer position is {0}'.format(
    mouse.position))


# variables for mouse corrdinates are in main.py
