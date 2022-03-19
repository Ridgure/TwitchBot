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
import tinyurl
from names import *
from config import *
from time import sleep
from decimal import *

s = socket.socket()
s.connect((Host, Port))
s.send("PASS {}\r\n".format("oauth:" + FollowerToken).encode("utf-8"))
s.send("NICK {}\r\n".format(Nickname.lower()).encode("utf-8"))
s.send("JOIN {}\r\n".format(Channel).encode("utf-8"))
s.send("CAP REQ :twitch.tv/membership\r\n")
s.send("CAP REQ :twitch.tv/commands\r\n")
s.send("CAP REQ :twitch.tv/tags\r\n")
BugMessages = 5


def randomEmote():
    randomNumber = random.randint(0, len(emotes))
    randomEmote = emotes[randomNumber]
    return randomEmote


def add():
    test = text.split()[1:]
    makingNumbers = [int(i) for i in test]
    addingNumbers = sum(makingNumbers)
    everythingTogether = ' + '.join(map(str, makingNumbers)) + ' = ' + str(addingNumbers)
    return everythingTogether


def multiply():
    test = text.split()[1:]
    makingNumbers = [int(i) for i in test]
    total = 1
    for x in makingNumbers:
        total *= x
    everythingTogether = ' * '.join(map(str, makingNumbers)) + ' = ' + str(total)
    return everythingTogether


def divide():
    test = text.split()[1:]
    makingNumbers = [int(i) for i in test]
    total = makingNumbers[0]
    for x in makingNumbers[1:]:
        total /= x
    everythingTogether = ' / '.join(map(str, makingNumbers)) + ' = ' + str(total)
    return everythingTogether


def bugCounter():
    global BugMessages
    BugMessages = BugMessages + 1


def lick():
    over = " over and "
    randomNumber = random.randint(1, 30)
    licks = over * randomNumber + "over again (x" + str(randomNumber) + ")"
    return licks


def mess():
    randomNumber = random.randint(0, len(messes))
    return messes[randomNumber]

# def token():
#     url = "https://id.twitch.tv/oauth2/token?client_id=" + ClientID + "&client_secret=" + ClientSecret + "&grant_type=client_credentials"
#     response = requests.post(url)
#     tokenResponse = response.json()
#     if response.status_code == 404:
#         print "error"
#     if response.status_code == 400:
#         print ("Bad request")
#     if response.status_code == 429:
#         print "Too many subscriber requests"
#     tokenResponse = response.json()


def subscribers():
    url = "https://api.twitch.tv/helix/subscriptions?broadcaster_id=" + User_ID_ridgure
    params = {"Accept": "application/vnd.twitchtv.v5+json", "Client-ID": ClientID, "Authorization": "Bearer " + SubscriberToken,
              "limit": "100"}
    response = requests.get(url, headers=params, allow_redirects=True)
    if response.status_code == 400:
        print ("Bad request")
    if response.status_code == 429:
        print ("Too many subscriber requests")
    global subscriberResponse
    subscriberResponse = response.json()
    return subscriberResponse

    # Kraken V5 returns
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

    # Helix Returns
    # {u'total': 12,
    # u'pagination': {u'cursor': u'eyJiIjp7IkN1cnNvciI6ImV5SkpkR1Z0U1VRdFUzUmhjblJ6UVhRdFNVUWlPbnNpUWlJNmJuVnNiQ3dpUWs5UFRDSTZiblZzYkN3aVFsTWlPbTUxYkd3c0lrd2lPbTUxYkd3c0lrMGlPbTUxYkd3c0lrNGlPbTUxYkd3c0lrNVRJanB1ZFd4c0xDSk9WVXhNSWpwdWRXeHNMQ0pUSWpvaU1EQXdNREF3TURBd01Ua3lOREEzTFRJd01UY3RNRFl0TWpoVU1UazZNak02TkRSYUxUQXdNREF3TURBeU1qY3lNekUwT1NJc0lsTlRJanB1ZFd4c2ZTd2lTWFJsYlU5M2JtVnlTVVFpT25zaVFpSTZiblZzYkN3aVFrOVBUQ0k2Ym5Wc2JDd2lRbE1pT201MWJHd3NJa3dpT201MWJHd3NJazBpT201MWJHd3NJazRpT201MWJHd3NJazVUSWpwdWRXeHNMQ0pPVlV4TUlqcHVkV3hzTENKVElqb2lNVEEyTlRnMk16UTVJaXdpVTFNaU9tNTFiR3g5TENKSmRHVnRUM2R1WlhKSlJDMUpkR1Z0U1VRdFUzUmhjblJ6UVhRdFNVUWlPbnNpUWlJNmJuVnNiQ3dpUWs5UFRDSTZiblZzYkN3aVFsTWlPbTUxYkd3c0lrd2lPbTUxYkd3c0lrMGlPbTUxYkd3c0lrNGlPbTUxYkd3c0lrNVRJanB1ZFd4c0xDSk9WVXhNSWpwdWRXeHNMQ0pUSWpvaU1EQXdNREF3TVRBMk5UZzJNelE1TFRBd01EQXdNREF3TURFNU1qUXdOeTB5TURFM0xUQTJMVEk0VkRFNU9qSXpPalEwV2kwd01EQXdNREF3TWpJM01qTXhORGtpTENKVFV5STZiblZzYkgwc0lrOTNibVZ5U1VRaU9uc2lRaUk2Ym5Wc2JDd2lRazlQVENJNmJuVnNiQ3dpUWxNaU9tNTFiR3dzSWt3aU9tNTFiR3dzSWswaU9tNTFiR3dzSWs0aU9tNTFiR3dzSWs1VElqcHVkV3hzTENKT1ZVeE1JanB1ZFd4c0xDSlRJam9pTXpJMk56QTBNallpTENKVFV5STZiblZzYkgxOSJ9LCJhIjp7IkN1cnNvciI6ImV5SkpkR1Z0U1VRdFUzUmhjblJ6UVhRdFNVUWlPbnNpUWlJNmJuVnNiQ3dpUWs5UFRDSTZiblZzYkN3aVFsTWlPbTUxYkd3c0lrd2lPbTUxYkd3c0lrMGlPbTUxYkd3c0lrNGlPbTUxYkd3c0lrNVRJanB1ZFd4c0xDSk9WVXhNSWpwdWRXeHNMQ0pUSWpvaU1EQXdNREF3TURBd01Ua3lOREE1TFRJd01UY3RNRFl0TWpoVU1qQTZNVEU2TkRWYUxUQXdNREF3TURBeU1qYzFNekV6TWlJc0lsTlRJanB1ZFd4c2ZTd2lTWFJsYlU5M2JtVnlTVVFpT25zaVFpSTZiblZzYkN3aVFrOVBUQ0k2Ym5Wc2JDd2lRbE1pT201MWJHd3NJa3dpT201MWJHd3NJazBpT201MWJHd3NJazRpT201MWJHd3NJazVUSWpwdWRXeHNMQ0pPVlV4TUlqcHVkV3hzTENKVElqb2lNVEEyTlRnMk16UTVJaXdpVTFNaU9tNTFiR3g5TENKSmRHVnRUM2R1WlhKSlJDMUpkR1Z0U1VRdFUzUmhjblJ6UVhRdFNVUWlPbnNpUWlJNmJuVnNiQ3dpUWs5UFRDSTZiblZzYkN3aVFsTWlPbTUxYkd3c0lrd2lPbTUxYkd3c0lrMGlPbTUxYkd3c0lrNGlPbTUxYkd3c0lrNVRJanB1ZFd4c0xDSk9WVXhNSWpwdWRXeHNMQ0pUSWpvaU1EQXdNREF3TVRBMk5UZzJNelE1TFRBd01EQXdNREF3TURFNU1qUXdPUzB5TURFM0xUQTJMVEk0VkRJd09qRXhPalExV2kwd01EQXdNREF3TWpJM05UTXhNeklpTENKVFV5STZiblZzYkgwc0lrOTNibVZ5U1VRaU9uc2lRaUk2Ym5Wc2JDd2lRazlQVENJNmJuVnNiQ3dpUWxNaU9tNTFiR3dzSWt3aU9tNTFiR3dzSWswaU9tNTFiR3dzSWs0aU9tNTFiR3dzSWs1VElqcHVkV3hzTENKT1ZVeE1JanB1ZFd4c0xDSlRJam9pTVRBMk5UZzJNelE1SWl3aVUxTWlPbTUxYkd4OWZRPT0ifX0'},
    # u'points': 12,
    # u'data': [
    #       {u'is_gift': False, u'gifter_id': u'', u'gifter_login': u'', u'broadcaster_id': u'106586349', u'gifter_name': u'', u'broadcaster_name': u'Ridgure', u'broadcaster_login': u'ridgure', u'tier': u'1000', u'user_id': u'32670426', u'user_login': u'lilgamerhelle', u'plan_name': u'Channel Subscription (ridgure)', u'user_name': u'LilGamerHelle'},
    #       {u'is_gift': False, u'gifter_id': u'', u'gifter_login': u'', u'broadcaster_id': u'106586349', u'gifter_name': u'', u'broadcaster_name': u'Ridgure', u'broadcaster_login': u'ridgure', u'tier': u'1000', u'user_id': u'127021182', u'user_login': u'bugmacgregor', u'plan_name': u'Channel Subscription (ridgure)', u'user_name': u'BugMacgregor'},
    #       {u'is_gift': False, u'gifter_id': u'', u'gifter_login': u'', u'broadcaster_id': u'106586349', u'gifter_name': u'', u'broadcaster_name': u'Ridgure', u'broadcaster_login': u'ridgure', u'tier': u'1000', u'user_id': u'142573858', u'user_login': u'obscurenorwegiangamer', u'plan_name': u'Channel Subscription (ridgure)', u'user_name': u'ObscureNorwegianGamer'},
    #       {u'is_gift': True, u'gifter_id': u'142573858', u'gifter_login': u'obscurenorwegiangamer', u'broadcaster_id': u'106586349', u'gifter_name': u'ObscureNorwegianGamer', u'broadcaster_name': u'Ridgure', u'broadcaster_login': u'ridgure', u'tier': u'1000', u'user_id': u'532293037', u'user_login': u'drageno01', u'plan_name': u'Channel Subscription (ridgure)', u'user_name': u'DRAGEno01'},
    #       {u'is_gift': True, u'gifter_id': u'142573858', u'gifter_login': u'obscurenorwegiangamer', u'broadcaster_id': u'106586349', u'gifter_name': u'ObscureNorwegianGamer', u'broadcaster_name': u'Ridgure', u'broadcaster_login': u'ridgure', u'tier': u'1000', u'user_id': u'161023431', u'user_login': u'implied_slight', u'plan_name': u'Channel Subscription (ridgure)', u'user_name': u'Implied_Slight'},
    #       {u'is_gift': True, u'gifter_id': u'142573858', u'gifter_login': u'obscurenorwegiangamer', u'broadcaster_id': u'106586349', u'gifter_name': u'ObscureNorwegianGamer', u'broadcaster_name': u'Ridgure', u'broadcaster_login': u'ridgure', u'tier': u'1000', u'user_id': u'139849169', u'user_login': u'quirkygeek17', u'plan_name': u'Channel Subscription (ridgure)', u'user_name': u'QuirkyGeek17'},
    #       {u'is_gift': True, u'gifter_id': u'142573858', u'gifter_login': u'obscurenorwegiangamer', u'broadcaster_id': u'106586349', u'gifter_name': u'ObscureNorwegianGamer', u'broadcaster_name': u'Ridgure', u'broadcaster_login': u'ridgure', u'tier': u'1000', u'user_id': u'114849229', u'user_login': u'tarillthemad', u'plan_name': u'Channel Subscription (ridgure)', u'user_name': u'TarilltheMad'},
    #       {u'is_gift': True, u'gifter_id': u'142573858', u'gifter_login': u'obscurenorwegiangamer', u'broadcaster_id': u'106586349', u'gifter_name': u'ObscureNorwegianGamer', u'broadcaster_name': u'Ridgure', u'broadcaster_login': u'ridgure', u'tier': u'1000', u'user_id': u'47576890', u'user_login': u'skysunna', u'plan_name': u'Channel Subscription (ridgure)', u'user_name': u'Skysunna'},
    #       {u'is_gift': True, u'gifter_id': u'127021182', u'gifter_login': u'bugmacgregor', u'broadcaster_id': u'106586349', u'gifter_name': u'BugMacgregor', u'broadcaster_name': u'Ridgure', u'broadcaster_login': u'ridgure', u'tier': u'1000', u'user_id': u'60748299', u'user_login': u'lukestergaming', u'plan_name': u'Channel Subscription (ridgure)', u'user_name': u'LukesterGaming'},
    #       {u'is_gift': True, u'gifter_id': u'127021182', u'gifter_login': u'bugmacgregor', u'broadcaster_id': u'106586349', u'gifter_name': u'BugMacgregor', u'broadcaster_name': u'Ridgure', u'broadcaster_login': u'ridgure', u'tier': u'1000', u'user_id': u'89499670', u'user_login': u'ivanabcroftin', u'plan_name': u'Channel Subscription (ridgure)', u'user_name': u'IvanaBCroftin'},
    #       {u'is_gift': False, u'gifter_id': u'', u'gifter_login': u'', u'broadcaster_id': u'106586349', u'gifter_name': u'', u'broadcaster_name': u'Ridgure', u'broadcaster_login': u'ridgure', u'tier': u'1000', u'user_id': u'44974162', u'user_login': u'sailorscoutlua', u'plan_name': u'Channel Subscription (ridgure)', u'user_name': u'sailorscoutlua'},
    #       {u'is_gift': True, u'gifter_id': u'279385205', u'gifter_login': u'erawyn_', u'broadcaster_id': u'106586349', u'gifter_name': u'Erawyn_', u'broadcaster_name': u'Ridgure', u'broadcaster_login': u'ridgure', u'tier': u'1000', u'user_id': u'109949586', u'user_login': u'riboture', u'plan_name': u'Channel Subscription (ridgure)', u'user_name': u'Riboture'},
    #       {u'is_gift': False, u'gifter_id': u'', u'gifter_login': u'', u'broadcaster_id': u'106586349', u'gifter_name': u'', u'broadcaster_name': u'Ridgure', u'broadcaster_login': u'ridgure', u'tier': u'3000', u'user_id': u'106586349', u'user_login': u'ridgure', u'plan_name': u'Channel Subscription (ridgure): $24.99 Sub', u'user_name': u'Ridgure'}]}


def channelInfo():
    url = "https://api.twitch.tv/helix/channels?broadcaster_id=" + User_ID_ridgure
    params = {"Client-ID" : ""+ ClientID +"", "Authorization": "Bearer " + FollowerToken, "Accept": "application/vnd.twitchtv.v5+json"}
    response = requests.get(url, headers=params)
    if response.status_code == 400:
        print ("Bad request")
    if response.status_code == 429:
        print ("Too many stream info requests")
    channelInfoResponse = response.json()
    return channelInfoResponse

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

def followers():
    try:
        url100 = "https://api.twitch.tv/helix/users/follows?to_id=" + User_ID_ridgure + "&first=100"
        params = {"Client-ID": "" + ClientID + "", "Authorization": "Bearer " + FollowerToken}
        response = requests.get(url100, headers=params)
        responseFirst100 = response.json()
        if response.status_code == 400:
            print ("Bad request")
        if response.status_code == 429:
            print ("Too many follower requests")

        global pagination
        pagination = responseFirst100['pagination']['cursor']
        totalFollowers = responseFirst100['total']
        global followerList
        followerList = responseFirst100['data']

        # making a list of all the followers
        for i9 in xrange(int(math.ceil(totalFollowers / float(100))) - 1):
            try:
                url200 = "https://api.twitch.tv/helix/users/follows?to_id=" + User_ID_ridgure + "&first=100&after=" + pagination
                params = {"Client-ID": "" + ClientID + "", "Authorization": "Bearer " + FollowerToken}
                response = requests.get(url200, headers=params)
                responseRest = response.json()
                if response.status_code == 400:
                    print ("Bad request")
                if response.status_code == 429:
                    print ("Too many follower requests")
                pagination = responseRest['pagination']['cursor']
                followerList = followerList + responseRest['data']
            except Exception as e:
                if str(e) == "'cursor'":
                    pass
                else:
                    print (str(e))
                    pass

        return followerList
    except Exception as e:
        print (str(e))
        pass

    # print response
    # Kraken returns
    # {u'pagination': {u'cursor': u'eyJiIjpudWxsLCJhIjoiMTUxNDI1NDE4NzA4NTAyMDAwMCJ9'},
    # u'total': 421,
    # u'data': [
        # {u'to_id': u'106586349', u'followed_at': u'2018-01-18T20:11:57Z', u'from_id': u'163393705'},
        # {u'to_id': u'106586349', u'followed_at': u'2018-01-18T06:41:48Z', u'from_id': u'46728242'},

    # Helix returns
    # {u'pagination': {u'cursor': u'eyJiIjpudWxsLCJhIjp7IkN1cnNvciI6ImV5SjBjQ0k2SW5WelpYSTZNVFl4TURJek5ETXhPbVp2Ykd4dmQzTWlMQ0owY3lJNkluVnpaWEk2TVRBMk5UZzJNelE1SWl3aWFYQWlPaUoxYzJWeU9qRXdOalU0TmpNME9UcG1iMnhzYjNkbFpGOWllU0lzSW1seklqb2lNVFl3TmpVNU1qRTJORE0yTmprek5EVXpPU0o5In19'},
    # u'total': 1484,
    # u'data': [
        # {u'from_name': u'fritoy911', u'to_login': u'ridgure', u'followed_at': u'2021-11-08T11:00:59Z', u'to_id': u'106586349', u'to_name': u'Ridgure', u'from_login': u'fritoy911', u'from_id': u'123985105'},
        # {u'from_name': u'AgentDaxon', u'to_login': u'ridgure', u'followed_at': u'2021-11-08T08:49:35Z', u'to_id': u'106586349', u'to_name': u'Ridgure', u'from_login': u'agentdaxon', u'from_id': u'45366409'},
        # {u'from_name': u'FloodedVoyage45', u'to_login': u'ridgure', u'followed_at': u'2021-11-06T22:29:22Z', u'to_id': u'106586349', u'to_name': u'Ridgure', u'from_login': u'floodedvoyage45', u'from_id': u'587906627'},
        # {u'from_name': u'SgtLegoTown', u'to_login': u'ridgure', u'followed_at': u'2021-11-06T16:45:57Z', u'to_id': u'106586349', u'to_name': u'Ridgure', u'from_login': u'sgtlegotown', u'from_id': u'210387514'}


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
        followDateTime = datetime.datetime.combine(followDate,
                                                   datetime.time(int(followHour), int(followMinute), int(followSecond),
                                                                 0, tzinfo=None))
        currentDate = datetime.date(int(currentYear), int(currentMonth), int(currentDay))
        currentDateTime = datetime.datetime.combine(currentDate,
                                                    datetime.time(int(currentHour), int(currentMinute), int(currentDay),
                                                                  0, tzinfo=None))
        deltaDate = currentDateTime - followDateTime
        deltaHours = int(math.floor(deltaDate.seconds / 3600))
        deltaMinutes = int(math.floor((deltaDate.seconds - (deltaHours * 3600)) / 60))
        deltaSeconds = int(deltaDate.seconds - (deltaHours * 3600) - (deltaMinutes * 60))
        secondsFollowed = (deltaSeconds + deltaMinutes * 60 + deltaHours * 3600 + deltaDate.days * 86400)

        # Return array
        followAgeList[i].insert(0, str(deltaDate))
        followAgeList[i].insert(1, deltaDate.days)
        followAgeList[i].insert(2, deltaHours)
        followAgeList[i].insert(3, deltaMinutes)
        followAgeList[i].insert(4, deltaSeconds)
        followAgeList[i].insert(5, secondsFollowed)
        followAgeList[i].insert(6, followDateTime)

    return followAgeList


def months_between(date1, date2):
    if date1 > date2:
        date1, date2 = date2, date1
    m1 = date1.year * 12 + date1.month
    m2 = date2.year * 12 + date2.month
    months = m2 - m1
    if date1.day > date2.day:
        months -= 1
    elif date1.day == date2.day:
        seconds1 = date1.hour * 3600 + date1.minute + date1.second
        seconds2 = date2.hour * 3600 + date2.minute + date2.second
        if seconds1 > seconds2:
            months -= 1
    return months


# date1 = dt.datetime.strptime('2011-08-15 12:00:00', '%Y-%m-%d %H:%M:%S')
# date2 = dt.datetime.strptime('2012-02-15', '%Y-%m-%d')
# print(months_between(date1,date2))


def subscribeAgeAll():
    global subscribeAgeList
    subscribeAgeList = [[] for i in range(len(subscriberResponse['data']))]

    for i in xrange(len(subscriberResponse['data'])):
        # Get subscribe Day Month Year
        m = re.search('(.+?)T', subscriberResponse['data'][i]['created_at'])
        subscribeDate = m.group(1).encode('ascii', 'ignore')
        m = re.search('(.+?)-', subscribeDate)
        subscribeYear = m.group(1).encode('ascii', 'ignore')
        m = re.search('-(.+?)-', subscribeDate)
        subscribeMonth = m.group(1).encode('ascii', 'ignore')
        m = re.search('-(.*)', subscribeDate)
        subscribeDay = m.group(1).encode('ascii', 'ignore')
        m = re.search('-(.*)', subscribeDay)
        subscribeDay = m.group(1).encode('ascii', 'ignore')

        # Get subscribe Hour Minute Second
        m = re.search('T(.+?)Z', subscriberResponse['data'][i]['created_at'])
        subscribeTime = m.group(1).encode('ascii', 'ignore')
        m = re.search('(.+?):', subscribeTime)
        subscribeHour = m.group(1).encode('ascii', 'ignore')
        m = re.search(':(.+?):', subscribeTime)
        subscribeMinute = m.group(1).encode('ascii', 'ignore')
        m = re.search(':(.*)', subscribeTime)
        subscribeSecond = m.group(1).encode('ascii', 'ignore')
        m = re.search(':(.*)', subscribeSecond)
        subscribeSecond = m.group(1).encode('ascii', 'ignore')

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

        # Compare subscribe with current
        subscribeDate = datetime.date(int(subscribeYear), int(subscribeMonth), int(subscribeDay))
        subscribeDateTime = datetime.datetime.combine(subscribeDate,
                                                      datetime.time(int(subscribeHour), int(subscribeMinute),
                                                                    int(subscribeSecond), 0, tzinfo=None))
        currentDate = datetime.date(int(currentYear), int(currentMonth), int(currentDay))
        currentDateTime = datetime.datetime.combine(currentDate,
                                                    datetime.time(int(currentHour), int(currentMinute), int(currentDay),
                                                                  0, tzinfo=None))
        deltaDate = currentDateTime - subscribeDateTime
        deltaHours = int(math.floor(deltaDate.seconds / 3600))
        deltaMinutes = int(math.floor((deltaDate.seconds - (deltaHours * 3600)) / 60))
        deltaSeconds = int(deltaDate.seconds - (deltaHours * 3600) - (deltaMinutes * 60))

        # Return array
        subscribeAgeList[i].insert(0, str(deltaDate))
        subscribeAgeList[i].insert(1, deltaDate.days)
        subscribeAgeList[i].insert(2, deltaHours)
        subscribeAgeList[i].insert(3, deltaMinutes)
        subscribeAgeList[i].insert(4, deltaSeconds)
        subscribeAgeList[i].insert(5, deltaDate.seconds)
        subscribeAgeList[i].insert(6, subscribeDateTime)

        date1 = datetime.datetime.strptime(
            str(subscribeYear) + "-" + str(subscribeMonth) + "-" + str(subscribeDay) + " " + str(
                subscribeHour) + ":" + str(subscribeMinute) + ":" + str(subscribeSecond), '%Y-%m-%d %H:%M:%S')
        date2 = datetime.datetime.strptime(
            str(currentYear) + "-" + str(currentMonth) + "-" + str(currentDay) + " " + str(currentHour) + ":" + str(
                currentMinute) + ":" + str(currentSecond), '%Y-%m-%d %H:%M:%S')
        subscribeAgeList[i].append(months_between(date1, date2))
        subscribeAgeList[i].append(subscriberResponse['data'][i]['user_name'])
    return subscribeAgeList


def uptime():
    try:
        url = "https://api.twitch.tv/helix/streams?user_id=" + User_ID_ridgure #from the config file
        params = {"Client-ID": "" + ClientID + "", "Authorization": "Bearer " + FollowerToken}
        response = requests.get(url, headers=params)
        streamData = response.json()
        if response.status_code == 400:
            print ("Bad request")
        if response.status_code == 429:
            print ("Too many uptime requests")
        if streamData['data'] == []:
            message("Twitch has not realized stream is live")
        StreamStart = streamData['data'][0]

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
        totalUptimeMinutes = int(totalFinishMinutes) - int(totalStartMinutes) + (delta.days * 24 * 60)
        uptimeHours = int(math.floor(totalUptimeMinutes / 60))
        uptimeMinutes = totalUptimeMinutes - (uptimeHours * 60)
        return datetime.time(uptimeHours, uptimeMinutes, 0)
    except Exception as e:
        print (str(e))
        pass


def message(msg):
    try:
        if len(msg) > 450:
            s.send("PRIVMSG " + Channel + " :" + msg[0:450] + "\n")
            s.send("PRIVMSG " + Channel + " :" + msg[450:900] + "\n")
            s.send("PRIVMSG " + Channel + " :" + msg[900:1350] + "\n")
            print (Nickname + ": " + msg[0:447])
            print (Nickname + ": " + msg[450:900])
            print (Nickname + ": " + msg[900:1350])
        else:
            s.send("PRIVMSG " + Channel + " :" + msg + "\n")
            print (Nickname + ": " + msg)
            sleep(30/100)
    except IndexError:
        pass

broadcaster = Channel[1:]

while True:
    try:
        response = s.recv(1024).decode("utf-8")
        data = response.strip("\r\n")
        if "PRIVMSG" in data:
            username = re.search(r'(?<=display-name=)\w+', response).group(0)
            text = re.search(r'(?<=PRIVMSG)\W+\w+\s\:(.*)', response).group(1)
            print(username + ": " + text)
            badges = re.search(r'(?:badges=)(.*?);', response).group(1).encode("utf-8").split(",")
            print ("Badges: " + str(badges[:]))
            print ("Response: " + response)  ### These are all the responses that are not message related
            try:
                # Timeout misbehaving users
                if not "clips.twitch.tv/" in text.lower():
                    if not username.lower().rstrip() == broadcaster:
                        for i1 in range(len(badges)):
                            if badges[i1] == 'moderator/1':
                                break
                            if badges[i1] == 'vip/1':
                                break
                            if "/" in text.lower().encode('ascii'):
                                if "." in text.lower().encode('ascii'):
                                    for i2 in topLevelDomains:  # Found in names.py
                                        if i2 in text.lower().encode('ascii', 'ignore'):
                                            try:
                                                message("/timeout " + username + " 1")
                                                print ("Timed out " + username + " for 1 second because of " + i2)
                                                break
                                            except IndexError, e:
                                                print str(e)
                                                pass
                            for i3 in timeout1:
                                if i3 in text.lower().encode('ascii', 'ignore'):
                                    try:
                                        message("/timeout " + username + " 1")
                                        print ("Timed out " + username + " for 1 second because of " + i3)
                                        break
                                    except IndexError, e:
                                        print str(e)
                                        pass
                            # for i6 in disney:
                            #     if i6 in text.lower().encode('ascii', 'ignore'):
                            #         try:
                            #             message("/timeout " + username + " 1")
                            #             print ("Timed out " + username + " for 1 second because of " + i6)
                            #         except IndexError as e:
                            #             print (str(e))
                            #             pass
                            for i4 in timeout10:
                                if i4 in text.lower().encode('ascii', 'ignore'):
                                    try:
                                        message("/timeout " + username + " 600")
                                        print "Timed out " + username + " for 10 minutes because of " + i4
                                        break
                                    except IndexError as e:
                                        print (str(e))
                                        pass
                            for i7 in timeout4Hours:
                                if i7 in text.lower().encode('ascii', 'ignore'):
                                    try:
                                        message("/timeout " + username + " 1440")
                                        print "Timed out " + username + " for 24 hours because of " + i7
                                        break
                                    except IndexError as e:
                                        print (str(e))
                                        pass
                        for i5 in banReasons:
                            if i5 in text.lower().encode('ascii', 'ignore'):
                                try:
                                    message("/ban " + username)
                                    print "Banned " + username + " because of " + i5
                                    break
                                except IndexError as e:
                                    print str(e)
                                    pass

                # Ban people posting sensitive information about going to a certain school
                try:
                    banreason = re.search(r'(?:\w+\W+){1,3}?\bWent to\W+(?:\w+\W+){1,2}?High\b', text).group(0)
                    if banreason.lower() in text.lower():
                        message("/ban " + username)
                        print username + " has been banned"
                except:
                    pass

                # Get new follower list and format it to compare with unfollowers
                followers()

                test = []
                for i in range(len(followerList)):
                    test.insert(0, followerList[i]['from_name'].encode('ascii', 'ignore'))
                test = map(str.strip, test)

                # Get existing follower list
                if not os.path.exists('followerData.csv'):
                    open('followerData.csv', "w+").close()
                csvfile = open('followerData.csv', "rb")
                followerDataReader = csv.reader(csvfile, delimiter=",")
                followerLines = list(followerDataReader)
                csvfile.close()

                # Compare follower lists
                newFollowers = [item for item in test if item not in [i[0] for i in followerLines[1:]]]
                unfollowers = [item for item in [i[0] for i in followerLines[1:]] if item not in test]

                # thank new follower and add to existing list
                if len(newFollowers) > 0:
                    if len(followerLines) == 0:
                        followerLines.append(
                            ["Username", "FollowLength", "IsFollower", "BatName", "BatGender", "BatColor",
                             "IsSubscriber"])
                        followerLines.append(
                            [Channel[1:], "0", "1", "", "", "", ""])
                    for i in range(len(newFollowers)):
                        followerLines.append([newFollowers[i], "", "", "", "", "", ""])
                    csvfile = open('followerDataNew.csv', "wb")
                    followerDataWriter = csv.writer(csvfile, delimiter=",")
                    followerDataWriter.writerows(followerLines)
                    csvfile.close()
                    os.remove('followerData.csv')
                    os.rename('followerDataNew.csv', 'followerData.csv')
                    if len(newFollowers) == 1:
                        message("Thank you for following the channel " + " ".join(
                            newFollowers) + "! Type !" + FolPet + " to see your the information on your " + FolPet + " :bat: :bat: :bat:")
                    if len(newFollowers) > 1:
                        message("Thank you for following the channel " + ", ".join(newFollowers[0:-1]) + " and " +
                                newFollowers[-1] + "! Type !" + FolPet + " to see the information on your " + FolPet + " :bat: :bat: :bat:")
                # If someone is a follower set isFollower to 1
                for i1 in range(len(followerList)):
                    for i2 in range(len(followerLines)):
                        if followerList[i1]['from_name'].encode('ascii', 'ignore').lower().rstrip() == \
                                followerLines[i2][0].lower().rstrip():
                            followerLines[i2][2] = "1"
                # If someone unfollows set isFollower to 0
                for i1 in range(len(unfollowers)):
                    for i2 in range(len(followerLines)):
                        if not followerLines[i2][0].lower().rstrip() == Channel[1:].lower().rstrip():
                            if followerLines[i2][0] == unfollowers[i1]:
                                followerLines[i2][2] = "0"

                # Assign gender
                for i in range(len(followerLines)):
                    try:
                        if followerLines[i][4] == "":
                            maleFemale = random.randint(0, 1)
                            if maleFemale == 1:
                                followerLines[i][4] = 'female'
                            else:
                                followerLines[i][4] = 'male'
                    except IndexError:
                        print 'Skipped adding gender. Will add next time this loops'
                        pass

                # Assign Name
                for i in range(len(followerLines)):
                    try:
                        if followerLines[i][3] == "":
                            if followerLines[i][4].lower() == 'male':
                                randomNumber = random.randint(0, len(batMaleNames))
                                maleName = batMaleNames[randomNumber]
                                followerLines[i][3] = maleName
                            if followerLines[i][4].lower() == 'female':
                                randomNumber = random.randint(0, len(batFemaleNames))
                                femaleName = batFemaleNames[randomNumber]
                                followerLines[i][3] = femaleName
                    except IndexError:
                        print 'Skipped adding name. Will add next time this loops'
                        pass

                # Refresh the total seconds followed per user
                followAgeAll()
                for i in range(len(followerLines)):
                    for i2 in range(len(followerList)):
                        if followerLines[i][0] == followerList[i2]['from_name'].rstrip():
                            followerLines[i][1] = followAgeList[i2][5]

                # Assign color
                global totalBlackBats, totalBrownBats, totalRedBats
                global blackBatScore, brownBatScore, redBatScore
                global percentageBlackBats, percentageRedBats, percentageBrownBrownBats
                global totalColoredBats
                try:
                    totalColoredBats = 0.00
                    totalBlackBats = 0.00
                    totalBrownBats = 0.00
                    totalRedBats = 0.00
                except Exception, e:
                    print str(e)
                if followerLines[1][5] == "":
                    followerLines[1][5] = 'Black'
                if followerLines[2][5] == "":
                    followerLines[2][5] = 'Brown'
                if followerLines[3][5] == "":
                    followerLines[3][5] = 'Red'
                try:
                    for i in range(len(followerLines)):

                        if totalColoredBats > 2:
                            percentageBlackBats = float(totalBlackBats / totalColoredBats)
                            percentageBrownBats = float(totalBrownBats / totalColoredBats)
                            percentageRedBats = float(totalRedBats / totalColoredBats)

                            blackBatScore = 0.6 - percentageBlackBats
                            brownBatScore = 0.3 - percentageBrownBats
                            redBatScore = 0.1 - percentageRedBats

                            # see if list is empty and add value
                            try:
                                if followerLines[i][5] == "":
                                    if (blackBatScore > brownBatScore) and (blackBatScore > redBatScore):
                                        followerLines[i][5] = 'Black'
                                    if (blackBatScore > brownBatScore) and (blackBatScore == redBatScore):
                                        followerLines[i][5] = 'Black'
                                    if (brownBatScore > blackBatScore) and (brownBatScore > redBatScore):
                                        followerLines[i][5] = 'Brown'
                                    if (brownBatScore > blackBatScore) and (brownBatScore == redBatScore):
                                        followerLines[i][5] = 'Brown'
                                    if (redBatScore > blackBatScore) and (redBatScore > brownBatScore):
                                        followerLines[i][5] = 'Red'
                                    if (redBatScore > blackBatScore) and (redBatScore == brownBatScore):
                                        followerLines[i][5] = 'Red'
                                    if (blackBatScore == brownBatScore) and (brownBatScore == redBatScore):
                                        followerLines[i][5] = 'Black'
                                    if (blackBatScore == brownBatScore):
                                        followerLines[i][5] = 'Black'
                            except Exception, e:
                                print "could not decide " + FolPet + " color"
                                print(str(e))

                        # check for which " + FolPet + " to add next
                        if followerLines[i][5] == 'Black':
                            totalBlackBats = totalBlackBats + 1
                        if followerLines[i][5] == 'Brown':
                            totalBrownBats = totalBrownBats + 1
                        if followerLines[i][5] == 'Red':
                            totalRedBats = totalRedBats + 1
                        totalColoredBats = totalBlackBats + totalBrownBats + totalRedBats

                except IndexError:
                    print "bat color indexerror"
                    pass
                except Exception, e:
                    print "could not add " + FolPet + " color"
                    print (str(e))

                # Check if subscriber or not.
                subscribers()
                for i1 in range(len(followerLines)):
                    followerLines[i1][6] = 0
                for i1 in range(len(followerLines)):
                    for i2 in range(len(subscriberResponse['data'])):
                        if followerLines[i1][0].lower() == subscriberResponse['data'][i2]['user_name'].lower():
                            followerLines[i1][6] = 1

                # After all the editing has been done
                # write back all the followerLines
                # I had to write back to a new file and rename it because of lack of memory

                if not os.path.exists('followerDataNew.csv'):
                    open('followerDataNew.csv', "w+").close()
                csvfile = open('followerDataNew.csv', "wb")
                followerDataWriter = csv.writer(csvfile, delimiter=",")
                followerDataWriter.writerows(followerLines)
                csvfile.close()
                os.remove('followerData.csv')
                os.rename('followerDataNew.csv', 'followerData.csv')

                # open the subsciber file to get the lines to the Sub file
                if not os.path.exists('subscriberData.csv'):
                    open('subscriberData.csv', "w+").close()
                global subscriberLines
                csvfile = open('subscriberData.csv', "rb")
                subscriberDataReader = csv.reader(csvfile, delimiter=",")
                subscriberLines = list(subscriberDataReader)
                csvfile.close()

                # Thank for upgrading and set Subtier
                try:
                    for i1 in range(len(subscriberLines)):
                        for i2 in range(len(subscriberResponse['data'])):
                            if subscriberResponse['data'][i2]['user_name'].encode('ascii',
                                                                                                      'ignore') == \
                                    subscriberLines[i1][0]:
                                # Check for upgrades of existing subscriptions
                                if subscriberResponse['data'][i2]['tier'][0] > subscriberLines[i1][2]:
                                    if subscriberResponse['data'][i2]['tier'] == u'1000':
                                        message("Thank you " + subscriberResponse['data'][i2]['user_name'].encode('ascii', 'ignore') + " for resubscribing! ridgurHeart ridgurHeart ridgurHeart ridgurHeart ridgurHeart ridgurHeart")
                                    if subscriberResponse['data'][i2]['tier'] == u'2000':
                                        message("Thank you " + subscriberResponse['data'][i2]['user_name'].encode('ascii', 'ignore') + " for upgrading your subscription to tier 2! ridgurHeart ridgurHeart ridgurHeart ridgurHeart ridgurHeart ridgurHeart")
                                    if subscriberResponse['data'][i2]['tier'] == u'3000':
                                        message("Thank you " + subscriberResponse['data'][i2]['user_name'].encode('ascii', 'ignore') + " for upgrading your subscription to tier 3! ridgurHeart ridgurHeart ridgurHeart ridgurHeart ridgurHeart ridgurHeart")

                                # Set sub tier and set back to 0 if sub runs out
                                subscriberLines[i1][2] = 0
                                subPlan = subscriberResponse['data'][i2]['tier'].encode('ascii', 'ignore')
                                subscriberLines[i1][2] = subPlan[0]
                except Exception, e:
                    print "Subtier error"
                    print str(e)

                # Find new subscribers
                subscriberList = []
                for i in range(len(subscriberResponse['data'])):
                    subscriberList.insert(0, subscriberResponse['data'][i]['user_name'].encode(
                        'ascii', 'ignore'))
                subscriberList = map(str.strip, subscriberList)

                newSubscribers = [item for item in subscriberList if
                                  item not in [i[0] for i in subscriberLines[1:]]]
                newGiftedSubscribers = []
                newGifters = []
                newSelfSubscribers = []

                for i1 in range(len(newSubscribers)):
                    for i2 in range(len(subscriberResponse['data'])):
                        subscriberName = subscriberResponse['data'][i2]['user_name'].lower()
                        if subscriberName == newSubscribers[i1].lower():
                            if subscriberResponse['data'][i2]['is_gift'] == False:
                                newSelfSubscribers.append(newSubscribers[i1])
                            if subscriberResponse['data'][i2]['is_gift'] == True:
                                newGiftedSubscribers.append(newSubscribers[i1])
                                newGifters.append(
                                    subscriberResponse['data'][i2]['gifter_name'].encode('ascii', 'ignore'))

                unSubscribers = [item for item in [i[0] for i in subscriberLines[1:]] if item not in subscriberList]

                if len(newSubscribers) > 0:
                    if len(subscriberLines) == 0:
                        subscriberLines.append(
                            ["Username", "SubStreak", "SubTier", "GiftedSubs", "GiftPoints", "SubPoints",
                             "TotalElves", "LastName", "Elf1Name", "Elf1Gender", "Elf2Name", "Elf2Gender",
                             "Elf3Name", "Elf3Gender", "Elf4Name", "Elf4Gender", "Elf5Name", "Elf5Gender",
                             "Elf6Name", "Elf6Gender"])
                    if len(newSelfSubscribers) == 1:
                        message("Thank you for subscribing " + " ".join(
                            newSelfSubscribers) + "! Type !" + SubPet + " to see your " + SubPet + "'s information ridgurHeart ridgurHeart ridgurHeart ridgurHeart ridgurHeart ridgurHeart")
                    if len(newSelfSubscribers) > 1:
                        message("Thank you for the subscriptions " + ", ".join(newSelfSubscribers[0:-1]) + " and " +
                                newSelfSubscribers[-1] + "! Type !" + SubPet + "  to see your " + SubPet + "'s information ridgurHeart ridgurHeart ridgurHeart ridgurHeart ridgurHeart ridgurHeart")
                    for i1 in range(len(newSubscribers)):
                        for i2 in range(len(subscriberResponse['data'])):
                            if subscriberResponse['data'][i2]['user_name'].encode('ascii',
                                                                                                      'ignore') == \
                                    newSubscribers[i1]:
                                if subscriberResponse['data'][i2]['tier'][0] == "1":
                                    subscriberLines.append([newSubscribers[i1]] + ["1"] + [
                                        subscriberResponse['data'][i2]['tier'][0]] + ([""] * 2) + [
                                                               "1"] + ([""] * 4))
                                if subscriberResponse['data'][i2]['tier'][0] == "2":
                                    subscriberLines.append([newSubscribers[i1]] + ["1"] + [
                                        subscriberResponse['data'][i2]['tier'][0]] + ([""] * 2) + [
                                                               "2"] + ([""] * 4))
                                if subscriberResponse['data'][i2]['tier'][0] == "3":
                                    subscriberLines.append([newSubscribers[i1]] + ["1"] + [
                                        subscriberResponse['data'][i2]['tier'][0]] + ([""] * 2) + [
                                                               "6"] + ([""] * 4))
                    if len(newGiftedSubscribers) == 1:
                        message(newGifters + " has given a subscription to " + " ".join(
                            newGiftedSubscribers) + "! Type !" + SubPet + " to see your " + SubPet + "'s information")
                    if len(newGiftedSubscribers) > 1:
                        if len(newGifters) == 1:
                                message(" ".join(newGifters) + "Has gifted a sub to the lucky " + ", ".join(
                                    newGiftedSubscribers[0:-1]) + " and " + newGiftedSubscribers[
                                            -1] + "! Type !" + SubPet + " to see your " + SubPet + "'s information")
                        if len(newGifters) > 1:
                                message(" ".join(newGifters) + "have gifted " + str(
                                    len(newGiftedSubscribers)) + " subs in total to the lucky " + ", ".join(
                                    newGiftedSubscribers[0:-1]) + " and " + newGiftedSubscribers[
                                            -1] + "! Type !" + SubPet + " to see your " + SubPet + "'s information")
                    if len(newGiftedSubscribers) > 0:
                        newGifter = True
                        for i1 in range(len(newGifters)):
                            for i2 in range(len(subscriberLines)):
                                if not newGifters[i1] == subscriberLines[i2][0]:
                                    newGifter = False
                                if newGifter == True:
                                    subscriberLines.append([newGifters[i1]] + ([""] * 18))

                # add sub and gift points
                for i in range(len(subscriberLines)):
                    if i > 0:
                        if subscriberLines[i][4] == "":
                            subscriberLines[i][4] = "0"
                        if subscriberLines[i][5] == "":
                            subscriberLines[i][5] = "0"
                        subscriberLines[i][6] = str(int(subscriberLines[i][4]) + int(subscriberLines[i][5]))

                # Assign gender
                for i1 in range(len(subscriberLines)):
                    for i2 in range(len(subscriberLines[i1][9::2])):
                        index = (i2 * 2) + 9
                        if subscriberLines[i1][index] == "":
                            maleFemale = random.randint(0, 2)
                            if maleFemale == 0:
                                subscriberLines[i1][index] = 'male'
                            if maleFemale == 1:
                                subscriberLines[i1][index] = 'female'
                            if maleFemale == 2:
                                subscriberLines[i1][index] = 'androgynous'

                # Assign first and last name
                for i1 in range(len(subscriberLines)):
                    try:
                        for i2 in range(len(subscriberLines[i1][8::2])):
                            index = (i2 * 2) + 8
                            genderIndex = index + 1
                            if subscriberLines[i1][index] == "":
                                if subscriberLines[i1][genderIndex] == 'male':
                                    randomNumber = random.randint(0, len(elfNamesFemale) - 1)
                                    maleName = elfNameMale[randomNumber]
                                    subscriberLines[i1][index] = maleName
                                if subscriberLines[i1][genderIndex] == 'female':
                                    randomNumber = random.randint(0, len(elfNameMale) - 1)
                                    femaleName = elfNamesFemale[randomNumber]
                                    subscriberLines[i1][index] = femaleName
                                if subscriberLines[i1][genderIndex] == 'androgynous':
                                    randomNumber = random.randint(0, len(elfNameAndrogynous) - 1)
                                    androgynousName = elfNameAndrogynous[randomNumber]
                                    subscriberLines[i1][index] = androgynousName
                            if subscriberLines[i1][7] == "":
                                randomNumber = random.randint(0, len(elfLastNames) - 1)
                                elfLastName = elfLastNames[randomNumber]
                                subscriberLines[i1][7] = elfLastName
                    except IndexError:
                        print 'Skipped adding " + SubPet + " name or gender. Will add next time this loops'
                        pass

                # add parameters for " + SubPetPlural + " if gifts subs have been given
                for i1 in range(len(subscriberLines)):
                    if i1 > 0:
                        if (int(subscriberLines[i1][6]) * 2) > len(subscriberLines[i1][8:]):
                            for i2 in range(((int(subscriberLines[i1][6]) * 2) - len(subscriberLines[i1][8:]))):
                                subscriberLines[i1].append("")

                # Update SubStreak if badge is higher than local value
                for i1 in range(len(badges)):
                    if "subscriber" in badges[i1]:
                        subStreak = re.search(r'/(\d*)', badges[i1]).group(1)
                        if subStreak == "0":
                            subStreak = "1"
                        for i2 in range(len(subscriberLines)):
                            if subscriberLines[i2][0].lower().rstrip() == username.rstrip().lower().encode('ascii', 'ignore'):
                                if subStreak > subscriberLines[i2][1]:
                                    subscriberLines[i2][1] = subStreak

                # Add length since subscription
                # subscribeAgeAll()
                # for i1 in range(len(subscriberLines)):
                #     for i2 in range(len(subscribeAgeList)):
                #         if not subscriberLines[i1][1] == "SubStreak":
                #             if subscriberLines[i1][0].lower() == subscribeAgeList[i2][8].lower().encode('ascii', 'ignore'):
                #                 if subscriberLines[i1][1] < subscribeAgeList[i2][7]:
                #                     subscriberLines[i1][1] = subscribeAgeList[i2][7]

                # write back any changes to a the subscriber file
                csvfile = open('subscriberDataNew.csv', "wb")
                subscriberDataWriter = csv.writer(csvfile, delimiter=",")
                subscriberDataWriter.writerows(subscriberLines)
                csvfile.close()
                os.remove('subscriberData.csv')
                os.rename('subscriberDataNew.csv', 'subscriberData.csv')

            except IndexError:
                pass
            except Exception, e:
                print("while true events error")
                print(str(e))
            if "!" in text.lower().split()[0][0]:
                firstStr = text.lower().split()[0]
                if "!commands" in firstStr or "!cmds" in firstStr:
                    try:
                        message("See what the bot can do here: https://github.com/ridgure/twitchbot#features")
                    except IndexError:
                        pass
                if username.lower() == "bugmacgregor":
                    try:
                        bugCounter()
                        print BugMessages
                        if BugMessages % 5 == 0:
                            randomNumber = random.randint(0, (len(bedTime) - 1))
                            message(bedTime[randomNumber])
                    except Exception, e:
                        print str(e)
                    except IndexError:
                        pass
                # if username == "couch_potato135":
                #     message("This message is brought to you by the e.p.a")
                elif "!song" in firstStr:
                    try:
                        csvfile = open('D:\Programs\Snip\Snip-v6.10.2\Snip\Snip.txt', "rb")
                        songDataReader = csv.reader(csvfile, delimiter=",")
                        songLines = list(songDataReader)
                        song = str(songLines[0][0]).decode("utf-8")
                        message(song.encode('ascii', 'ignore'))
                    except IndexError:
                        pass
                elif "!ctt" in firstStr or "!tweet" in text.lower().split()[0]:
                    try:
                        subscriber = False
                        title = channelInfo()['status'].encode('utf', 'ignore')
                        title = title.replace(" ", "%20")
                        for i1 in range(len(subscriberLines)):
                            if username.lower().rstrip() == subscriberLines[i1][0].lower().rstrip() and int(
                                    subscriberLines[i1][1]) > 0:
                                if not subscriberLines[i1][0] == "Username":
                                    subscriber = True
                                    if int(subscriberLines[i1][6]) == 1:
                                        tweet = tinyurl.create_one("https://twitter.com/intent/tweet?text=My%20" + SubPet + "%20" + subscriberLines[i1][8] + "%20and%20I%20are%20watching%20@Ridgure%20doing%20" + title + "%20come%20join%20us%20at%20Twitch.tv/Ridgure%20#ModdedMinecraft%20#SevTech")
                                    if int(subscriberLines[i1][6]) > 1:
                                        maxElf = (int(subscriberLines[i1][6]) * 2) + 7
                                        tweet = tinyurl.create_one("https://twitter.com/intent/tweet?text=My%20" + SubPetPlural + "%20" + ",%20".join(subscriberLines[i1][8:maxElf:2]) + "%20and%20I%20are%20watching%20@Ridgure%20doing%20" + title + "%20come%20join%20us%20at%20Twitch.tv/Ridgure%20%23ModdedMinecraft%20%23SevTech")
                        if subscriber == False:
                            follower = False
                            for i1 in range(len(followerLines)):
                                if not followerLines[i1][0] == "Username":
                                    if username.lower().rstrip() == followerLines[i1][0].lower().rstrip():
                                        if int(followerLines[i1][2]) == 1:
                                            follower = True
                                            tweet = tinyurl.create_one("https://twitter.com/intent/tweet?text=My%20" + FolPet + "%20" + followerLines[i1][3] + "%20and%20I%20are%20watching%20@Ridgure%20doing%20" + title + "%20come%20join%20us%20at%20Twitch.tv/Ridgure%20#ModdedMinecraft%20#SevTech")
                            if follower == False:
                                    tweet = tinyurl.create_one("https://twitter.com/intent/tweet?text=I%20am%20watching%20@Ridgure%20doing%20" + title + "%20come%20join%20me%20at%20Twitch.tv/Ridgure%20#Asylumcraft%20#ModdedMinecraft%20#SevTech")
                        message("This link is only for " + username + "! " + tweet + " get your link by doing !ctt")
                    except IndexError:
                        pass
                    except Exception, e:
                        print str(e)
                        pass
                elif "!tp" in firstStr:
                    try:
                        message("The texture pack I am currently using is Soartex Fanver Modded Universal")
                    except IndexError:
                        pass
                # elif "!multi" in firstStr or "kadgar" in firstStr:
                #     try:
                #         message("https://multistre.am/ridgure/lilgamerhelle/xman657483/")
                #     except IndexError:
                #         pass
                elif "!nextbreak" in firstStr:
                    try:
                        if uptime().hour % 2 == 0:
                            message("Next break is in 1 hour and " + str(55 - uptime().minute) + " minutes")
                            pass
                        else:
                            if uptime().minute >= 55:
                                message("Breaktime should be right now. If there is no break being taken something is severely wrong")
                            else:
                                message("Next break is in " + str(55 - uptime().minute) + " minutes")
                    except IndexError:
                        pass
                elif "!social" in firstStr or "!link" in firstStr:
                    try:
                        message("Find me on Facebook: fb.com/Ridgure    ")
                        message("Find me on Twitter: Twitter.com/RigidStructure")
                        message("Find me on Instagram: Instagram.com/Ridgure")
                        message("Join the discord! https://discord.gg/yddBmCE")
                    except IndexError:
                        pass
                elif "!facebook" in firstStr or "!face" in firstStr:
                    try:
                        message("Find me on Facebook: fb.com/Ridgure")
                    except IndexError:
                        pass
                elif "!youtube" in firstStr or "!yt" in firstStr:
                    try:
                        message("Find me on Youtube: https://www.youtube.com/channel/UC6_7gjgcdGXsu0zIz42D6fA")
                    except IndexError:
                        pass
                elif "!twitter" in firstStr:
                    try:
                        message("Find me on Twitter: Twitter.com/RigidStructure")
                    except IndexError:
                        pass
                elif "!instagram" in firstStr or "!insta" in firstStr:
                    try:
                        message("Find me on Instagram: Instagram.com/RigidStructure")
                    except IndexError:
                        pass
                elif "!sub" in firstStr:
                    try:
                        message("twitch.tv/products/ridgure")
                    except IndexError:
                        pass
                elif "!insomniac" in firstStr:
                    try:
                        if username.lower() == broadcaster.lower():
                            message("/timeout " + text.split()[1] + "14400")
                        else:
                            message("this command is broadcaster only")
                    except IndexError:
                        pass
                elif "!sr" in firstStr:
                    try:
                        message("If the song you want me to play is on pretzel.rocks I will play it for you")
                    except IndexError:
                        pass
                elif "!lurk" in firstStr:
                    try:
                        isSubscriber = 0
                        for i1 in range(len(badges)):
                            if "subscriber" in badges[i1]:
                                isSubscriber = 1
                                pass
                        if isSubscriber == 1:
                            elfInfo = None
                            for i in range(len(subscriberLines)):
                                if subscriberLines[i][0].rstrip().lower().decode('utf-8') == username.lower():
                                    elfInfo = subscriberLines[i]
                            if elfInfo[6] == "1":
                                message(username + "'s " + SubPet + " " + elfInfo[8] + " " + elfInfo[7] + " is going back inside the elf tree for the night")
                            elif elfInfo[6] == "2":
                                message(username + "'s " + SubPetPlural + " " + elfInfo[8] + " and " + elfInfo[10] + " " + elfInfo[7] + " are going back inside the elf tree for the night")
                            elif int(elfInfo[6]) > 2:
                                maxElf = (int(elfInfo[6]) * 2) + 6
                                elfFirstNames = elfInfo[8:maxElf:2]
                                message(username + "'s " + SubPetPlural + " " + ", ".join(elfFirstNames) + " and " + elfInfo[
                                    maxElf] + " " + elfInfo[7] + " are going back inside the elf tree for the night")
                        else:
                            for i in range(len(followerLines)):
                                if followerLines[i][0].lower().rstrip().decode('utf-8') == username.lower():
                                    if followerLines[i][2] == "0":
                                        message("User is not following the channel")
                                    elif followerLines[i][2] == "1":
                                        if followerLines[i][6] == 0:
                                            message(username + "'s " + FolPet + " " + followerLines[i][3] + " is going into hybernation")
                    except IndexError:
                        pass
                elif "!unlurk" in firstStr:
                    try:
                        anOrA = random.randint(0,1)
                        anOrALetter = ""
                        exclusivity = random.randint(0,3)
                        rise = ""
                        slumber = ""

                        if anOrA == 0:
                            anOrALetter = "an "
                        else:
                            anOrALetter = "a "
                        if exclusivity == 0:
                            #exclusive rise
                            rise = exclusiveAdverb[random.randint(0, len(exclusiveAdverb) - 1)]
                            if anOrA == 0:
                                slumber = exclusiveAdjectiveAn[random.randint(0, len(exclusiveAdjectiveAn) - 1)]
                            else:
                                slumber = exclusiveAdjectiveA[random.randint(0, len(exclusiveAdjectiveA) - 1)]
                            getUp = getUpType[random.randint(0, len(getUpType) - 1)]
                        elif exclusivity == 1:
                            #exclusive slumber
                            rise = riseType[random.randint(0, len(riseType) - 1)]
                            if anOrA == 0:
                                slumber = exclusiveAdjectiveAn[random.randint(0, len(exclusiveAdjectiveAn) - 1)]
                            else:
                                slumber = exclusiveAdjectiveA[random.randint(0, len(exclusiveAdjectiveA) - 1)]
                            getUp = getUpType[random.randint(0, len(getUpType) - 1)]
                        elif exclusivity == 2:
                            #exclusive getup
                            rise = riseType[random.randint(0, len(riseType) - 1)]
                            if anOrA == 0:
                                slumber = slumberAn[random.randint(0, len(slumberAn) - 1)]
                            else:
                                slumber = slumberA[random.randint(0, len(slumberA) - 1)]
                            getUp = exclusiveAdverb[random.randint(0, len(exclusiveAdverb) - 1)]
                        else:
                            #no exclusivity
                            rise = riseType[random.randint(0, len(riseType) - 1)]
                            if anOrA == 0:
                                slumber = slumberAn[random.randint(0, len(slumberAn) - 1)]
                            else:
                                slumber = slumberA[random.randint(0, len(slumberA) - 1)]
                            getUp = getUpType[random.randint(0, len(getUpType) - 1)]
                        isSubscriber = 0
                        for i1 in range(len(badges)):
                            if "subscriber" in badges[i1]:
                                isSubscriber = 1
                                pass
                        if isSubscriber == 1:
                            elfInfo = None
                            for i in range(len(subscriberLines)):
                                if subscriberLines[i][0].rstrip().lower().decode('utf-8') == username.lower():
                                    elfInfo = subscriberLines[i]
                            if elfInfo[6] == "1":
                                message(username + "'s " + SubPet + " " + elfInfo[8] + " " + elfInfo[7] + " " + rise + " rises from " + anOrALetter + slumber + " slumber and " + getUp + " gets up")
                            elif elfInfo[6] == "2":
                                message(username + "'s " + SubPetPlural + " " + elfInfo[8] + " and " + elfInfo[10] + " " + elfInfo[7] + " " + rise + " rise from " + anOrALetter + slumber + " slumber and " + getUp + " get up")
                            elif int(elfInfo[6]) > 2:
                                maxElf = (int(elfInfo[6]) * 2) + 6
                                elfFirstNames = elfInfo[8:maxElf:2]
                                message(username + "'s " + SubPetPlural + " " + ", ".join(elfFirstNames) + " and " + elfInfo[
                                    maxElf] + " " + elfInfo[7] + " " + rise + " rise from " + anOrALetter + slumber + " slumber and " + getUp + " get up")
                        else:
                            for i in range(len(followerLines)):
                                if followerLines[i][0].lower().rstrip().decode('utf-8') == username.lower():
                                    if followerLines[i][2] == "0":
                                        message("User is not following the channel")
                                    if followerLines[i][2] == "1":
                                        if followerLines[i][6] == 0:
                                            message(username + "'s " + FolPet + " " + followerLines[i][3] + " " + rise + " rises from " + anOrALetter + slumber + " slumber and " + getUp + " gets up")
                    except IndexError:
                        pass
                elif "!english" in firstStr:
                    try:
                        message("Please keep the chat in english so your fellow chatters will understand you")
                    except IndexError:
                        pass
                elif "!rhino" in firstStr:
                    try:
                        message("The program I am using to generate the bat cave and sub tree is called Rhinoceros3D")
                    except IndexError:
                        pass
                elif "!ob" in firstStr:
                    try:
                        message('If you feel like your message was not seen please write "^" and it might still be read')
                    except IndexError:
                        pass
                elif "!pokemon" in firstStr:
                    try:
                        message("Here is my trainer code: 8164 5829 3574 Feel free to add me")
                    except IndexError:
                        pass
                elif "!benefits" in firstStr:
                    try:
                        message("Per sub point you contribute to the stream one " + FolPet + " morphs into an " + SubPet + ". If you are subscribed you will also have access to my sub emote")
                    except IndexError:
                        pass
                elif ("!" + FolPet) == firstStr:
                    try:
                        if len(text.lower().split()) == 1:
                            for i in range(len(followerLines)):
                                if followerLines[i][0].lower().rstrip() == username.lower().rstrip():
                                    if followerLines[i][4].lower() == 'male':
                                        gender = 'he'
                                    if followerLines[i][4].lower() == 'female':
                                        gender = 'she'
                                    if followerLines[i][2] == "0":
                                        message("User is not following the channel")
                                    if followerLines[i][2] == "1":
                                        if followerLines[i][6] == 0:
                                            message(username + "'s " + FolPet + " is called " + followerLines[i][
                                                3] + " " + gender + " is colored " + followerLines[i][5].lower() + " :bat: :bat: :bat:")
                                        if followerLines[i][6] == 1:
                                            message(
                                                username + "'s " + FolPet + " has morphed into an " + SubPet + ". !" + SubPet + " to see information on your " + SubPet + ".")
                        if len(text.lower().split()) == 2:
                            for i in range(len(followerLines)):
                                if followerLines[i][0].lower().rstrip() == text.lower().split()[1]:
                                    if followerLines[i][4].lower() == 'male':
                                        gender = 'He'
                                    if followerLines[i][4].lower() == 'female':
                                        gender = 'She'
                                    if followerLines[i][2] == "0":
                                        message("User is not following the channel")
                                    if followerLines[i][2] == "1":
                                        if followerLines[i][6] == 0:
                                            message(text.split()[1] + "'s " + FolPet + " is called " + followerLines[i][
                                                3] + ". " + gender + " is colored " + followerLines[i][5].lower() + " :bat: :bat: :bat:")
                                        if followerLines[i][6] == 1:
                                            message(
                                                text.split()[1] + "'s " + FolPet + " has morphed into an " + SubPet + ". !" + subPet + " " + text.split()[
                                                    1] + " to see information on their " + SubPet + ".")
                                    if not followerLines[i][0].lower().rstrip() == text.lower().split()[1]:
                                        message("Follower not found")
                                elif followerLines[i][0].lower().rstrip() == text.lower().split()[1]:
                                    message("User is not following the channel")
                            # else:
                            #     message("User is not following the channel")
                    except IndexError:
                        pass
                        message(text.split()[1] + "'s bat could not be found")
                    except Exception, e:
                        message(text.split()[1] + "'s bat could not be found")
                        pass
                elif ("!" + SubPet) == firstStr or ("!" + SubPetPlural) == firstStr:
                    try:
                        elfInfo = None
                        if len(text.lower().split()) == 2:
                            for i in range(len(subscriberLines)):
                                if subscriberLines[i][0].lower().rstrip() == text.lower().split()[1]:
                                    elfInfo = subscriberLines[i]
                            if elfInfo == None:
                                message("User is not a subscriber")
                            if elfInfo[9].lower() == 'male':
                                gender = 'His'
                            if elfInfo[9].lower() == 'female':
                                gender = 'Her'
                            if elfInfo[9].lower() == 'androgynous':
                                gender = 'Their'
                            if elfInfo[6] == "1":
                                message(
                                    text.split()[1] + "'s " + FolPet + " morphed into 1 " + SubPet + ". " + gender + " name is " + elfInfo[
                                        8] + " " +
                                    elfInfo[7])
                            if elfInfo[6] == "2":
                                message(
                                    text.split()[1] + "'s " + FolPet + " morphed into 2 " + SubPetPlural + ". Their names are " + elfInfo[
                                        8] + " and " +
                                    elfInfo[10] + " " + elfInfo[7])
                            if int(elfInfo[6]) > 2:
                                maxElf = (int(elfInfo[6]) * 2) + 6
                                elfFirstNames = elfInfo[8:maxElf:2]
                                message(text.split()[1] + "'s " + FolPet + " morphed into " + elfInfo[
                                    6] + " " + SubPetPlural + ". Their names are " + ", ".join(elfFirstNames) + " and " + elfInfo[
                                            maxElf] + " " + elfInfo[7])
                        if len(text.lower().split()) == 1:
                            for i in range(len(subscriberLines)):
                                if subscriberLines[i][0].lower() == username.lower().encode('ascii', 'ignore'):
                                    elfInfo = subscriberLines[i]
                            if elfInfo == None:
                                message("User is not a subscriber")
                            if elfInfo[9].lower() == 'male':
                                gender = 'His'
                            if elfInfo[9].lower() == 'female':
                                gender = 'Her'
                            if elfInfo[9].lower() == 'androgynous':
                                gender = 'Their'
                            if elfInfo[6] == "1":
                                message(username +
                                    "'s " + FolPet + " morphed into 1 " + SubPet + ". " + gender + " name is " + elfInfo[8] + " " + elfInfo[7])
                            if elfInfo[6] == "2":
                                message(username +
                                    "'s " + FolPet + " morphed into 2 " + SubPetPlural + ". Their names are " + elfInfo[8] + " and " +
                                    elfInfo[10] + " " + elfInfo[7])
                            if int(elfInfo[6]) > 2:
                                maxElf = (int(elfInfo[6]) * 2) + 6
                                elfFirstNames = elfInfo[8:maxElf:2]
                                message(username + "'s " + FolPet + " morphed into " + elfInfo[6] + " " + SubPetPlural + ". Their names are " + ", ".join(elfFirstNames) + " and " +
                                        elfInfo[maxElf] + " " + elfInfo[7])
                    except IndexError, e:
                        print str(e)
                        pass
                    except Exception, e:
                        print str(e)
                        pass
                elif "!raid" in text.lower().split()[0]:
                    try:
                        if username.lower() == broadcaster:
                            message("Please raid Twitch.tv/" + text.split()[1])
                            message('Followers: "/me Ridgure raid" + any heart you have')
                            message('Subs: "/me Ridgure raid ridgurHeart ridgurHeart ridgurHeart "')
                        else:
                            message("This command is broadcaster only")
                    except IndexError:
                        message("Msg: /me Ridgure raid twitchRaid twitchRaid twitchRaid")
                        pass
                elif "!dance" in firstStr:
                    try:
                        message("<o/")
                        message("\o>")
                        message(",o/")
                        message("\o,")
                        message("_o>")
                        message("<o_")
                        message("<o>")
                        message("\o/")
                    except IndexError:
                        pass
                elif "!fu" in firstStr:
                    try:
                        if username.lower() == broadcaster:
                            message("( ︶︿︶)_╭∩╮")
                        else:
                            message("This command is broadcaster only")
                    except IndexError:
                        pass
                elif "!break" in firstStr:
                    try:
                        if username.lower() == broadcaster:
                            message("Breakdancing is happening while chat completely breaks out in applause ")
                        else:
                            message("This command is broadcaster only")
                    except IndexError:
                        pass
                elif "!server" in firstStr or "!ip" == firstStr:
                    try:
                        message(
                            "the Ri3D server is for VIP's in the stream and people in the asylumcraft community only. !VIP to see how to become a VIP or try !ipee")
                    except IndexError:
                        pass
                elif "!vip" in firstStr or "!straitjacket" in firstStr or "!join" in firstStr:
                    try:
                        message(
                            "If you redeem the VIP/Discord ticket reward with your points you will be made VIP and get a special role in the discord")
                    except IndexError:
                        pass
                elif "!pack" in firstStr or "modpack" in firstStr or "sev" in firstStr:
                    try:
                        pack = "Reclaiming Our Home"
                        mcVersion = "1.12.2"
                        availability = False
                        if availability:
                            message(
                                "The modpack I am playing is called " + pack + ". Minecraft version " + mcVersion + " It is available through the curse and the AT launcher")
                        else:
                            message(
                                "The modpack I am playing is called " + pack + ". Minecraft version " + mcVersion + " This modpack made by xTrickShotProx is in closed beta and therefore not publicly available yet")
                    except IndexError:
                        pass
                elif "!version" in firstStr or "!vanilla" in firstStr:
                    try:
                        message("The version of minecraft I am currently playing is 1.12.2")
                    except IndexError:
                        pass
                elif "!streamcaptain" in firstStr or "!streamraiders" in firstStr or "!arr" in firstStr or "!boss" in firstStr or "!sc" == firstStr:
                    try:
                        message(
                            "Place your units over at https://www.streamcaptain.com/t/ridgure and help us win!")
                    except IndexError:
                        pass
                elif "!test" in firstStr or "!t3st" in firstStr:
                    try:
                        print str(datetime.datetime.now().strftime("%M:%S"))
                    except IndexError:
                        pass
                elif "!scrowl" == firstStr:
                    try:
                        message(username + "grumpily scowls at " + text.split()[1])
                    except IndexError:
                        pass
                elif "!shaders" == firstStr:
                    try:
                        shadersUsed = True
                        if shadersUsed:
                            message("I am using complimentary shaders")
                        else:
                            message("I am not using any shaders at the moment")
                    except IndexError:
                        pass
                elif "!rules" == firstStr:
                    try:
                        message("Welcome to my chat! My current commands are !social, !discord, !pack, !tp, !shaders, !lurk, !java, !oclock, !lick, !bellyrub, !smile, !timemeout, !ctt, !multipy and !add Chat rules: 1. Please be respectful to others. 2. No all caps. 3. No offensive language. 4. No Links or self promotion. 5. No talking about age 6. Join the java vanilla server if you are VIP. You can be VIP with 3600 Channel poitns 7. I say what I want to say. I will not repeat anything you ask. 8. I play what I want to play. 9. Pease keep the chat in english so your fellow chatters will understand you. Enjoy the show!")
                    except IndexError:
                        pass
                elif "!discord" in firstStr:
                    try:
                        message("Join the Discord! https://discord.gg/yddBmCE")
                    except IndexError:
                        pass
                elif "!ri3d" in firstStr.lower():
                    try:
                        message("Join the Ri3D Discord! https://discord.gg/vvS66dK2n3")
                    except IndexError:
                        pass
                elif "!java" in firstStr:
                    try:
                        message("https://github.com/DarkPacks/SevTech-Ages/wiki/Recommended-Java-Args")
                    except IndexError:
                        pass
                elif "!oclock" in firstStr or "!o'clock" in firstStr:
                    try:
                        message("The time for me right now is " + datetime.datetime.now().strftime(
                            "%H:%M") + " o'clock" + " CET") 
                    except IndexError:
                        pass
                elif "!specs" in firstStr:
                    try:
                        message("i7-4790k, GTX970")
                    except IndexError:
                        pass
                elif "!skin" in firstStr:
                    try:
                        message("mine.ly/Ridgure.1")
                    except IndexError:
                        pass
                elif "!shout" in firstStr or "!so" in firstStr:
                    if username.lower().rstrip() == broadcaster:
                        try:
                            message("Check out this awesome streamer over at Twitch.tv/" + text.split()[1])
                        except IndexError:
                            message("This command is broadcaster only")
                            pass
                elif "!breakdance" in firstStr:
                    if username.lower().rstrip() == broadcaster:
                        try:
                            message("Move around, grab a drink and Ridgure will be back before you think. If you enjoyed this session follow the !social media for updates on my progress so far and to get notified when I go live")
                        except IndexError:
                            pass
                elif "!support" in firstStr:
                    try:
                        message("You can support the stream by hosting, tweeting out the stream -> !ctt")
                    except IndexError:
                        pass
                elif "!newvid" in firstStr or "!audiobook" in firstStr:
                    try:
                        message("I made an audiobook! Go check it out -> https://youtu.be/lmpqw01Qs6kx")
                    except IndexError:
                        pass
                elif "!asylumcraft" in firstStr:
                    try:
                        message("See all the members of asylumcraft in the panel below and follow like you have never followerd before")
                    except IndexError:
                        pass
                elif "!bot" in firstStr:
                    try:
                        message("I write my own chatbot. To figure out what commands can be used and how to install it check out this page: https://github.com/Ridgure/TwitchBot")
                    except IndexError:
                        pass
                elif "!bug" in firstStr:
                    try:
                        message("If you have encountered an issue with the bot or have found a bug please report it here: https://github.com/Ridgure/TwitchBot/issues")
                    except IndexError:
                        pass
                elif "!ipee" in firstStr or "!eyepee" in firstStr:
                    try:
                        message("Haha " + username + " peed!")
                    except IndexError:
                        pass
                elif "!bellyrub" in firstStr:
                    try:
                        message(username + " rubs " + text.split()[1] + "'s belly " + lick())
                    except IndexError:
                        message("Did you remember to '!bellyrub <target>'?")
                        pass
                elif "!uptime" in firstStr:
                    try:
                        message("The stream has been live for " + str(uptime().hour) + "h " + str(uptime().minute) + "m")
                    except IndexError:
                        print "Uptime failed"
                elif "!fc" in firstStr or "!followdate" in firstStr:
                    try:
                        # get the user
                        if len(text.lower().split()) == 1:
                            user = username
                        if len(text.lower().split()) == 2:
                            user = (text.lower().split()[1])

                        testFollower = False
                        # get user index and get their follow time and date and length
                        for i1 in xrange(len(followerList)):
                            for i2 in xrange(len(followerList[i1])):
                                # print i1, followerList[i1]['from_name']
                                if followerList[i1]['from_name'] == user:
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
                            message("Command on cooldown")

                    except IndexError:
                        pass
                    except Exception, e:
                        print message("followage failed")
                        print(str(e))
                elif "!smile" in firstStr:
                    try:
                        message(username + " smiles at " + text.split()[1] + " " + randomEmote())
                    except IndexError:
                        message("Remember to '!smile <someone>'!")
                    except Exception, e:
                        message("Smile failed")
                        message(str(e))
                elif "!pet" in firstStr:
                    try:
                        message(username + " pets " + text.split()[1])
                    except IndexError:
                        message("Remember to '!pet <someone>'!")
                    except Exception, e:
                        message("Pet failed")
                        message(str(e))
                elif "!multiply" == firstStr:
                    try:
                        message(multiply())
                    except IndexError:
                        pass
                    except Exception, e:
                        message("Multiplication failed")
                        message(str(e))
                elif "!divide" == text.lower().split()[0]:
                    try:
                        message(divide())
                    except IndexError:
                        pass
                    except Exception, e:
                        message("Division failed")
                        message(str(e))
                elif "!add" == firstStr:
                    try:
                        message(add())
                    except IndexError:
                        pass
                    except Exception, e:
                        message("Addition failed")
                        message(str(e))
                elif "!elfnamechange" in firstStr:
                    try:
                        owner = False
                        if (len(text.lower().split()[2])) <= 16:
                            for i1 in range(len(subscriberLines)):
                                if subscriberLines[i1][0].rstrip().lower() == username.rstrip().lower():
                                    for i2 in range(len(subscriberLines[i1][0:]))[8::2]:
                                        if text.lower().split()[1] == subscriberLines[i1][i2].lower():
                                            csvfile = open('subscriberData.csv', "rb")
                                            subscriberDataReader = csv.reader(csvfile, delimiter=",")
                                            subscriberLines = list(subscriberDataReader)
                                            csvfile.close()
                                            subscriberLines[i1][i2] = text.split()[2].encode("utf-8")
                                            for i in range(1):
                                                message("Successfully changed " + text.split()[1] + "'s name to " + text.split()[2] + " " + subscriberLines[i1][7])
                                            csvfile = open('subscriberDataNew.csv', "wb")
                                            subscriberDataWriter = csv.writer(csvfile, delimiter=",")
                                            subscriberDataWriter.writerows(subscriberLines)
                                            csvfile.close()
                                            os.remove('subscriberData.csv')
                                            os.rename('subscriberDataNew.csv', 'subscriberData.csv')
                                            owner = True
                                            break
                        elif (len(text.lower().split()[2].encode("ascii"))) > 16:
                            message("Name cannot be longer than 16 characters")
                            owner = True
                        if owner == False:
                            message("You cannot change the name of other people's " + SubPetPlural)
                    except IndexError:
                        message("Did you remember to write '!elfnamechange <old first Name> <new first name>'?")
                        print "elfgenderchange failed"

                # Automatic responses
                elif "uwu" in text.lower():
                    message("ᵘʷᵘ")
                elif "rawr" in text.lower():
                    message("Rawr XD")
                elif "cobble" in text.lower().split()[:]:
                    try:
                        message("Eww not cobble!")
                    except IndexError:
                        pass
                elif "69" in text.lower().split()[:]:
                    try:
                        message("Nice")
                    except IndexError:
                        pass
                elif "(╯°□°）╯︵ ┻━┻" in text.lower().encode("utf-8"):
                    message("┬─┬ノ( º _ ºノ)")
                elif "!quote" in firstStr:
                    try:
                        message("You can redeem a quote with your channel points and I will bestow some ridgurWisdom upon you")
                    except IndexError:
                        pass

                # User specific commands
                elif "!jc747" in firstStr:
                    try:
                        if username.lower() == 'jc747' or username.lower() == broadcaster.lower():
                            message("It's JSea474 you fool!")
                        else:
                            message("This command is user specific")
                    except IndexError:
                        pass
                elif "!octo" in firstStr:
                    try:
                        message("Squid1 Squid2 Squid3 Squid2 Squid4")
                    except IndexError:
                        pass
                elif "!ras2709" in firstStr or "!ras" in firstStr:
                    try:
                        message("its the Ras patas! LUL")
                    except IndexError:
                        pass
                elif "!hayleyprimee" in firstStr.lower() or "!hayley" in firstStr.lower() or "!yoooohayley" in firstStr.lower():
                    try:
                        oAmount = random.randint(1, 149) * "o"
                        print oAmount
                        if username.lower() == 'yoooohayley' or username.lower() == broadcaster.lower():
                            message("Y" + oAmount)
                        else:
                            message("This command is user specific")
                    except IndexError:
                        pass
                elif "!lick" in firstStr:
                    try:
                        if username.lower() == 'wolvesarecool24' or username.lower() == broadcaster.lower():
                            message(username + " licks " + text.split()[1] + lick())
                        else:
                            message("only wolves can lick")
                    except IndexError:
                        pass
                elif "!sgt" in firstStr:
                    try:
                        if username.lower() == 'sgtlegotown':
                            message("0900-sgtCare")
                        else:
                            message("This command is user specific")
                            pass
                    except IndexError:
                        pass
                elif "!ruffle" in firstStr or "!ruffles" in firstStr:
                    try:
                        if username.lower() == 'ivanabcroftin' or username.lower() == 'ridgure':
                            message("IvanaBCroftin sneaks up to Ridgure and puts " + mess() + " in his hair")
                        else:
                            pass
                    except IndexError:
                        pass
                elif "!timemeout" in firstStr:
                    try:
                        if username.lower().rstrip() == "kbigliar":
                            if 0 < int(text.split()[1]) < 3601:
                                message("/timeout " + username + " " + text.split()[1])
                                message("Timed out " + username + " for " + text.split()[1] + " seconds")
                            elif int(text.split()[1]) < 0:
                                message("You cannot go back in time unless you are the doctor or Marty McFly")
                            else:
                                message("TimeMeOut failed")
                        if not username.lower() == "kbigliar":
                            message("Only ") + username + (" can time himself out")
                    except IndexError:
                        message("Add amount of seconds you want to be timed out after command")
                        pass

                # Pet commands
                elif "!batnamechange" in firstStr:
                    try:
                        csvfile = open('followerData.csv', "rb")
                        followerDataReader = csv.reader(csvfile, delimiter=",")
                        followerLines = list(followerDataReader)
                        csvfile.close()

                        if len(text.lower().split()[1].encode("utf-8")) < 10:
                            for i in range(len(followerLines)):
                                if followerLines[i][0].lower().rstrip() == username.lower().rstrip():
                                    followerLines[i][3] = text.split()[1]
                                    message("Successfully changed the name of " + username + "'s " + FolPet + " to " + text.split()[1])

                        if len(text.lower().split()[1].encode("utf-8")) > 20:
                            message("Name cannot be longer than 20 characters")
                        csvfile = open('followerDataNew.csv', "wb")
                        followerDataWriter = csv.writer(csvfile, delimiter=",")
                        followerDataWriter.writerows(followerLines)
                        csvfile.close()
                        os.remove('followerData.csv')
                        os.rename('followerDataNew.csv', 'followerData.csv')
                    except IndexError:
                        message("Did you remember to '!batnamechange <new name>'?")
                        pass
                elif "!batgenderchange" in firstStr:
                    try:
                        csvfile = open('followerData.csv', "rb")
                        followerDataReader = csv.reader(csvfile, delimiter=",")
                        followerLines = list(followerDataReader)
                        csvfile.close()

                        owner = False
                        for i1 in range(len(followerLines)):
                            if followerLines[i1][0].rstrip().lower() == username.rstrip().lower():
                                if text.split()[1].lower().rstrip() == "male":
                                    if followerLines[i1][4].lower().rstrip() == "male":
                                        message(followerLines[i1][0] + "'s " + FolPet + " is already male")
                                    if followerLines[i1][4].lower().rstrip() == "female":
                                        message(
                                            "Successfully changed the gender of " + followerLines[i1][0] + "'s " + folPet + " from " +
                                            "female to male")
                                        followerLines[i1][4] = "male"
                                if text.split()[1].lower().rstrip() == "female":
                                    if followerLines[i1][4].lower().rstrip() == "female":
                                        message(followerLines[i1][0] + "'s " + FolPet + " is already female")
                                    if followerLines[i1][4].lower().rstrip() == "male":
                                        message(
                                            "Successfully changed the gender of " + followerLines[i1][0] + "'s " + FolPet + " from " +
                                            "male to female")
                                        followerLines[i1][4] = "female"
                                if not text.split()[1].lower().rstrip() == "male":
                                    if not text.split()[1].lower().rstrip() == "female":
                                        message("The gender can only be male or female")
                                owner = True
                        csvfile = open('followerDataNew.csv', "wb")
                        followerDataWriter = csv.writer(csvfile, delimiter=",")
                        followerDataWriter.writerows(followerLines)
                        csvfile.close()
                        os.remove('followerData.csv')
                        os.rename('followerDataNew.csv', 'followerData.csv')
                        if owner == False:
                            message("You cannot change the gender of other people's " + FolPetPlural)
                    except IndexError:
                        print message("Did you remember to '!batgenderchange <new gender>'?")
                        print "batgenderchange error"
                        pass
                elif "!elffamilychange" in firstStr:
                    try:
                        owner = False
                        if (len(text.lower().split()[1].encode("ascii"))) <= 16:
                            for i1 in range(len(subscriberLines)):
                                if subscriberLines[i1][0].rstrip().lower() == username.rstrip().lower():
                                    csvfile = open('subscriberData.csv', "rb")
                                    subscriberDataReader = csv.reader(csvfile, delimiter=",")
                                    subscriberLines = list(subscriberDataReader)
                                    csvfile.close()
                                    oldFamilyName = subscriberLines[i1][7]
                                    subscriberLines[i1][7] = text.split()[1]
                                    for i in range(1):
                                        message("Successfully changed family " + oldFamilyName + " to family " +
                                                subscriberLines[i1][7])
                                    csvfile = open('subscriberDataNew.csv', "wb")
                                    subscriberDataWriter = csv.writer(csvfile, delimiter=",")
                                    subscriberDataWriter.writerows(subscriberLines)
                                    csvfile.close()
                                    os.remove('subscriberData.csv')
                                    os.rename('subscriberDataNew.csv', 'subscriberData.csv')
                                    owner = True
                        elif (len(text.lower().split()[1].encode("ascii"))) > 16:
                            message("Family name cannot be longer than 16 characters")
                            owner = True
                        if owner == False:
                            message("You cannot change the family of other people's " + SubPetPlural)
                    except IndexError:
                        message("Did you remember to write '!elffamilychange <new last name>'?")
                        print "elffamilychange failed"
                    except UnicodeEncodeError:
                        print message("You cannot use one of those characters")
                        print ("UnicodeEncodeError")

                elif "!elfgenderchange" in firstStr:
                    try:
                        csvfile = open('subscriberData.csv', "rb")
                        subscriberDataReader = csv.reader(csvfile, delimiter=",")
                        subscriberLines = list(subscriberDataReader)
                        csvfile.close()
                        owner = False
                        for i1 in range(len(subscriberLines)):
                            if subscriberLines[i1][0].rstrip().lower() == username.rstrip().lower():
                                for i2 in range(len(subscriberLines[i1][0:]))[9::2]:
                                    if text.lower().split()[1] == subscriberLines[i1][i2].lower():
                                        genderIndex = (int(i2) + 1)
                                        if text.split()[
                                            2].lower().rstrip() == "male" or text.split()[
                                            2].lower().rstrip() == "female" or text.split()[
                                            2].lower().rstrip() == "androgynous":
                                            message(
                                                "Successfully changed the gender of " + subscriberLines[i1][i2] + " from " +
                                                subscriberLines[i1][genderIndex] + " to " + text.split()[2])
                                            subscriberLines[i1][genderIndex] = text.split()[2]
                                        if not text.split()[
                                            2].lower().rstrip() == "male" or text.split()[
                                            2].lower().rstrip() == "female" or text.split()[
                                            2].lower().rstrip() == "androgynous":
                                            message("The gender can only be male, female or androgynous")
                                        owner = True
                        csvfile = open('subscriberDataNew.csv', "wb")
                        subscriberDataWriter = csv.writer(csvfile, delimiter=",")
                        subscriberDataWriter.writerows(subscriberLines)
                        csvfile.close()
                        os.remove('subscriberData.csv')
                        os.rename('subscriberDataNew.csv', 'subscriberData.csv')
                        if owner == False:
                            message("You cannot change the gender of other people's " + SubPetPlural)
                    except IndexError:
                        message("Did you remember to write '!elfgenderchange <first name> <gender>'?")
                        print "elfnamechange failed"
        if "USERNOTICE" in data:
            try:
                print "Response: " + response.rstrip("/r/n")
                username = re.search(r'(?<=display-name=)\w+', response).group(0)
                msgId = re.search(r'(?<=msg-id=)(.*?);', response).group(1)
                systemMsg = re.search(r'(?<=system-msg=)(.*?);', response).group(1)
                try:
                    global text
                    text = re.search(r'(?<=USERNOTICE)\W+\w+\s\:(.*)', response).group(1)
                except Exception, e:
                    print "text failed"
                    print str(e)
                if msgId == "ritual":
                    message("Welcome " + username + "! " + text.encode('ascii', 'ignore'))
                elif msgId == "raid":
                    message("Raiders are flying through the cave and climbing up the tree!")
                elif msgId == "sub":
                    msgParamSubPlan = re.search(r'(?<=msg-param-sub-plan=)\w+', response).group(0)
                    csvfile = open('subscriberData.csv', "rb")
                    subscriberDataReader = csv.reader(csvfile, delimiter=",")
                    subscriberLines = list(subscriberDataReader)
                    csvfile.close()
                    for i in range(len(subscriberLines)):
                        if subscriberLines[i][0].rstrip().lower() == username.rstrip().lower():
                            subscriberLines[i][1] = 1
                    message("Spam all the hearts you have!!! ridgurHeart ridgurHeart ridgurHeart ridgurHeart ridgurHeart ridgurHeart")
                elif msgId == "resub":
                    msgParamSubPlan = re.search(r'(?<=msg-param-sub-plan=)\w+', response).group(0)
                    csvfile = open('subscriberData.csv', "rb")
                    subscriberDataReader = csv.reader(csvfile, delimiter=",")
                    subscriberLines = list(subscriberDataReader)
                    csvfile.close()
                    subStreak = re.search(r'for\\s(\d+)', systemMsg).group(1)
                    for i in range(len(subscriberLines)):
                        if subscriberLines[i][0].rstrip().lower() == username.rstrip().lower():
                            subscriberLines[i][1] = subStreak
                    message("Spam all the hearts you have!!! ridgurHeart ridgurHeart ridgurHeart ridgurHeart ridgurHeart ridgurHeart")
                elif msgId == "subgift":
                    recipientUserName = re.search(r'(?<=msg-param-recipient-display-name=)(.*?);', response).group(1)
                    msgParamSubPlan = re.search(r'(?<=msg-param-sub-plan=)\w+', response).group(0)
                    message("Thank you so much " + username + " for gifting that tier " +
                            msgParamSubPlan.encode('ascii', 'ignore')[0] + " sub to " + recipientUserName + " ridgurHeart ridgurHeart ridgurHeart ridgurHeart ridgurHeart ridgurHeart")
                    csvfile = open('subscriberData.csv', "rb")
                    subscriberDataReader = csv.reader(csvfile, delimiter=",")
                    subscriberLines = list(subscriberDataReader)
                    csvfile.close()
                    newContributer = True
                    for i1 in range(len(subscriberLines)):
                        if subscriberLines[i1][0].rstrip().lower() == username.rstrip().lower():
                            newContributer = False
                            if subscriberLines[i1][3] == "":
                                subscriberLines[i1][3] = "0"
                            if subscriberLines[i1][4] == "":
                                subscriberLines[i1][4] = "0"
                            subscriberLines[i1][3] = str(int(subscriberLines[i1][3]) + 1)
                            if msgParamSubPlan.encode('ascii', 'ignore') == "1000":
                                subscriberLines[i1][4] = str(int(subscriberLines[i1][4]) + 1)
                            if msgParamSubPlan.encode('ascii', 'ignore') == "2000":
                                subscriberLines[i1][4] = str(int(subscriberLines[i1][4]) + 2)
                            if msgParamSubPlan.encode('ascii', 'ignore') == "3000":
                                subscriberLines[i1][4] = str(int(subscriberLines[i1][4]) + 6)
                    if newContributer == True:
                        if msgParamSubPlan.encode('ascii', 'ignore') == "1000":
                            subscriberLines.append(
                                [username] + ["0"] + ["0"] + ["1"] + ["1"] + ["0"] + ([""] * 4))
                        if msgParamSubPlan.encode('ascii', 'ignore') == "2000":
                            subscriberLines.append(
                                [username] + ["0"] + ["0"] + ["1"] + ["2"] + ["0"] + ([""] * 4))
                        if msgParamSubPlan.encode('ascii', 'ignore') == "3000":
                            subscriberLines.append(
                                [username] + ["0"] + ["0"] + ["1"] + ["6"] + ["0"] + ([""] * 4))
                elif msgId == "anonsubgift":
                    recipientUserName = re.search(r'(?<=msg-param-recipient-user-name=)(.*?);', response).group(1)
                    msgParamSubPlan = re.search(r'(?<=msg-param-sub-plan=)\w+', response).group(0)
                    message("Thank you for giving that anonymous tier " + msgParamSubPlan.encode('ascii', 'ignore')[
                        0] + " subgift to " + recipientUserName + "ridgurHeart ridgurHeart ridgurHeart ridgurHeart ridgurHeart ridgurHeart")

                # Write back subscriber lines
                csvfile = open('subscriberDataNew.csv', "wb")
                subscriberDataWriter = csv.writer(csvfile, delimiter=",")
                subscriberDataWriter.writerows(subscriberLines)
                csvfile.close()
                os.remove('subscriberData.csv')
                os.rename('subscriberDataNew.csv', 'subscriberData.csv')
            except Exception, e:
                print str(e)
        else:
            try:
                if not "PRIVMSG" in data:
                    print "Response: " + response.rstrip("\r\n")  ### These are all the non message related responses
                if response == "PING :tmi.twitch.tv\r\n":
                    try:
                        s.send("PONG :tmi.twitch.tv\r\n".encode("utf-8"))
                        print "Reply: PONG :tmi.twitch.tv"
                    except IndexError:
                        pass
                    except Exception, e:
                        print("Pong error")
                        print(str(e))
                if response == "":
                    print "lost connection"
                    exit()
                if "PRIVMSG" in data:
                    username = re.search(r'(?<=display-name=)\w+', response).group(0)
                    text = re.search(r'(?<=PRIVMSG)\W+\w+\s\:(.*)', response).group(1)
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
        sleep(20/30)
    except IndexError:
        pass
    except Exception, e:
        print "An error just occurred"
        print str(e)
        s.shutdown(1)
        s.close()
        s = socket.socket()
        s.connect((Host, Port))
        s.send("PASS {}\r\n".format("oauth:" + FollowerToken).encode("utf-8"))
        s.send("NICK {}\r\n".format(Nickname.lower()).encode("utf-8"))
        s.send("JOIN {}\r\n".format(Channel).encode("utf-8"))
        s.send("CAP REQ :twitch.tv/membership\r\n")
        s.send("CAP REQ :twitch.tv/commands\r\n")
        s.send("CAP REQ :twitch.tv/tags\r\n")
        pass
