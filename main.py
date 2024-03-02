from ota import OTAUpdater
from Fixed import SSID, PASSWORD

firmware_url = "https://raw.githubusercontent.com/NarcoticGaMe/PicoW_gab/main"
ota_updater = OTAUpdater(SSID, PASSWORD, firmware_url, "test.py")
ota_updater.download_and_install_update_if_available()

