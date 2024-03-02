from Fixed import SSID, PASSWORD, TOKEN, TELEGRAMID
from update import update
import utelegram

## Check for updates
update()

#Initialization
utelegram_config = {
    'token': TOKEN
}
print('Staritng Telegram Bot')
bot = utelegram.ubot(utelegram_config['token'])
bot.send(TELEGRAMID, 'Bot Online')