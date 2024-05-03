from Fixed import SSID, PASSWORD, TOKEN, TELEGRAMID, GITURL
from picodate import update
import utelegram
from machine import Pin, I2C
from SSD1306 import SSD1306_I2C
from picozero import LED
from time import sleep

## Check for updates
update(GITURL, SSID, PASSWORD)


##Display
WIDTH =128 
HEIGHT= 64
i2c=I2C(0,scl=Pin(17),sda=Pin(16),freq=200000)
oled = SSD1306_I2C(WIDTH,HEIGHT,i2c)
oled.fill(0)
oled.text("Connection to", 0, 0)
oled.text("Telegram ...", 0, 10)
oled.show()

#Initialization
utelegram_config = {
    'token': TOKEN
}
print('Staritng Telegram Bot')
bot = utelegram.ubot(utelegram_config['token'])
oled.text("Connected", 0, 40)
oled.show()
bot.send(TELEGRAMID, 'Bot Online')

def get_message(message):
    bot.send(message['message']['chat']['id'], message['message']['text'].upper())

def check_update(message):
    oled.fill(0)
    oled.text('Searching for new update ...',0,0)
    oled.text('new update ...',0,10)
    oled.show()
    update(GITURL, SSID, PASSWORD)
    oled.text('No new update',0,20)
    oled.show()

bot.set_default_handler(get_message)
bot.register('/update', check_update)
bot.listen()
