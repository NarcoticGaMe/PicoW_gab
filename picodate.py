from ota import OTAUpdater

def update(GitURL, SSID, PASSWORD):
    firmware_url = GitURL
    ota_updater = OTAUpdater(SSID, PASSWORD, firmware_url, "main.py")
    ota_updater.download_and_install_update_if_available()