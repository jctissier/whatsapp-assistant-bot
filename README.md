# WhatsApp Assistant Bot

## Demo
<img src="https://github.com/jctissier/whatsapp-assistant-bot/blob/master/documentation/pics/whatsappbotdemo.gif" width="640" height="480" />

A personal WhatsApp assistant bot that will help you search anything on the web:
<br><i>script is automated with selenium, the bot will check the chat and reply on valid commands</i>
  * Search Google
  * Search Google Images
  * Directions from Google Maps
     * User can set {origin}, {destination} and {travelmode}

**If bot fails when you first run it, please check and update if the class attribute for Line 13 has changed:**
```
MESSAGE_BUBBLE_CLASS_NAME = "_13mgZ"
```
**1) Inspect the Whatsapp text bubble element**
<br>
**2) Extract the class attribute and update Line 13**

# TODOs 

## Features
- [x] Bot can poll 1 conversation
- [ ] Bot can poll multiple assigned conversations
- [x] Search Google
- [x] Search Google Images
- [x] Search Google Maps
- [ ] Google Maps directions from user's location

## Down the road
- [ ] Remotely access the QR code
- [ ] Image to text analysis w/ Pytesseract 
- [ ] Flask server running headless Chrome


## Step by Step Guide
I have been receiving a lot of requests about what to do when the bot starts running. Here is a step by step example:
1. Once the bot is running, it should automatically open chrome and display the whatsapp web QR code. Once you scan it, you should be able to see a list of your conversations, choose the one you want to test with. 
![QR Code Scan](https://github.com/jctissier/whatsapp-assistant-bot/blob/master/documentation/pics/tutorial%20-%20run%20bot.png)

2. **Line 293 of whatsapp_assistant_bot.py** can be changed to read incoming messages (other person in conversation) vs outgoing messages (your own messages)
```
text_bubbles = driver.find_elements_by_class_name("message-out")  # message-in = incoming, message-out = outgoing
```
![Incoming vs Outgoing](https://github.com/jctissier/whatsapp-assistant-bot/blob/master/documentation/pics/tutorial%20-%20features.png)

3. Example of sending commands and the bot scanning for outgoing messages (my messages)
![Test outgoing](https://github.com/jctissier/whatsapp-assistant-bot/blob/master/documentation/pics/tutorial%20-%20sending%20or%20receiving%20messages.png)

4. Example of asking the bot to google something. Since the bot is running on your computer, chrome will be automated by selenium and you will see a chrome page open, a screenshot will be taken and attached to the chat.
![Test Google](https://github.com/jctissier/whatsapp-assistant-bot/blob/master/documentation/pics/tutorial%20-%20google%20feature.png)

## What You'll Need
1. Install Chromedriver and make sure the Setup is completed (add the path to the chromedriver executable)

**Chromedriver**

* [Setup chromedriver](http://www.kenst.com/2015/03/installing-chromedriver-on-mac-osx/)
* [Download chromedriver](https://sites.google.com/a/chromium.org/chromedriver/)

2. Install Selenium from your command line
**Selenium**
```
$ pip3 install selenium
```

## How to Run
Clone the repo
```
$ git clone https://github.com/jctissier/whatsapp-assistant-bot.git
$ cd whatsapp-assistant-bot
$ python3 whatsapp_assistant_bot.py
```

*If you get an error at this stage, it's most likely due to Chromedriver not being installed properly. Repeat the first step.*

Script is running properly if you see **"Bot is active, scan your QR code from your phone's WhatsApp"**
* Scan your QR Code
![QR Code](https://github.com/jctissier/whatsapp-assistant-bot/blob/master/documentation/pics/scan_qr_code_doc.png)
* Select a chat and start sending commands

## Valid Commands
The bot will always send back screenshots of the Chrome browser 
``` 
/google {query}              # Search google text
/images {query}              # Search google images
/maps                        # Directions with Google Maps
    /origin {from where}     # Sub-menus from /maps
    /dest {to where}
    /mode {driving, walking, transit, bicycling}
```

## How Selenium Automates the Bot
I was able to scan incoming/outgoing messages by inspecting the HTML and using selenium to access on class names and xpath
![Scan Messages](https://github.com/jctissier/whatsapp-assistant-bot/blob/master/documentation/pics/chat_history_documentation.png)

**Testing**

You can either create a bot account ([as mentioned below](https://github.com/jctissier/whatsapp-assistant-bot#how-i-use-it)) or you can use your own account to test it. 

* In the function chat_history(), set the first line of the function to "message-out"
   * This allows the bot to only scan for messages sent by yourself
   * You can send commands to yourself and the bot will respond (no need for a spare account)
* "message-in" forces to bot to scan for incoming messages from the other person

**Flowchart for Main Features**
![Flow Chart](https://github.com/jctissier/whatsapp-assistant-bot/blob/master/documentation/flowchart/GoogleResults%20Flowchart.png)

## How I Use It
I run the script from my home computer in Canada and I have a separate WhatsApp account running 24/7. 

You can create a free WhatsApp account if you have a spare/old smartphone. 
* Charge the device 24/7, have it on Wifi and download WhatsApp on it (SIM card is not needed)
* When they ask you to verify your WhatsApp and need a number to text
   * Download one of the many apps on app store which allows you to get a temporary phone number 
      * For example, I use [textPlus](https://textplus.com/) - FREE
      * Generate a free number and use it to verify your bot account
   * For the verification, ask for a call, answer the call and set the password
   * Account should now be created, you can now message the bot to that particular number that was generated with the app
   
There is plenty more that can be done with this bot, but I only needed basic googling. 




## Comments
**Author: Jean-Claude Tissier**<br>
**MIT License**


I created this bot for when I travel since I have unlimited WhatsApp everywhere in the world but no data plan. I needed a way to be able to find directions, search for touristy attractions and general googling necessities in a new city without having data. 

Feel free to grab the code and let me know if you have questions.

*PS: This bot is not meant for spamming and is only meant for personal use.* 
