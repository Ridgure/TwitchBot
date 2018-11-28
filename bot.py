#!/usr/bin/env python
# -*- coding: utf-8 -*-
# bot.py

import os
import re
import socket
import random
import requests
import datetime
import math
import csv
from config import *
from time import sleep
from decimal import *

s = socket.socket()
s.connect((Host, Port))
s.send("PASS {}\r\n".format("oauth:" + Token).encode("utf-8"))
s.send("NICK {}\r\n".format(Nickname).encode("utf-8"))
s.send("JOIN {}\r\n".format(Channel).encode("utf-8"))

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

def subscribers():
    # url = "https://api.twitch.tv/kraken/channels/" + User_ID_ridgure
    # params = {"Client-ID" : ""+ ClientID +"", "Authorization": "oauth:" + Token, "Accept": "application/vnd.twitchtv.v5+json"}
    # response = requests.get(url, headers=params).json()

    # responds
    # {u'private_video': False,
    # u'updated_at': u'2018-11-26T00:23:37Z',
    # u'privacy_options_enabled': False,
    # u'video_banner': u'https://static-cdn.jtvnw.net/jtv_user_pictures/ridgure-channel_offline_image-3c60c59d9ba5c169-1920x1080.png',
    # u'partner': False,
    # u'logo': u'https://static-cdn.jtvnw.net/jtv_user_pictures/ee5101dc-3ddb-43aa-a887-a569414a8844-profile_image-300x300.png',
    # u'display_name': u'Ridgure',
    # u'followers': 720,
    # u'broadcaster_software': u'unknown_rtmp',
    # u'broadcaster_language': u'en',
    # u'broadcaster_type': u'affiliate',
    # u'status': u'Making the Asakusa Tourism Center by Kengo Kuma | Architecture',
    # u'description': u'I stream every Wednesday from 7-12 CET. You can expect entertainment and other fun as well as an awesome community of chatters and other streamers that hang out when I am live.',
    # u'views': 11096,
    # u'game': u'Art',
    # u'name': u'ridgure',
    # u'language': u'en',
    # u'url': u'https://www.twitch.tv/ridgure',
    # u'created_at': u'2015-11-08T22:14:42Z',
    # u'mature': True,
    # u'profile_banner_background_color': u'#000000',
    # u'_id': u'106586349',
    # u'profile_banner': u'https://static-cdn.jtvnw.net/jtv_user_pictures/ridgure-profile_banner-aab842adb656bc98-480.png'}

    # Use this url for getting the token
    # url = "https://id.twitch.tv/oauth2/authorize?client_id=" + ClientID + "&redirect_uri=http://localhost&response_type=token&scope=channel_subscriptions+user_read+channel_check_subscription+chat_edit+channel_moderate+chat_login"

    url = "https://api.twitch.tv/kraken/channels/106586349/subscriptions"
    params = {"Accept": "application/vnd.twitchtv.v5+json", "Client-ID": ClientID, "Authorization": "OAuth " + Token, "limit": "100"}
    response = requests.get(url, headers=params, allow_redirects=True)
    if response.status_code == 429:
        print "Too many subscriber requests"
    global subscriberResponse
    subscriberResponse = response.json()
    return subscriberResponse

    # returns
    # {u'_total': 3,
    # u'subscriptions': [
    #     {u'is_gift': False, u'sender': None, u'sub_plan_name': u'Channel Subscription (ridgure)', u'sub_plan': u'1000',
    #      u'created_at': u'2017-06-28T19:23:44Z', u'user': {
    #         u'bio': u'Just a start up streamer who does a bit of youtube while still working and going to college',
    #         u'display_name': u'LilGamerHelle', u'name': u'lilgamerhelle', u'created_at': u'2012-08-03T19:04:34Z',
    #         u'updated_at': u'2018-11-25T20:13:23Z',
    #         u'logo': u'https://static-cdn.jtvnw.net/jtv_user_pictures/lilgamerhelle-profile_image-bde580adc7af34ad-300x300.png',
    #         u'_id': u'32670426', u'type': u'user'}, u'_id': u'c56ff1e6b85b0bcbbfbbb471b7fe903798ecb9dc'},
    #     {u'is_gift': False, u'sender': None, u'sub_plan_name': u'Channel Subscription (ridgure): $24.99 Sub',
    #      u'sub_plan': u'3000', u'created_at': u'2017-06-28T20:11:45Z', u'user': {
    #         u'bio': u'I stream every Wednesday from 7-12 CET. You can expect entertainment and other fun as well as an awesome community of chatters and other streamers that hang out when I am live.',
    #         u'display_name': u'Ridgure', u'name': u'ridgure', u'created_at': u'2015-11-08T22:14:42Z',
    #         u'updated_at': u'2018-11-27T23:23:47Z',
    #         u'logo': u'https://static-cdn.jtvnw.net/jtv_user_pictures/ee5101dc-3ddb-43aa-a887-a569414a8844-profile_image-300x300.png',
    #         u'_id': u'106586349', u'type': u'user'}, u'_id': u'f6fdc613e0ee25ef84b5d0c16605c4444e9d7b50'},
    #     {u'is_gift': False, u'sender': None, u'sub_plan_name': u'Channel Subscription (ridgure)', u'sub_plan': u'1000',
    #      u'created_at': u'2018-01-03T23:11:27Z',
    #      u'user': {u'bio': u'Rocket League/Minecraft', u'display_name': u'Cirekon', u'name': u'cirekon',
    #                u'created_at': u'2012-07-04T16:10:34Z', u'updated_at': u'2018-11-25T13:14:25Z',
    #                u'logo': u'https://static-cdn.jtvnw.net/jtv_user_pictures/bca68a9164bd54a1-profile_image-300x300.jpeg',
    #                u'_id': u'31861174', u'type': u'user'}, u'_id': u'e7879cef043c356c6b99901f3c89d2e32f1d0543'}
    #  ]}


def followers():
    try:
        url100 = "https://api.twitch.tv/helix/users/follows?to_id=" + User_ID_ridgure + "&first=100"
        params = {"Client-ID" : ""+ ClientID +"", "Authorization": "oauth:" + Token}
        response = requests.get(url100, headers=params)
        responseFirst100 = response.json()
        if response.status_code == 429:
            print "Too many follower requests"

        global pagination
        pagination = responseFirst100['pagination']['cursor']
        totalFollowers = responseFirst100['total']
        global followerList
        followerList = responseFirst100['data']

        # making a list of all the followers
        for i in xrange(int(math.ceil(totalFollowers / float(100))) - 1):
            url200 = "https://api.twitch.tv/helix/users/follows?to_id=" + User_ID_ridgure + "&first=100&after=" + pagination
            response = requests.get(url200, headers=params).json()
            pagination = response['pagination']['cursor']
            followerList = followerList + response['data']

        return followerList
    except Exception, e:
        pass

    # print response
    # returns
    #{u'pagination': {u'cursor': u'eyJiIjpudWxsLCJhIjoiMTUxNDI1NDE4NzA4NTAyMDAwMCJ9'},
        # u'total': 421,
    # u'data': [
        # {u'to_id': u'106586349', u'followed_at': u'2018-01-18T20:11:57Z', u'from_id': u'163393705'},
        # {u'to_id': u'106586349', u'followed_at': u'2018-01-18T06:41:48Z', u'from_id': u'46728242'},

def followAgeAll():
    global followAgeList
    followAgeList = [[] for i in range(len(followerList))]

    for i in xrange(len(followerList)):

        # Get follow Day Month Year
        m = re.search('(.+?)T', followerList[i]['followed_at'])
        followDate = m.group(1).encode('ascii', 'ignore')
        m = re.search('(.+?)-', followDate)
        followYear = m.group(1).encode('ascii', 'ignore')
        m = re.search('-(.+?)-', followDate)
        followMonth = m.group(1).encode('ascii', 'ignore')
        m = re.search('-(.*)', followDate)
        followDay = m.group(1).encode('ascii', 'ignore')
        m = re.search('-(.*)', followDay)
        followDay = m.group(1).encode('ascii', 'ignore')

        # Get follow Hour Minute Second
        m = re.search('T(.+?)Z', followerList[i]['followed_at'])
        followTime = m.group(1).encode('ascii', 'ignore')
        m = re.search('(.+?):', followTime)
        followHour = m.group(1).encode('ascii', 'ignore')
        m = re.search(':(.+?):', followTime)
        followMinute = m.group(1).encode('ascii', 'ignore')
        m = re.search(':(.*)', followTime)
        followSecond = m.group(1).encode('ascii', 'ignore')
        m = re.search(':(.*)', followSecond)
        followSecond = m.group(1).encode('ascii', 'ignore')

        # Get current Day Month Year
        currentDate = datetime.datetime.utcnow().strftime("%Y-%m-%d")
        m = re.search('(.+?)-', currentDate)
        currentYear = m.group(1).encode('ascii', 'ignore')
        m = re.search('-(.+?)-', currentDate)
        currentMonth = m.group(1).encode('ascii', 'ignore')
        m = re.search('-(.*)', currentDate)
        currentDay = m.group(1).encode('ascii', 'ignore')
        m = re.search('-(.*)', currentDay)
        currentDay = m.group(1).encode('ascii', 'ignore')

        # Get current Hour Minute Second
        currentTime = datetime.datetime.utcnow().strftime("%H:%M:%S")
        m = re.search('(.+?):', currentTime)
        currentHour = m.group(1).encode('ascii', 'ignore')
        m = re.search(':(.+?):', currentTime)
        currentMinute = m.group(1).encode('ascii', 'ignore')
        m = re.search(':(.*)', currentTime)
        currentSecond = m.group(1).encode('ascii', 'ignore')
        m = re.search(':(.*)', currentSecond)
        currentSecond = m.group(1).encode('ascii', 'ignore')

        # Compare follow with current
        followDate = datetime.date(int(followYear), int(followMonth), int(followDay))
        followDateTime = datetime.datetime.combine(followDate, datetime.time(int(followHour), int(followMinute), int(followSecond), 0,  tzinfo=None))
        currentDate = datetime.date(int(currentYear), int(currentMonth), int(currentDay))
        currentDateTime = datetime.datetime.combine(currentDate, datetime.time(int(currentHour), int(currentMinute), int(currentDay), 0,  tzinfo=None))
        deltaDate = currentDateTime - followDateTime
        deltaHours = int(math.floor(deltaDate.seconds / 3600))
        deltaMinutes = int(math.floor((deltaDate.seconds - (deltaHours * 3600)) / 60))
        deltaSeconds = int(deltaDate.seconds - (deltaHours * 3600) - (deltaMinutes * 60))

        # Return array
        followAgeList[i].insert(0, str(deltaDate))
        followAgeList[i].insert(1, deltaDate.days)
        followAgeList[i].insert(2, deltaHours)
        followAgeList[i].insert(3, deltaMinutes)
        followAgeList[i].insert(4, deltaSeconds)
        followAgeList[i].insert(5, deltaDate.seconds)
        followAgeList[i].insert(6, followDateTime)

    return followAgeList


def uptime():
    url = "https://api.twitch.tv/helix/streams?user_id=" + User_ID_ridgure
    params = {"Client-ID" : ""+ ClientID +"", "Authorization": "oauth:" + Token}
    response = requests.get(url, headers=params).json()
    StreamStart = response['data'][0]
    # print response
    # returns
    # {u'pagination': {u'cursor': u'eyJiIjpudWxsLCJhIjp7Ik9mZnNldCI6MX19'}, u'data': [{
        # u'user_id': u'109949586',
        # u'language': u'',
        # u'title': u'This is the title',
        # u'type': u'live',
        # u'tag_ids': None,
        # u'community_ids': [],
        # u'thumbnail_url': u'https://static-cdn.jtvnw.net/previews-ttv/live_user_riboture-{width}x{height}.jpg',
        # u'game_id': u'0',
        # u'started_at': u'2018-11-16T11:04:29Z',
        # u'user_name': u'',
        # u'id': u'31261236144',
        # u'viewer_count': 0}
    # ]}
    m = re.search('T(.+?):', StreamStart['started_at'])
    startHours = m.group(1)
    m = re.search(':(.+?):', StreamStart['started_at'])
    startMinutes = m.group(1)
    finishTime = datetime.datetime.utcnow().strftime("%H:%M")
    m = re.search('(.+?):', finishTime)
    finishHours = m.group(1)
    m = re.search(':(.*)', finishTime)
    finishMinutes = m.group(1)
    totalStartMinutes = (int(startHours) * 60) + int(startMinutes)
    totalFinishMinutes = (int(finishHours) * 60) + int(finishMinutes)
    m = re.search('(.+?)T', StreamStart['started_at'])
    startDate = m.group(1).encode('ascii', 'ignore')
    m = re.search('(.+?)-', startDate)
    startYear = m.group(1).encode('ascii', 'ignore')
    m = re.search('-(.+?)-', startDate)
    startMonth = m.group(1).encode('ascii', 'ignore')
    m = re.search('-(.*)', startDate)
    startDay = m.group(1).encode('ascii', 'ignore')
    m = re.search('-(.*)', startDay)
    startDay = m.group(1).encode('ascii', 'ignore')
    finishDate = str(datetime.datetime.utcnow().strftime("%Y-%m-%d"))
    m = re.search('(.+?)-', finishDate)
    finishYear = m.group(1).encode('ascii', 'ignore')
    m = re.search('-(.+?)-', finishDate)
    finishMonth = m.group(1).encode('ascii', 'ignore')
    m = re.search('-(.*)', finishDate)
    finishDay = m.group(1).encode('ascii', 'ignore')
    m = re.search('-(.*)', finishDay)
    finishDay = m.group(1).encode('ascii', 'ignore')
    d1 = datetime.date(int(startYear), int(startMonth), int(startDay))
    d2 = datetime.date(int(finishYear), int(finishMonth), int(finishDay))
    delta = d2 - d1
    if delta.days == 1:
        totalUptimeMinutes = int(totalFinishMinutes) - int(totalStartMinutes) + (24 * 60)
        uptimeHours = int(math.floor(totalUptimeMinutes / 60))
        uptimeMinutes = totalUptimeMinutes - (uptimeHours * 60)
        return "The stream has been live for " + str(uptimeHours) + "h " + str(uptimeMinutes) + "m"
    if delta.days == 2:
        totalUptimeMinutes = int(totalFinishMinutes) - int(totalStartMinutes) + (48 * 60)
        uptimeHours = int(math.floor(totalUptimeMinutes / 60))
        uptimeMinutes = totalUptimeMinutes - (uptimeHours * 60)
        return "The stream has been live for " + str(uptimeHours) + "h " + str(uptimeMinutes) + "m"
    if delta.days == 3:
        totalUptimeMinutes = int(totalFinishMinutes) - int(totalStartMinutes) + (72 * 60)
        uptimeHours = int(math.floor(totalUptimeMinutes / 60))
        uptimeMinutes = totalUptimeMinutes - (uptimeHours * 60)
        return "The stream has been live for " + str(uptimeHours) + "h " + str(uptimeMinutes) + "m"
    if delta.days == 0:
        totalUptimeMinutes = int(totalFinishMinutes) - int(totalStartMinutes)
        uptimeHours = int(math.floor(totalUptimeMinutes / 60))
        uptimeMinutes = totalUptimeMinutes - (uptimeHours * 60)
        return "The stream has been live for " + str(uptimeHours) + "h " + str(uptimeMinutes) + "m"

CHAT_MSG = re.compile(r"^:\w+!\w+@\w+\.tmi\.twitch\.tv PRIVMSG #\w+ :")

while True:

    try:
        def message(msg):
            try:
                s.send("PRIVMSG " + Channel + " :" + msg + "\n")
            except IndexError:
                pass
        response = s.recv(1024).decode("utf-8")
        data = response.strip("\r\n")
        if True == True:
            try:
                # Get new follower list and format it to compare with unfollowers
                followers()
                test = []
                for i in range(len(followerList)):
                    test.insert(0, followerList[i]['from_name'].encode('ascii', 'ignore'))
                test = map(str.strip, test)

                # Get existing follower list
                if not os.path.exists('followerData.csv'):
                    open('followerData.csv', "w+").close()
                with open('followerData.csv', "rb") as csvfile:
                    followerDataReader = csv.reader(csvfile, delimiter=",")
                    lines = list(followerDataReader)

                # Compare follower lists
                newFollowers = [item for item in test if item not in [i[0] for i in lines[1:]]]
                unfollowers = [item for item in [i[0] for i in lines[1:]] if item not in test]

                # thank new follower and add to existing list
                if len(newFollowers) > 0:
                    for i in range(len(newFollowers)):
                        lines.append([newFollowers[i], "", "1", "", "", "", ""])
                    with open('followerDataNew.csv', "wb") as csvfile:
                        followerDataWriter = csv.writer(csvfile, delimiter=",")
                        followerDataWriter.writerows(lines)
                    os.remove('followerData.csv')
                    os.rename('followerDataNew.csv', 'followerData.csv')
                    if len(newFollowers) == 1:
                        message("Thank you for following the channel " + " ".join(newFollowers) + "! Type !bat to see the information on your bat")
                    if len(newFollowers) > 1:
                        message("Thank you for following the channel " + ", ".join(newFollowers[0:-1]) + " and " + newFollowers[-1] + "! !bat to see the information on your bat")

                # If someone unfollows set follow value to 0
                for i1 in range(len(unfollowers)):
                    for i2 in range(len(lines)):
                        if lines[i2][0] == unfollowers[i1]:
                            lines[i2][2] = "0"

                # Assign gender
                for i in range(len(lines)):
                    if lines[i][4] == "":
                        maleFemale = random.randint(0, 1)
                        if maleFemale == 1:
                            lines[i][4] = 'Female'
                        else:
                            lines[i][4] = 'Male'

                maleNames = ['Matrix', 'Fuzz', 'Tiberius', 'Impaler', 'Shrike', 'Vulkan', 'Butch', 'Guano',
                             'Ripmaw', 'Vamp', 'Nightmare', 'Baxter', 'Azar', 'Lockjaw', 'Booboo', 'Darth',
                             'Dimitri', 'Blues', 'Moon', 'Shrike', 'Midnight', 'Sonar', 'Flaps', 'Screech',
                             'Draculon', 'Sabath', 'Angel', 'Vladimir', 'Grey', 'Spuds', 'Dexter', 'Mothra',
                             'Cole', 'Dimitri', 'Archangel', 'Bruce', 'Drake', 'Comet', 'Spectre', 'Rascal',
                             'Blade', 'Nyx', 'Basil', 'Char', 'Wingnut', 'Orion', 'Shadow', 'Brutus', 'Ash',
                             'Lucifer']
                femaleNames = ['Angel', 'Trixy', 'Ruth', 'Rhyme', 'Rhyme', 'Echo', 'Mirage', 'Flutters',
                               'Bandetta', 'Giggles', 'Sona', 'Dawnstar', 'Nibbles', 'Harmony', 'Equina',
                               'Siren', 'Mittens', 'Sage', 'Cookie', 'Dawnstar', 'Moonlight', 'Shine', 'Haze',
                               'Lady', 'Scarlett', 'Illumina', 'Ivy', 'Morning', 'Abby', 'Sade', 'Aine',
                               'Shade', 'Velvet', 'Aura', 'Azurys', 'Dot', 'Equinox', 'Twilight', 'Iris',
                               'Cerulean', 'Star', 'Violet', 'Raine', 'Lucy', 'Nugget', 'Indigo', 'Skye',
                               'Skylar', 'Morticia']

                # Assign Name
                for i in range(len(lines)):
                    try:
                        if lines[i][3] == "":
                            if lines[i][4] == 'Male':
                                randomNumber = random.randint(0, len(maleNames))
                                maleName = maleNames[randomNumber]
                                lines[i][3] = maleName
                            if lines[i][4] == 'Female':
                                randomNumber = random.randint(0, len(femaleNames))
                                femaleName = femaleNames[randomNumber]
                                lines[i][3] = femaleName
                    except IndexError:
                        print 'Skipped adding gender. Will add next time this loops'
                        pass

                # Refresh the total seconds followed per user
                followAgeAll()
                for i in range(len(lines)):
                    for i2 in range(len(followerList)):
                        if lines[i][0] == followerList[i2]['from_name']:
                            lines[i][1] = followAgeList[i2][5]

                # Assign color
                global totalBlackBats, totalBrownBats, totalRedBats
                global blackBatScore, brownBatScore, redBatScore
                global percentageBlackBats, percentageRedBats, percentageBrownBrownBats
                global totalColoredBats
                totalColoredBats = 0.00
                totalBlackBats = 0.00
                totalBrownBats = 0.00
                totalRedBats = 0.00
                if lines[1][5] == "":
                    lines[1][5] = 'Black'
                if lines[2][5] == "":
                    lines[2][5] = 'Brown'
                if lines[3][5] == "":
                    lines[3][5] = 'Red'
                try:
                    for i in range(len(lines)):

                        if totalColoredBats > 2:
                            percentageBlackBats = float(totalBlackBats / totalColoredBats)
                            percentageBrownBats = float(totalBrownBats / totalColoredBats)
                            percentageRedBats = float(totalRedBats / totalColoredBats)

                            blackBatScore = 0.6 - percentageBlackBats
                            brownBatScore = 0.3 - percentageBrownBats
                            redBatScore = 0.1 - percentageRedBats

                            # see if list is empty and add value
                            try:
                                if lines[i][5] == "":
                                    if (blackBatScore > brownBatScore) and (blackBatScore > redBatScore):
                                        lines[i][5] = 'Black'
                                    if (blackBatScore > brownBatScore) and (blackBatScore == redBatScore):
                                        lines[i][5] = 'Black'
                                    if (brownBatScore > blackBatScore) and (brownBatScore > redBatScore):
                                        lines[i][5] = 'Brown'
                                    if (brownBatScore > blackBatScore) and (brownBatScore == redBatScore):
                                        lines[i][5] = 'Brown'
                                    if (redBatScore > blackBatScore) and (redBatScore > brownBatScore):
                                        lines[i][5] = 'Red'
                                    if (redBatScore > blackBatScore) and (redBatScore == brownBatScore):
                                        lines[i][5] = 'Red'
                                    if (blackBatScore == brownBatScore) and (brownBatScore == redBatScore):
                                        lines[i][5] = 'Black'
                            except Exception, e:
                                print "could not decide bat color"
                                print(str(e))

                        # check for which bat to add next
                        if lines[i][5] == 'Black':
                            totalBlackBats = totalBlackBats + 1
                        if lines[i][5] == 'Brown':
                            totalBrownBats = totalBrownBats + 1
                        if lines[i][5] == 'Red':
                            totalRedBats = totalRedBats + 1
                        totalColoredBats = totalBlackBats + totalBrownBats + totalRedBats

                except IndexError:
                    pass
                except Exception, e:
                    print "could not add bat color"
                    print (str(e))

                # Check if subscriber or not.
                subscribers()
                for i1 in range(len(lines)):
                    for i2 in range(len(subscriberResponse['subscriptions'])):
                        if lines[i1][0] == subscriberResponse['subscriptions'][i2]['user']['display_name']:
                            lines[i1][6] = 1
                        if not lines[i1][0] == subscriberResponse['subscriptions'][i2]['user']['display_name']:
                            if not lines[i1][6] == "IsSubscriber":
                                lines[i1][6] = 0

                # After all the editing has been done write back all the lines
                # I had to write back to a new file and rename it because of lack of memory

                if not os.path.exists('followerDataNew.csv'):
                    open('followerDataNew.csv', "w+").close()
                with open('followerDataNew.csv', "wb") as csvfile:
                    followerDataWriter = csv.writer(csvfile, delimiter=",")
                    followerDataWriter.writerows(lines)
                os.remove('followerData.csv')
                os.rename('followerDataNew.csv', 'followerData.csv')

                # open the subsciber file to get the lines to the Sub file
                if not os.path.exists('subscriberData.csv'):
                    open('subscriberData.csv', "w+").close()
                with open('subscriberData.csv', "rb") as csvfile:
                    subscriberDataReader = csv.reader(csvfile, delimiter=",")
                    subscriberLines = list(subscriberDataReader)



                # write back any changes to a the subscriber file
                with open('subscriberDataNew.csv', "wb") as csvfile:
                    subscriberDataWriter = csv.writer(csvfile, delimiter=",")
                    subscriberDataWriter.writerows(subscriberLines)
                os.remove('subscriberData.csv')
                os.rename('subscriberDataNew.csv', 'subscriberData.csv')

            except IndexError:
                pass
            except Exception, e:
                print("while true events error")
                print(str(e))
        if response == "PING :tmi.twitch.tv\r\n":
            try:
                s.send("PONG :tmi.twitch.tv\r\n".encode("utf-8"))
            except IndexError:
                 pass
        if "!commands" in data.lower().split()[3]:
            try:
                message("See what the bot can do here: https://github.com/ridgure/twitchbot#features")
            except IndexError:
                pass
        if "!test" in data.lower().split()[3]:
            try:
                message(subscribers())
            except IndexError:
                pass
            except Exception, e:
                message("Division failed")
                message(str(e))
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
        if "!bat" in data.lower().split()[3]:
            try:
                batInfo = None
                if data.lower().split()[4]:
                    for i in range(len(lines)):
                        if lines[i][0].lower() == data.lower().split()[4]:
                            batInfo = lines[i]
                    if batInfo == None:
                        message("User is not following the channel")
                    if batInfo[4] == 'Male':
                        gender = 'He'
                    if batInfo[4] == 'Female':
                        gender = 'She'
                    message(data.split()[4] + "'s bat is called " + batInfo[3] + ". " + gender + " is colored " + batInfo[5].lower())
                if not data.lower().split()[4]:
                    for i in range(len(lines)):
                        if lines[i][0] == sender():
                            batInfo = lines[i]
                    if batInfo[4] == 'Male':
                        gender = 'He'
                    if batInfo[4] == 'Female':
                        gender = 'She'
                    message("Your bat is called " + batInfo[3] + ". " + gender + " is colored " + batInfo[5].lower())
            except IndexError:
                pass
            except Exception, e:
                pass
        if "!raid" in data.lower().split()[3]:
            try:
                if sender().lower() == Channel[1:]:
                    message("Please raid Twitch.tv/" + data.split()[4] + " msg: Ridgure raid twitchRaid twitchRaid twitchRaid")
                else:
                    pass
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
                if sender() == 'pupgirl22':
                    message(sender() + " licks " + data.split()[4] + lick())
                else:
                    pass
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
        if "!namechange" in data.lower().split()[3]:
            try:
                with open('followerData.csv', "rb") as csvfile:
                    followerDataReader = csv.reader(csvfile, delimiter=",")
                    lines = list(followerDataReader)

                for i in range(len(lines)):
                    if lines[i][0] == sender():
                        lines[i][3] = data.split(4)
                        message("Successfully changed the name of " + sender() + "'s bat to: " + data.split()[4])


                with open('followerDataNew.csv', "wb") as csvfile:
                    followerDataWriter = csv.writer(csvfile, delimiter=",")
                    followerDataWriter.writerows(lines)
                os.remove('followerData.csv')
                os.rename('followerDataNew.csv', 'followerData.csv')

            except IndexError:
                pass
        if "!timemeout" in data.lower().split()[3]:
            try:
                ## time out KBiglair ##
                if 0 < int(data.split()[4]) < 3601:
                    message("/timeout " + sender() + " " + data.split()[4])
                    message("Timed out " + sender() + " for " + data.split()[4] + " seconds")
                elif int(data.split()[4]) < 0:
                    message("You cannot go back in time unless you are the doctor or Marty McFly")
                else:
                    message("TimeMeOut failed")
            except IndexError:
                message("Add amount of seconds you want to be timed out after command")
                pass
        if "!uptime" in data.lower().split()[3]:
            try:
                message(uptime())
            except IndexError:
                print "Uptime failed"
        if "!fc" in data.lower().split()[3]:
            try:
                # get the user
                if len(data.lower().split()) == 4:
                    user = sender()
                if len(data.lower().split()) == 5:
                    user = (data.lower().split()[4])

                testFollower = False
                # get user index and get their follow time and date and length
                for i1 in xrange(len(followerList)):
                    for i2 in xrange(len(followerList[i1])):
                        # print i1, followerList[i1]['from_name']
                        if followerList[i1]['from_name'].lower() == user:
                            followAge = followAgeAll()
                            message("Last follow was on: " + str(
                                followAge[i1][6]) + " GMT-0 and has been following the channel for " + str(
                                followAge[i1][1]) + " days, " + str(followAge[i1][2]) + " hours, " + str(
                                followAge[i1][3]) + " minutes and " + str(followAge[i1][4]) + " seconds")
                            user = None
                            testFollower = True
                        else:
                            pass
                if testFollower == False:
                    message("User is not following the channel")

            except IndexError:
                pass
            except Exception, e:
                message("followage failed")
                message(str(e))
        if "!smile" in data.lower().split()[3]:
            try:
                message(sender() + " smiles at " + data.split()[4] + " " + randomEmote())
            except IndexError:
                message("Remember to smile at someone!")
            except Exception, e:
                message("Smile failed")
                message(str(e))
        if "!multiply" in data.lower().split()[3]:
            try:
                message(multiply())
            except IndexError:
                pass
            except Exception, e:
                message("Multiplication failed")
                message(str(e))
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
            try:
                f = open("output.txt", "a")
                f.write(username + ": " + message)
                f.close()
                f = open("output.txt", "r")
                lines = f.readlines()
                f.close()
                f = open("output.txt", "w")
                displayedLines = 20
                if len(lines) > displayedLines:
                    backlog = len(lines) - displayedLines
                    f.truncate()
                    f.writelines(lines[backlog:len(lines)])
                    f.close()
                else:
                    f.writelines(lines)
                    f.close()
            except:
                pass
            print(username + ": " + message)
###            print response
            sleep(0.1)
    except IndexError:
        pass
    except Exception, e:
        print "An error just occurred"
        print str(e)
