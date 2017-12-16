# whatsapp-assistant-bot

A personal WhatsApp assistant bot that will help you search anything on the web:
<br><i>script is automated with selenium, the bot will check the chat and reply on valid commands</i>
  * Search Google
  * Search Google Images
  * Directions from Google Maps
     * User can set {origin}, {destination} and {travelmode}

## What You'll Need
**Chromedriver**

* [Setup chromedriver](http://www.kenst.com/2015/03/installing-chromedriver-on-mac-osx/)
* [Download chromedriver](https://sites.google.com/a/chromium.org/chromedriver/)

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

*If you get an error at this stage, it's most likely due to Chromedriver not being installed properly.*

Script is running properly if you see **"Bot is active, scan your QR code from your phone's WhatsApp"**
* Scan your QR Code
![QR Code](https://github.com/jctissier/whatsapp-assistant-bot/blob/master/documentation/pics/scan_qr_code_doc.png)
