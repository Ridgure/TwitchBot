#!/usr/bin/env python
# -*- coding: utf-8 -*-
# bot.py

import os
import csv
import re
import socket
from config import *
from time import sleep

s = socket.socket()
s.connect((Host, Port))
s.send("PASS {}\r\n".format("oauth:" + FollowerToken).encode("utf-8"))
s.send("NICK {}\r\n".format(Nickname).encode("utf-8"))
s.send("JOIN {}\r\n".format(Channel).encode("utf-8"))

while True:

    try:
        def message(msg):
            try:
                s.send("PRIVMSG " + Channel + " :" + msg + "\n")
            except IndexError:
                pass
        response = s.recv(1024).decode("utf-8")
        data = response.strip("\r\n")
        if response == "PING :tmi.twitch.tv\r\n":
            try:
                s.send("PONG :tmi.twitch.tv\r\n".encode("utf-8"))
                print "Reply: PONG :tmi.twitch.tv"
            except IndexError:
                pass
            except Exception, e:
                print("Pong error")
                print(str(e))
        if True:
            try:
                if "PRIVMSG" in data:
                    username = re.search(r"\w+", response).group(0)
                    text = re.search(r'(?<=PRIVMSG)\W+\w+\s\:(.*)', response).group(1)
                    print(username + ": " + text)
                    try:
                        csvfile = open('followerData.csv', "rb")
                        followerDataReader = csv.reader(csvfile, delimiter=",")
                        followerLines = list(followerDataReader)
                        csvfile.close()
                        bot = True
                        for i in range(len(followerLines)):
                            if username.lower().rstrip() == followerLines[i][0].lower().rstrip():
                                bot = False
                        if bot == True:
                            message("/ban " + username)
                    except Exception, e:
                        print str(e)
                    if "curselit (╯°□°）╯︵ ┻━┻" in text.lower().encode("utf-8"):
                        try:
                            message("┬─┬ノ( º _ ºノ)")
                        except Exception, e:
                            print str(e)
                else:
                    print "Response: " + response
            except Exception, e:
                print str(e)
            sleep(0.1)
    except IndexError:
        pass
    except Exception, e:
        print "An error just occurred"
        print str(e)
