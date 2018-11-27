<a href="http://www.twitch.tv/ridgure"><img src="https://pbs.twimg.com/profile_banners/4144666635/1497981943/1500x500" title="FVCproductions" alt="FVCproductions"></a>

<h1 align="center">
  <br>
  <a href="http://www.twitch.tv/ridgure"><img src="https://pbs.twimg.com/profile_images/965416492924891136/N-EvLzcd_400x400.jpg" alt="Markdownify" width="200"></a>
  <br>
  Riboture
  <br>
</h1>

<h4 align="center">An IRC bot written in python and made for my Twitch channel <a href="https://twitch.tv/ridgure" target="_blank">Twitch.tv/Ridgure</a>.</h4>

<p align="center">
  <a href="#key-features">Key Features</a> •
  <a href="#getting-started">Getting started</a> •
  <a href="#acknowledgements">Acknowledgements</a> •
  <a href="#connect">Connect</a>
</p>

## Features:

**Commands:**

###### Commands for everyone:
!add,
!bellyrub,
!divide,
!facebook,
!fc, 
!instagram
!multipy,
!oclock,
!pack, 
!social,
!shout 
!smile, 
!timemeout,
!twitter
!uptime
!namechange

###### Broadcaster commands:
!raid

###### User specific commands:
!lick

**Automated functions:**

Follower notification,
Text to file, Cobble

## Getting started

**Clone**

Clone this repo to your local machine using ```https://github.com/Ridgure/TwitchBot.git```

**Setup**

In order to be able to run the bot add a file config.py that looks something like this and go through the steps below:

```
HOST = "irc.twitch.tv"                                  # the Twitch IRC server
PORT = 6667                                             # always use port 6667!
NICK = "riboture"                                       # your bots Twitch username, lowercase
PASS = "<insert Oauth here>"                            # your Twitch OAuth token
CHAN = "#ridgure"                                       # the channel you want to join

User_ID_ridgure = "106586349"
User_ID_riboture = "109949586"
User_ID_princess___lissy = "124936690"
Client_ID = "<Insert client id here>"
Client_Secret = "<Insert client secret here>"
```

- Create a Twitch account with the name of your bot
- Register your application on the [Twitch developer site](https://glass.twitch.tv/login)
  - Set the Name to the name of the account you just created
  - Set the redirect uri to http://localhost
  - Set the application directory to Chat Bot
  - Agree to the terms and conditions
  - Get a Client_ID and a Client_Secret
- generate an Oauth at this address https://twitchapps.com/tmi/

**Prerequisites**

You will need to install these things to run the bot

- Python 2.7.14
- Libraries:
  - Requests
  
**Running the bot**

Run [bot.py](docs/bot.py) by going to its location and running this command:

```
python bot.py
```

## Acknowledgements:

This whole project started off with this [Instructables article](https://www.instructables.com/id/Twitchtv-Moderator-Bot/)

Other interesting projects to check out:

[PythonBot](https://github.com/ZERG3R/PythonBot) by ZERG3R on Twitch as [ZERG3R](https//:twitch.tv/ZERG3R)


## Connect:

**Twitch**

See the bot in action when I am live on [Twitch](https://twitch.tv/ridgure) over at [Twitch.tv/Ridgure](https://twitch.tv/ridgure)

**Social media**

Please follow me on:
[Facebook](https://www.Facebook.com/ridgure), 
[Twitter](https://www.Twitter.com/ridgure) and
[Instagram](https://www.Instagram.com/rigidstructure)