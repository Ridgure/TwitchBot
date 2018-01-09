#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# bot.py

import re
import socket
import random
from time import sleep

# network functions go here

HOST = "irc.twitch.tv"                                  # the Twitch IRC server
PORT = 6667                                             # always use port 6667!
NICK = "riboture"                                       # your Twitch username, lowercase
PASS = "oauth:fv7eg2w31t8fslccflit2506ej3gkx"           # your Twitch OAuth token
CHAN = "#ridgure"                                       # the channel you want to join
RATE = 20/30                                            # messages per second

s = socket.socket()
s.connect((HOST, PORT))
s.send("PASS {}\r\n".format(PASS).encode("utf-8"))
s.send("NICK {}\r\n".format(NICK).encode("utf-8"))
s.send("JOIN {}\r\n".format(CHAN).encode("utf-8"))

def randomEmote():
    emotes = ["Kappa", "MrDestructoid", "BCWarrior", "DansGame", "SwiftRage", "PJSalt", "Kreygasm", "SSSsss", "PunchTrees", "FunRun", "SMOrc", "FrankerZ", "BibleThump", "PogChamp", "ResidentSleeper", "4Head", "FailFish", "Keepo", "ANELE", "BrokeBack", "EleGiggle", "BabyRage", "panicBasket", "WutFace", "HeyGuys", "KappaPride", "CoolCat", "NotLikeThis", "riPepperonis", "duDudu", "bleedPurple", "SeemsGood", "MingLee", "KappaRoss", "KappaClaus", "OhMyDog", "OPFrog", "SeriousSloth", "KomodoHype", "VoHiYo", "KappaWealth", "cmonBruh", "NomNom", "StinkyCheese", "ChefFrank", "FutureMan", "OpieOP", "DxCat", "GivePLZ", "TakeNRG", "Jebaited", "CurseLit", "TriHard", "CoolStoryBob", "ItsBoshyTime", "PartyTime", "TheIlluminati", "BlessRNG", "TwitchLit", "CarlSmile", "Squid3", "VaultBoy", "LUL", "PowerUpR", "PowerUpL"]
    randomNumber = random.randint(0, len(emotes))
    randomEmote = emotes[randomNumber]
    return randomEmote

def sender():
    m = re.search(':(.+?)!', data)
    sender= m.group(1)
    return sender

def add():
    test = data.split()[4:]
    makingNumbers = [int(i) for i in test]
    addingNumbers = sum(makingNumbers)
    everythingTogether = ' + '.join(map(str, makingNumbers)) + ' = ' + str(addingNumbers)
    return everythingTogether

def multiply():
    test = data.split()[4:]
    makingNumbers = [int(i) for i in test]
    total = 1
    for x in makingNumbers:
        total *= x
    everythingTogether = ' * '.join(map(str, makingNumbers)) + ' = ' + str(total)
    return everythingTogether



CHAT_MSG = re.compile(r"^:\w+!\w+@\w+\.tmi\.twitch\.tv PRIVMSG #\w+ :")

while True:

    def message(msg):
        s.send("PRIVMSG " + CHAN + " :" + msg + "\n")
    response = s.recv(1024).decode("utf-8")
    data = response.strip("\r\n")
    if response == "PING :tmi.twitch.tv\r\n":
        s.send("PONG :tmi.twitch.tv\r\n".encode("utf-8"))
    if "!test" in data.lower():
        message(data)
    if "!social" in data.lower():
        message("Add me on Facebook: fb.com/Ridgure")
        message("Add me on Facebook: Twitter.com/RigidStructure")
        message("Add me on Facebook: Instagram.com/Ridgure")
    if "!facebook" in data.lower():
        message("Add me on Facebook: fb.com/Ridgure")
    if "!twitter" in data.lower():
        message("Add me on Facebook: Twitter.com/RigidStructure")
    if "!instagram" in data.lower():
        message("Add me on Facebook: Instagram.com/RigidStructure")
    if "!raid" in data.lower():
        message("Please raid Twitch.tv/" + data.split()[4] + " msg: Ridgure raid twitchRaid twitchRaid twitchRaid")
    if "!smile" in data.lower():
        try:
            message(sender() + " smiles at " + data.split()[4] + " " + randomEmote())
        except IndexError:
            message("Remember to smile at someone!")
        except Exception,e:
            message ("Smile failed")
            message (str(e))
    if "!multiply" in data.lower():
        try:
            message(multiply())
        except:
            message ("Multiplication failed")
    if "!add" in data.lower():
        try:
            message(add())
        except:
            message ("Addition failed")
    else:
        username = re.search(r"\w+", response).group(0) # return the entire match
        message = CHAT_MSG.sub("", response)
        print(username + ": " + message)
        sleep(0.1)