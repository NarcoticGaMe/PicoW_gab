from ota import OTAUpdater
from Fixed import SSID, PASSWORD, TOKEN, TELEGRAMID
import utelegram

debug = True

## Check for updates
firmware_url = "https://raw.githubusercontent.com/NarcoticGaMe/PicoW_gab/main/"
ota_updater = OTAUpdater(SSID, PASSWORD, firmware_url, "main.py")
ota_updater.download_and_install_update_if_available()

#Initialization
utelegram_config = {
    'token': TOKEN
}
print('Staritng Telegram Bot')
bot = utelegram.ubot(utelegram_config['token'])
bot.send(TELEGRAMID, 'Bot Online')