from Fixed import SSID, PASSWORD, TOKEN, TELEGRAMID, GITURL
from picodate import update
import utelegram

## Check for updates
update(GITURL, SSID, PASSWORD)

#Initialization
utelegram_config = {
    'token': TOKEN
}
print('Staritng Telegram Bot')
bot = utelegram.ubot(utelegram_config['token'])
bot.send(TELEGRAMID, 'Bot Online')