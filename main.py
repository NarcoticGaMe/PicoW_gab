from Fixed import SSID, PASSWORD, TOKEN, TELEGRAMID, GITURL
from picodate import update
import utelegram
from machine import Pin, I2C
from SSD1306 import SSD1306_I2C
from time import sleep

## Check for updates
Temperature = 40



##Display
WIDTH =128 
HEIGHT= 64
i2c=I2C(0,scl=Pin(17),sda=Pin(16),freq=200000)
oled = SSD1306_I2C(WIDTH,HEIGHT,i2c)
oled.fill(0)
oled.text("Checking for", 0, 0)
oled.text("update...", 0, 10)
update(GITURL, SSID, PASSWORD)
oled.text("V", 110, 10)
oled.text("Connection to", 0, 20)
oled.text("Telegram...", 0, 30)
oled.show()

#Initialization
utelegram_config = {
    'token': TOKEN
}
print('Staritng Telegram Bot')
bot = utelegram.ubot(utelegram_config['token'])
print('Connected')
oled.text("V", 110, 30)
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

def change_display(message):
    bot.send(TELEGRAMID, 'Value?')
    mm = bot.read_messages()
    temp = mm[0]['message']['text']
    oled.rect(0,40,WIDTH,8,0,True)
    oled.text(temp,0,40)
    oled.show()

bot.set_default_handler(get_message)
bot.register('/update', check_update)
bot.register('/change', change_display)
while True:
    try:
        bot.listen()
    except Exception as error:
        print(error)
