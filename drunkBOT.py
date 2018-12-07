import json
import telepot
import time
import urllib2

#This function will coordinate and refresh the sending of the messages
def refresh(msg):
    print(msg['text'])
    if msg['text'] == "/start":
        GLOBAL = 1
    if msg['text'] == "/end":
        GLOBAL = 0
    if GLOBAL == 1:
        content_type, chat_type, chat_id = telepot.glance(msg)
#informations about the channel on thingspeak
        READ_API_KEY='0P9G8UILTJ3XOAT4'
        CHANNEL_ID= '641127'

        
        TS = urllib2.urlopen("http://api.thingspeak.com/channels/%s/feeds/last.json?api_key=%s" \
                       % (CHANNEL_ID,READ_API_KEY))
        response = TS.read()
        data=json.loads(response)
        if data == -1:
            print("No data available yet")
            time.sleep(10)
        else:
            a = int(data['field1'])
            if a >= 3000:
                bot.sendMessage(chat_id, "Warning, the driver is drunk!")
            if a >= 2000 and a < 3000:
                bot.sendMessage(chat_id, "Warning, the driver is almost drunk!")
            if a < 2000:
                bot.sendMessage(chat_id, "The driver is not drunk!")
        TS.close()
        time.sleep(10)
            
#information about the bot        
bot = telepot.Bot("758882569:AAFEPnuUKOD6cgyiZuHZeB5b07wJBX-ymjE")
GLOBAL = 0
bot.message_loop(refresh)

while True:
    pass
