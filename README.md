# final-project
1) For my final project, I'm going to create a dice roller program. It will be a six sided dice that randomly selects a number to roll. I'm going to try to make it so the dice actually rolls rather than just pick a random number.
2A) The first function will make the dice roll
2B) The second function will pick a random number
2C) The third function will keep the dice rolling

2) Overtime, I have decided to opt out of the dice roll. I would rather do an escape room game that allows you to exit the room with a code that you find through puzzles and hints. I need my functions to create a room to start the game, create puzzles that allows the player to figure out 1 number for the either four or six digit code, create hints and limit them to three.

My program will be a game that provides puzzles to solve in order to get numbers for a code, so they can exit the room. This game is for pure entertainment, but it's also a brain game that allows people to think outside the box.
  I will need to create a main funtion that starts the game, display function that displays the room that is for solving the puzzles and finding the numbers, and I need a puzzle function that makes the puzzles needed to solve the code. I will also need a display function for when the player wins. 
  Someone will use my program to play a game for entertainment or to exercise their brain. It's for players who like puzzles and escape rooms.
  I can use tkinter or pygame to import the images for the escape room and puzzles. The format would be JSON, mostly strings and integers being used, there is one field that must be ordered which is the code
  There will be many if/while loops and inputs
  





import pygame
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog


class Window:
    def __init__(self):

    def setup_gui(self):
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(padx=10, pady=10)

print("Hi player")

print("what's your name?")
name = input("> ")

if name:
    print(f"Hello {name}")
else:
    print("You must insert your name")

while vars:
    vars = False

while True:
    decision = input("> ")

    if decision == "y":
        print("you said yes")
    if decision == "n":
        print("you said no")
    else:
        break


def __init__(self, master):
    self.master = master
    self.setup_gui()
