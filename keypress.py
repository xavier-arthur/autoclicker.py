##!/usr/bin/env python3

from pynput import keyboard

def on_press(key):
    try:
        if key == keyboard.KeyCode.from_char(target):
            return False
    except:
        pass

def listen():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

def set_target(trgt):
    #target : string
    global target
    target = trgt
