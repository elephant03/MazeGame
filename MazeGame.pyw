# Imports all needed libaries
# Attepts to import pygame but as it isn't standered it is in a try statment
try:
    import pygame
except ImportError:
    print("Sorry you must have pygame installed to run this")
import json


# Sets constant varibles that will be used throught the program
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Will get these from the config file so they can be eaily edited
with open("config.json") as config:
    data = json.load(config)
    SCREEN_WIDTH = data["dimensions"]["width"]
    SCREEN_HEIGHT = data["dimensions"]["height"]

# Calculates the screen size based off the dimensions given in the config
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)


def Main():
    '''Starts the program and controls the game loop'''

    return


# Will only run the prgram if it is being directally called
if __name__ == "__main__":
    Main()
    raise SystemExit
