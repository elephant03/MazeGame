# Imports all needed libaries
# Attepts to import pygame but as it isn't standered it is in a try statment
try:
    import pygame
except ImportError:
    print("Sorry you must have pygame installed to run this")
import json
import tkinter


# Sets constant varibles that will be used throught the program
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Will get these from the config file so they can be eaily edited
with open("config.json") as config:
    data = json.load(config)
    # pygame varables
    pygame_data = data["pygame"]

    SCREEN_WIDTH = pygame_data["dimensions"]["width"]
    SCREEN_HEIGHT = pygame_data["dimensions"]["height"]

    # tkinter varables
    tkinter_data = data["tkinter"]

    BACKGROUND = tkinter_data["background"]
    FOREGROUND = tkinter_data["foreground"]
    BTN_BACKGROUND = tkinter_data["btn_background"]
    BTN_ACTIVE = tkinter_data["btn_activebackground"]
    QUIT_BTN_BACKGROUND = tkinter_data["quitbtn_background"]
    QUIT_BTN_ACTIVE = tkinter_data["quitbtn_activebackground"]
    POSITIVE_BTN_BACKGROUND = tkinter_data["positivebtn_background"]
    POSITIVE_BTN_ACTIVE = tkinter_data["positivebtn_activebackground"]
    BTN_FOREGROUND = tkinter_data["btn_foreground"]
    BTN_ACTIVEFOREGROUND = tkinter_data["btn_activeforeground"]
    FONT_FAMILY = tkinter_data["font"]
    FONT_SIZE = tkinter_data["font_size"]
    TITLE_FONT_SIZE = tkinter_data["title_font_size"]

    FONT = (FONT_FAMILY, FONT_SIZE)
    TITLE_FONT = (FONT_FAMILY, TITLE_FONT_SIZE)

    # Game varables
    game_data = data["game"]

    dificulty = game_data["difficulty"]


# Calculates the screen size based off the dimensions given in the config
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)


def StartMenu():
    '''Starts the program and opens the start menu'''
    root = tkinter.Tk()

    root.title("Maze Game")
    root.config(bg=BACKGROUND)
    root.wm_iconbitmap("Libary/Images/MazeIcon.ico")

    start_fr = tkinter.Frame(root, bg=BACKGROUND)
    start_fr.pack(fill=tkinter.BOTH, expand=True)

    title_lbl = tkinter.Label(start_fr, bg=BACKGROUND, fg=FOREGROUND,
                              font=TITLE_FONT, text="Wellcome to...\nThe Maze")
    title_lbl.grid(row=0, column=0, sticky="nsew",
                   padx=2, pady=2, columnspan=2)

    space_lbl = tkinter.Label(
        start_fr, bg=BACKGROUND, fg=FOREGROUND, font=FONT)
    space_lbl.grid(row=1, column=0, sticky="nsew",
                   padx=2, pady=2, columnspan=2)

    dificulty_lbl = tkinter.Label(
        start_fr, bg=BACKGROUND, fg=FOREGROUND, font=FONT, text="Dificulty: ")
    dificulty_lbl.grid(row=2, column=0, sticky="nsew", padx=2, pady=2)

    StrVar = tkinter.StringVar(start_fr)
    StrVar.set(dificulty)

    difficulty_dd = tkinter.OptionMenu(
        start_fr, StrVar, "Easy", "Normal", "Hard", "Mega")
    difficulty_dd.config(bg=BACKGROUND, foreground=FOREGROUND,
                         font=FONT, activebackground=BACKGROUND)
    difficulty_dd["menu"].config(
        bg=BACKGROUND, foreground=FOREGROUND, font=FONT, activebackground=BACKGROUND)
    difficulty_dd["highlightthickness"] = 0
    difficulty_dd.grid(
        row=2, column=1, padx=2, pady=2, sticky="nsew")

    quit_btn = tkinter.Button(start_fr, bg=QUIT_BTN_BACKGROUND, activebackground=QUIT_BTN_ACTIVE,
                              fg=BTN_FOREGROUND, activeforeground=BTN_ACTIVEFOREGROUND, font=FONT,
                              text="QUIT", command=lambda: [root.destroy(), quit()])
    quit_btn.grid(row=3, column=0, padx=2, pady=2, sticky="nsew")

    play_btn = tkinter.Button(start_fr, bg=POSITIVE_BTN_BACKGROUND, activebackground=POSITIVE_BTN_ACTIVE, fg=BTN_FOREGROUND,
                              activeforeground=BTN_FOREGROUND, font=FONT, text="Play!", command=lambda: [root.destroy(), play()])
    play_btn.grid(row=3, column=1, sticky="nsew", pady=2, padx=2)

    Align_Grid(root)
    Align_Grid(start_fr)

    root.mainloop()

    return


def Align_Grid(Frame):
    '''Adds weight to all of the slaves of Frame in a tkinter grid'''
    # Gets the nuber of rows and columns of the grid
    Grid_Size = Frame.grid_size()

    # Loops through every column
    for i in range(Grid_Size[0]):
        # Sets the weight to a non zero value so it can expand
        Frame.columnconfigure(i, weight=1)
    # Loops through every row
    for i in range(Grid_Size[1]):
        # Sets the weight to a non zero value so it can expand
        Frame.rowconfigure(i, weight=1)


def play():
    '''Opens the game window and controls the game loop'''
    return


# Will only run the prgram if it is being directally called
if __name__ == "__main__":
    StartMenu()
    raise SystemExit
