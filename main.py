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


def check_default_install_path():
    default_install_path = r'C:\Program Files\CrystalDiskMark8'
    is_default_install = False
    logging.info("Installed via default path? " + default_install_path)
    if os.path.isdir(default_install_path):
        logging.info("Application is installed in default directory")
        is_default_install = True
    else:
        logging.error("Application IS NOT installed in default directory!")
    return is_default_install
    pass


def is_in_default_path(is_default_install_path):
    logging.INFO(
        "Please uninstall and re-install via default directory path")
    logging.INFO("Now closing automation...")
    sys.exit()
    pass


def launchCDM():
    versionx64 = r"C:\Program Files\CrystalDiskMark8\DiskMark64.exe"
    versionx32 = r"C:\Program Files\CrystalDiskMark8\DiskMark32.exe"
    if os.path.isfile(versionx64):
        logging.info("Opeing " + versionx64)
        subprocess.Popen(versionx64)
    else:
        logging.info("Opeing " + versionx32)
        subprocess.Popen(versionx32)
    pass


def main():
    logging.info("Starting Crystal Disk Mark Automation...")
    is_in_default_path(check_default_install_path())
    launchCDM()
    pass


if __name__ == "__main__":
    main()
    pass
