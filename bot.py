#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# bot.py

import re
import socket
from time import sleep

# network functions go here

HOST = "irc.twitch.tv"                                  # the Twitch IRC server
PORT = 6667                                             # always use port 6667!
NICK = "riboture"                                       # your Twitch username, lowercase
PASS = "oauth:fv7eg2w31t8fslccflit2506ej3gkx"           # your Twitch OAuth token
CHAN = "#ridgure"                                       # the channel you want to join
RATE = 20/30                                            # messages per second
PATT = [
    r"swear",
    # ...
    r"some_pattern", r"fuck", r"balls"
]

s = socket.socket()
s.connect((HOST, PORT))
s.send("PASS {}\r\n".format(PASS).encode("utf-8"))
s.send("NICK {}\r\n".format(NICK).encode("utf-8"))
s.send("JOIN {}\r\n".format(CHAN).encode("utf-8"))



def multiply():
    test = data.split()[4:]
    makingNumbers = [int(i) for i in test]
    total = 1
    for x in makingNumbers:
        total *= x
    everythingTogether = ' * '.join(map(str, makingNumbers)) + ' = ' + str(total)
    return message(everythingTogether)



CHAT_MSG = re.compile(r"^:\w+!\w+@\w+\.tmi\.twitch\.tv PRIVMSG #\w+ :")

while True:

    def message(msg):
        s.send("PRIVMSG " + CHAN + " :" + msg + "\n")
    response = s.recv(1024).decode("utf-8")
    data = response.strip("\r\n")
    if response == "PING :tmi.twitch.tv\r\n":
        s.send("PONG :tmi.twitch.tv\r\n".encode("utf-8"))
    if "!social" in data:
        message("Add me on Facebook: fb.com/Ridgure")
        message("Add me on Facebook: Twitter.com/RigidStructure")
        message("Add me on Facebook: Instagram.com/Ridgure")
    if "!Social" in data:
        message("Add me on Facebook: fb.com/Ridgure")
        message("Add me on Facebook: Twitter.com/RigidStructure")
        message("Add me on Facebook: Instagram.com/Ridgure")
    if "!facebook" in data:
        message("Add me on Facebook: fb.com/Ridgure")
    if "!twitter" in data:
        message("Add me on Facebook: Twitter.com/RigidStructure")
    if "!instagram" in data:
        message("Add me on Facebook: Instagram.com/RigidStructure")
    if "!Facebook" in data:
        message("Add me on Facebook: fb.com/Ridgure")
    if "!Twitter" in data:
        message("Add me on Facebook: Twitter.com/RigidStructure")
    if "!Instagram" in data:
        message("Add me on Facebook: Instagram.com/Ridgure")
    if "!multiply" in data:
        message(multiply())
    else:
        username = re.search(r"\w+", response).group(0) # return the entire match
        message = CHAT_MSG.sub("", response)
        print(username + ": " + message)
        for pattern in PATT:
            if re.match(pattern, message):
                ban(s, username)
                break
        sleep(0.1)

