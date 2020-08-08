#!/usr/bin/env python3

from keypress import wait_input
from pynput.mouse import Button, Controller
from time import sleep
import argparse

def getArgs():
    args = argparse.ArgumentParser()

    args.add_argument("-t", "--times",
    type=int, default=10,  help="times button is pressed")

    args.add_argument("-w", "--wait",
    help="waits until chosen key is pressed to start clicking default='c'",
    default="c")

    args.add_argument("-U", "--unlimited", action="count",
    help="don't stop cliking until the cursor is moved")

    return args.parse_args()

def main():
    args = getArgs()
    m = Controller()

    if args.wait:
       wait_input(args.wait)

    # quits if cursor has moved
    i = 0
    position = m.position
    while i < args.times and m.position == position:
        m.click(Button.left)
        sleep(0.01)
        if not args.unlimited:
            i += 1

if __name__ == "__main__":
    main()
