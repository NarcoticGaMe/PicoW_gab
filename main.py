from Fixed import SSID, PASSWORD, TOKEN, TELEGRAMID, GITURL
from picodate import update
import utelegram

from picozero import LED
from time import sleep

## Check for updates
# update(GITURL, SSID, PASSWORD)


##
Green_led = LED(11)
Yellow_led = LED(12)
Red_led = LED(13)

#Initialization
utelegram_config = {
    'token': TOKEN
}
print('Staritng Telegram Bot')
bot = utelegram.ubot(utelegram_config['token'])
bot.send(TELEGRAMID, 'Bot Online')

def get_message(message):
    bot.send(message['message']['chat']['id'], message['message']['text'].upper())

def reply_red(message):
    Red_led.toggle()
def reply_green(message):
    Green_led.toggle()
def reply_yellow(message):
    Yellow_led.toggle()

bot.register('/red', reply_red)
bot.register('/yellow', reply_yellow)
bot.register('/green', reply_green)
bot.set_default_handler(get_message)
bot.listen()