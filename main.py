# ' CrystalDiskMark 8.0.4 x64 [Admin] '
# ' CrystalDiskMark 8.0.4 x86 [Admin] '
# ' CrystalDiskMark 8.0.4 x64 '
# ' CrystalDiskMark 8.0.4 x86 '
from datetime import date
import logging
import os
import pyautogui
import struct
import subprocess
import sys
import time

TODAYSDATE = str(date.today()).replace(
    '-', '')  # Grabs current date as YYYYMMDD

FORMAT = '[%(asctime)s]-[%(funcName)s]-[%(levelname)s] - %(message)s'
logging.basicConfig(
    encoding='utf-8',
    filename=TODAYSDATE+'_cdm_automation.log',
    format=FORMAT,
    level=logging.INFO
)


def main():
    logging.info("Starting Crystal Disk Mark Automation...")
    is_in_default_path(check_default_install_path())
    launchCDM()
    pass


if __name__ == "__main__":
    main()
    pass
