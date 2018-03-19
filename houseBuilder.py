"""Twitch.tv./Ridgure"""

__author__ = "Ridgure"
__version__ = "2018.03.19"

import rhinoscriptsyntax as rs
words = x.split(" ")
wordsLowercase = x.lower().split(" ")
if "house" not in globals():
    house = False
if "door" not in globals():
    door = False
if "window" not in globals():
    window = False
try:
    if "!house" in wordsLowercase[1]:
        house = True
        houseStatus = house
    if "door" in wordsLowercase[1]:
        door = True
        doorStatus = door
    if "windows" in wordsLowercase[1]:
        window = True
        windowStatus = window
    if "!demolish" in wordsLowercase[1]:
        house = False
        door = False
        window = False
        houseStatus = house
        doorStatus = door
        windowStatus = window
    else:
        pass
except Exception, e:
    print e
    pass
houseStatus = house
doorStatus = door
windowStatus = window