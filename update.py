from ota import OTAUpdater
from Fixed import SSID, PASSWORD, URL

def update():
    firmware_url = URL
    ota_updater = OTAUpdater(SSID, PASSWORD, firmware_url, "main.py")
    ota_updater.download_and_install_update_if_available()