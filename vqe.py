from seleniumbase import SB
import time
import requests
import sys
import requests
import os
import random
import subprocess
from dataclasses import dataclass
from typing import List, Optional

import requests
geo_data = requests.get("http://ip-api.com/json/").json()

latitude = geo_data["lat"]
longitude = geo_data["lon"]
timezone_id = geo_data["timezone"]
language_code = geo_data["countryCode"].lower()  # e.g., 'us' -> 'en-US'
with SB(uc=True, test=True,locale=f"{language_code.upper()}") as deagea:
    deagea.execute_cdp_cmd(
        "Emulation.setGeolocationOverride",
        {
            "latitude": latitude,
            "longitude": longitude,
            "accuracy": 100
        }
    )
    deagea.execute_cdp_cmd(
        "Emulation.setTimezoneOverride",
        {"timezoneId": timezone_id}
    )
    #deagea.set_window_size(resolution.width, resolution.height)
    #"#live-channel-stream-information"
    url = "https://kick.com/brutalles"
    deagea.uc_open_with_reconnect(url, 4)
    deagea.sleep(4)
    deagea.uc_gui_click_captcha()
    deagea.sleep(1)
    deagea.uc_gui_handle_captcha()
    deagea.sleep(4)
    if deagea.is_element_present('button:contains("Accept")'):
        deagea.uc_click('button:contains("Accept")', reconnect_time=4)
    if deagea.is_element_visible('#injected-channel-player'):
        deagea2 = deagea.get_new_driver(undetectable=True)
        deagea2.uc_open_with_reconnect("https://www.twitch.tv/brutalles", 5)
        deagea2.uc_gui_click_captcha()
        deagea2.uc_gui_handle_captcha()
        deagea.sleep(10)
        if deagea2.is_element_present('button:contains("Accept")'):
            deagea2.uc_click('button:contains("Accept")', reconnect_time=4)
        while deagea.is_element_visible('#injected-channel-player'):
            deagea.sleep(100)
        deagea.quit_extra_driver()
    deagea.sleep(1)
    if deagea.is_element_present("#live-channel-stream-information"):
        url = "https://www.twitch.tv/brutalles"
        deagea.uc_open_with_reconnect(url, 5)
        if deagea.is_element_present('button:contains("Accept")'):
            deagea.uc_click('button:contains("Accept")', reconnect_time=4)
        if True:
            deagea2 = deagea.get_new_driver(undetectable=True)
            deagea2.uc_open_with_reconnect("https://kick.com/brutalles", 5)
            deagea.sleep(10)
            if deagea2.is_element_present('button:contains("Accept")'):
                deagea2.uc_click('button:contains("Accept")', reconnect_time=4)
            while deagea.is_element_present("#live-channel-stream-information"):
                deagea.sleep(100)
            deagea.quit_extra_driver()
    deagea.sleep(1)
