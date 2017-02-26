"""
An adventure planting a tree.
"""

import random
import time
import textwrap
import re

def p(text):
    """Print `text` with word wrapping. This makes it easier to work with
    triple-quoted strings."""

    # first remove duplicate whitespace
    text = " ".join(text.split())
    print textwrap.fill(text)

def doorclang():
    p("The door closes behind you as you enter the castle!")
    return 4

def magicmirror():
    p("""
      You touch the magic mirror and are sucked in! Who knows where you'll
      end up.
      """)
    return random.choice([6, 7, 16, 12, 17, 19])

def ogre():
    p("""
      "Good evening!" says the ogre. "If you want to rescue the prince,
      you must answer this riddle: A doctor and a boy were fishing. The
      boy was the doctor's son, but the doctor was not the boy's father.
      Who was the doctor?"
      """)
    answer = raw_input("What do you say? ").lower()
    if answer.find("mother") == -1 and answer.find("mom") == -1:
        p("""
          The ogre frowns: "That is not the answer I desire. You may not
          pass." The ogre throws you down the grand staircase.
          """)
        return 14

    p("""
      The ogre smiles: "Correct! Congratulations, you may pass."
      """)
    return 20

def lockeddoor9():
    print "The East door out of the courtyard is locked!"
    return 9

def lockeddoor10():
    print "The door West to the courtyard is locked!"
    return 10

def wine():
    print "You fall asleep after the wine. It'll take a little while to wake up again."
    for i in range(10):
        time.sleep(1)
        print "%i..." % (i,)
    print "Maybe don't do that again."
    return 16

# A dictionary of rooms in the maze.
#
# Each room has:
#   "description": "text to print"
#   "paths": [ ("N", "description", nextroom)... ]
# `nextroom` can either be a number (of the next room) or a function which
# is called and returns the next room to go to.

rooms = {
    1: {
        "description": """The southern door to the castle is ajar.""",
        "paths": [
            ("G", "Go into the castle", doorclang),
        ],
    },
    2: {
        "description": """
            You are at the end of a hallway. There is an outside window
            to the West.""",
        "paths": [
            ("N", "Open the door North to the guest bedroom.", 7),
            ("E", "Go East", 3),
        ],
    },
    3: {
        "description": "You are in a long dark hallway.",
        "paths": [
            ("E", "Go East", 4),
            ("W", "Go West", 2),
        ],
    },
    4: {
        "description": "The castle door is closed. No turning back now!",
        "paths": [
            ("E", "Go East", 5),
            ("W", "Go West", 3),
        ],
    },
    5: {
        "description": """You are in a corner hallway. There is a slimy spot
            on the floor.""",
        "paths": [
            ("N", "Go North", 10),
            ("W", "Go West", 4),
        ],
    },
    6: {
        "description": "You are at the end of a hall with a red magic mirror.",
        "paths": [
            ("T", "Touch the mirror", magicmirror),
            ("N", "Go North", 11),
        ],
    },
    7: {
        "description": """You are in the guest bedroom. There is a blue magic
            mirror here.""",
        "paths": [
            ("T", "Touch the mirror", magicmirror),
            ("S", "Go South", 2),
        ],
    },
    8: {
        "description": """The halls turns here. To the east you can see the
            courtyard.""",
        "paths": [
            ("N", "Go North", 13),
            ("E", "Go East to the courtyard", 9),
        ],
    },
    9: {
        "description": "You are in the castle courtyard.",
        "paths": [
            ("N", "Go North", 14),
            ("E", "Go East", lockeddoor9),
            ("W", "Go West", 8),
        ],
    },
    10: {
        "description": "You are in the dining room. It's pretty messy.",
        "paths": [
            ("N", "Go North", 15),
            ("E", "Go East", 11),
            ("S", "Go South", 5),
            ("W", "Go West through a door into the courtyard", lockeddoor10),
        ],
    },
    11: {
        "description": "You are in a service hall near the dining room.",
        "paths": [
            ("S", "Go South", 6),
            ("W", "Go West", 10),
        ],
    },
    12: {
        "description": """You are in the princess's bedroom. There is a green
            magic mirror.""",
        "paths": [
            ("T", "Touch the mirror", magicmirror),
            ("E", "Go East out the door", 13),
        ],
    },
    13: {
        "description": "You are in a hallway near two bedrooms.",
        "paths": [
            ("N", "Go North to the master bedroom", 17),
            ("W", "Go West to the princess's bedroom", 12),
            ("S", "Go South down the hall.", 8),
        ],
    },
    14: {
        "description": "You are in a great hall north of the courtyard.",
        "paths": [
            ("N", "Go North up the grand staircase.", 18),
            ("S", "Go South to the courtyard.", 9),
        ],
    },
    15: {
        "description": "You are in the kitchen.",
        "paths": [
            ("S", "Go South to the dining room", 10),
            ("W", "Go West to the pantry.", 16),
        ],
    },
    16: {
        "description": "You are in the pantry. There is a purple magic mirror.",
        "paths": [
            ("W", "Drink a bottle of wine", wine),
            ("T", "Touch the mirror", magicmirror),
            ("W", "Go West to the kitchen", 15),
        ],
    },
    17: {
        "description": "You are in the master bedroom. There is an orange magic mirror.",
        "paths": [
            ("T", "Touch the mirror", magicmirror),
            ("S", "Go South out of the bedroom", 13),
        ],
    },
    18: {
        "description": """You are at the top of the grand staircase. There is
            an ogre blocking the door north to the music room.""",
        "paths": [
            ("O", "Approach the ogre.", ogre),
            ("E", "Go East along the balcony over the great hall.", 19),
            ("S", "Go South down the grand staircase.", 14),
        ],
    },
    19: {
        "description": """You are on the balcony over the grand hallway. There
        is a silver magic mirror on the wall.""",
        "paths": [
            ("T", "Touch the mirror", magicmirror),
            ("W", "Go the top of the grand staircase", 18),
        ],
    },
    20: {
        "description": """You have found your prince in the music room! May you
            live happily ever after. Good luck!""",
    },
}

print "You need to rescue your prince! He is somewhere in the castle here."

# Set the starting room
room = 1
while True:
    roomdata = rooms[room]
    print
    p(roomdata['description'])
    # if we're at room 20, we're done!
    if room == 20:
        break

    keymap = {}
    keys = []
    for key, description, nextroom in roomdata["paths"]:
        keymap[key] = nextroom
        keys.append(key)
        print "  %s: %s" % (key, description)

    print "? ",
    while True:
        key = raw_input().upper()
        if key in keymap:
            break
        print "Choose %s: " % ("/".join(keys),),

    nextroom = keymap[key]
    if isinstance(nextroom, int):
        room = nextroom
    else:
        # if nextroom isn't an int, it's a function we call
        room = nextroom()

