from Fixed import SSID, PASSWORD, TOKEN, TELEGRAMID, GITURL
from picodate import update
import utelegram

from picozero import LED
from time import sleep

## Check for updates
update(GITURL, SSID, PASSWORD)


#Initialization
utelegram_config = {
    'token': TOKEN
}
print('Staritng Telegram Bot')
bot = utelegram.ubot(utelegram_config['token'])
bot.send(TELEGRAMID, 'Bot Online')

def get_message(message):
    bot.send(message['message']['chat']['id'], message['message']['text'].upper())
