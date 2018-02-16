#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# bot.py

import re
import socket
import random
import requests
import datetime
from time import sleep

# network functions go here

HOST = "irc.twitch.tv"                                  # the Twitch IRC server
PORT = 6667                                             # always use port 6667!
NICK = "riboture"                                       # your Twitch username, lowercase
PASS = "oauth:8qw7v2bn8pa8r69q53k91ycv9u4vi3"           # your Twitch OAuth token
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

def divide():
    test = data.split()[4:]
    makingNumbers = [int(i) for i in test]
    total = makingNumbers[0]
    for x in makingNumbers[1:]:
        total /= x
    everythingTogether = ' / '.join(map(str, makingNumbers)) + ' = ' + str(total)
    return everythingTogether

def lick():
    over = " over and "
    randomNumber = random.randint(1, 30)
    licks = over * randomNumber + "over again (x" + str(randomNumber) + ")"
    return licks

User_ID_ridgure = "106586349"
User_ID_riboture = "109949586"
Client_ID = "7cvp1bezng3ypb8bosyzosl3fcgb5ra"
Client_Secret = "gf4y8h01lffer7w0msjcnakdbstlfv"

def followers():
    url = "https://api.twitch.tv/helix/users/follows?to_id=" + User_ID_ridgure
    params = {"Client-ID" : ""+ Client_ID +"", "Authorization": PASS}
    response = requests.get(url, headers=params).json()
    print response
    #returns
    #{u'pagination': {u'cursor': u'eyJiIjpudWxsLCJhIjoiMTUxNDI1NDE4NzA4NTAyMDAwMCJ9'},
        # u'total': 421,
    # u'data': [
        # {u'to_id': u'106586349', u'followed_at': u'2018-01-18T20:11:57Z', u'from_id': u'163393705'},
        # {u'to_id': u'106586349', u'followed_at': u'2018-01-18T06:41:48Z', u'from_id': u'46728242'},
    Total =  response['total']
    print Total

def uptime():
    url = "https://api.twitch.tv/helix/streams?user_id=" + User_ID_riboture
    params = {"Client-ID" : ""+ Client_ID +"", "Authorization": PASS}
    response = requests.get(url, headers=params).json()
    LiveInformation = response['data'][0]
    # print response
    # returns
    # {u'pagination': {u'cursor': u'eyJiIjpudWxsLCJhIjp7Ik9mZnNldCI6MX19'},
    # u'data': [{
        # u'user_id': u'109949586',
        # u'language': u'no',
        # u'title': u'',
        # u'community_ids': [],
        # u'thumbnail_url': u'https://static-cdn.jtvnw.net/previews-ttv/live_user_riboture-{width}x{height}.jpg',
        # u'game_id': u'',
        # u'started_at': u'2018-01-22T07:09:44Z',
        # u'type': u'live',
        # u'id': u'27355247712',
        # u'viewer_count': 1}
    # ]}

    print LiveInformation['type']
    if LiveInformation['type'] == "live":
        try:
            message("Stream is live")
            return "live"
        except IndexError:
             pass
    else:
        message("Stream is offline")
        return "offline"


def liveOrNot():
    try:
        url = "https://api.twitch.tv/helix/streams?user_id=" + User_ID_riboture
        params = {"Client-ID" : ""+ Client_ID +"", "Authorization": PASS}
        response = requests.get(url, headers=params).json()
        LiveInformation = response['data'][0]
        # print response
        # returns
        # {u'pagination': {u'cursor': u'eyJiIjpudWxsLCJhIjp7Ik9mZnNldCI6MX19'},
        # u'data': [{
            # u'user_id': u'109949586',
            # u'language': u'no',
            # u'title': u'',
            # u'community_ids': [],
            # u'thumbnail_url': u'https://static-cdn.jtvnw.net/previews-ttv/live_user_riboture-{width}x{height}.jpg',
            # u'game_id': u'',
            # u'started_at': u'2018-01-22T07:09:44Z',
            # u'type': u'live',
            # u'id': u'27355247712',
            # u'viewer_count': 1}
        # ]}
        print LiveInformation['type']
        if LiveInformation['type'] == "live":
            return "live"
        else:
            return "offline"
    except IndexError:
        pass

def setValue(val):
    global globalVal
    valueChanged= g_val != val
    if valueChanged:
        liveOrNot()
    globalVal = val
    if valueChanged:
        liveOrNot()
    #This is called a setter function. Do more research. This might be the key to p

CHAT_MSG = re.compile(r"^:\w+!\w+@\w+\.tmi\.twitch\.tv PRIVMSG #\w+ :")

while True:

    try:
        def message(msg):
            try:
                s.send("PRIVMSG " + CHAN + " :" + msg + "\n")
            except IndexError:
                pass
        response = s.recv(1024).decode("utf-8")
        data = response.strip("\r\n")
        if response == "PING :tmi.twitch.tv\r\n":
            try:
                s.send("PONG :tmi.twitch.tv\r\n".encode("utf-8"))
            except IndexError:
                 pass
        if "!commands" in data.lower().split()[3]:
            try:
                message("My current commands are !social, !pack, !oclock, !smile, !timemeout, !multipy and !add")
            except IndexError:
                pass
        if "!test" in data.lower().split()[3]:
            try:
               message(data)
            except IndexError:
                pass
        if "!social" in data.lower().split()[3]:
            try:
                message("Add me on Facebook: fb.com/Ridgure")
                message("Add me on Twitter: Twitter.com/RigidStructure")
                message("Add me on Instagram: Instagram.com/Ridgure")
            except IndexError:
                pass
        if "!facebook" in data.lower().split()[3]:
            try:
                message("Add me on Facebook: fb.com/Ridgure")
            except IndexError:
                pass
        if "!twitter" in data.lower().split()[3]:
            try:
                message("Add me on Facebook: Twitter.com/RigidStructure")
            except IndexError:
                pass
        if "!instagram" in data.lower().split()[3]:
            try:
                message("Add me on Facebook: Instagram.com/RigidStructure")
            except IndexError:
                pass
        if "!raid" in data.lower().split()[3]:
            try:
                message("Please raid Twitch.tv/" + data.split()[4] + " msg: Ridgure raid twitchRaid twitchRaid twitchRaid")
            except IndexError:
                pass
        if "!pack" in data.lower().split()[3]:
            try:
                message("The modpack I am playing is called FTB Infinity Evolved on expert mode. Minecraft version 1.7.10. It is available through the twitch launcher and on curse")
            except IndexError:
                pass
        if "!oclock" in data.lower().split()[3]:
            try:
                message("The time for me right now is " + datetime.datetime.now().strftime("%H:%M") + " o'clock" + " CET")
            except IndexError:
                pass
        if "!shout" in data.lower().split()[3]:
            try:
                message("Check out this awesome streamer over at Twitch.tv/" + data.split()[4])
            except IndexError:
                pass
        if "!lick" in data.lower().split()[3]:
            try:
                message(sender() + " licks " + data.split()[4] + lick())
            except IndexError:
                pass
        if "!bellyrub" in data.lower().split()[3]:
            try:
                message(sender() + " rubs " + data.split()[4] + "'s belly " + lick())
            except IndexError:
                pass
        if "cobble" in data.lower().split()[2:]:
            try:
                message("Eww not cobble!")
            except IndexError:
                pass
        if "!timemeout" in data.lower().split()[3]:
            try:
                ## time out KBiglair ##
                message("/timeout " + sender() + " " + data.split()[4])
                message("Timed out " + sender() + " for " + data.split()[4] + " seconds")
            except IndexError:
                message("Add amount of seconds you want to be timed out after command")
                pass
        if "!uptime" in data.lower().split()[3]:
            try:
                uptime()
                message("Uptime is supposed to be displayed here")
            except IndexError:
                pass
        if liveOrNot() == "live":
            try:
                message("Stream just went live")
            except IndexError:
                pass
        if "!smile" in data.lower().split()[3]:
            try:
                message(sender() + " smiles at " + data.split()[4] + " " + randomEmote())
            except IndexError:
                message("Remember to smile at someone!")
            except Exception,e:
                message ("Smile failed")
                message (str(e))
        if "!multiply" in data.lower().split()[3]:
            try:
                message(multiply())
            except IndexError:
                pass
            except Exception,e:
                message ("Multiplication failed")
                message (str(e))
        if "!divide" in data.lower().split()[3]:
            try:
                message(divide())
            except IndexError:
                pass
            except Exception, e:
                message("Division failed")
                message(str(e))
        if "!add" in data.lower().split()[3]:
            try:
                message(add())
            except IndexError:
                pass
            except Exception, e:
                message("Addition failed")
                message(str(e))
        else:
            username = re.search(r"\w+", response).group(0) # return the entire match
            message = CHAT_MSG.sub("", response)
            print(username + ": " + message)
            print response
            sleep(0.1)
    except IndexError:
        pass
    except Exception, e:
        print "An error just occurred"
        print str(e)