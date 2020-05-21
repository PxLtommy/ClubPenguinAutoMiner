import time
import keyboard
import autopy
from pynput.mouse import Button , Controller
import os

mouse = Controller()

print("Don't make your mine spots too far apart")
print(' ')
print('Put your mouse in the spot you want to mine')
print('Saving spot #1 in 3 seconds...')
time.sleep(3)
pos_one = mouse.position
print('Saved #1')

os.system("cls")

print('Put your mouse in the spot you want to mine')
print(' ')
print('Saving spot #2 in 3 seconds...')
time.sleep(3)
pos_two = mouse.position
print('Saved #2')

os.system("cls")

print('Put your mouse in the spot you want to mine')
print(' ')
print('Saving spot #3 in 3 seconds...')
time.sleep(3)
pos_three = mouse.position
print('Saved #3')
time.sleep(1)

os.system("cls")
print('Starting...')

def run():
    time.sleep(10)
    global mouse
    mouse.position = pos_one
    time.sleep(1)
    mouse.click(Button.left,1)
    time.sleep(3)
    keyboard.press_and_release('d')

    time.sleep(10)
    mouse.position = pos_two
    time.sleep(1)
    mouse.click(Button.left,1)
    time.sleep(3)
    keyboard.press_and_release('d')

    time.sleep(10)
    mouse.position = pos_three
    time.sleep(1)
    mouse.click(Button.left,1)
    time.sleep(3)
    keyboard.press_and_release('d')

while True:
    run()