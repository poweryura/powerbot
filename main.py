import random
import inspect
import datetime
import yaml
import sys
import traceback
import webbrowser
import os
from PIL import ImageGrab
#from Pics import Pics
import smtplib
import pyautogui
#import pywinauto


#webbrowser.open('https://www.easports.com/fifa/ultimate-team/web-app')




def get_config_file(file):
    f = open(file)
    Pics = yaml.safe_load(f)
    f.close()
    return Pics


Pics = get_config_file('Pics.yaml')


class Main:
    def __init__(self):
        pass

    @staticmethod
    def take_screenshot(prefix=''):
        current_time = str(datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')) + prefix+".jpg"
        ImageGrab.grab().save(current_time, "JPEG")
        print("Saved screenshot: %s" % current_time)

    def wait_for_picture(self, picture, time=5, screenshot=True):
        print("Waiting for picture: %s for %s seconds" % (picture, str(time)))
        coordinates = pyautogui.locateOnScreen(picture, time)
        if coordinates is None:
            print("Picture: %s not found" % picture)
            if screenshot:
                self.take_screenshot(picture)
        else:
            print(coordinates)
            coordinates = pyautogui.center(coordinates)
        return coordinates

    def wait_for_list_of_pictures(self, list_to_search, time=5, screenshot=False):
        coordinates = None
        for picture in list_to_search:
            print("Waiting for picture: %s for %s seconds" % (picture, str(time)))
            coordinates = pyautogui.locateOnScreen(picture, time,  grayscale=False)
            if coordinates is None:
                print("Picture: %s not found" % picture)
                if screenshot:
                    self.take_screenshot(picture)
            else:
                print(coordinates)
                coordinates = pyautogui.center(coordinates)
                break
        return coordinates

    @staticmethod
    def click_on_center(coordinates):
        if coordinates is None:
            print('Exiting as NONE!!!')
            sys.exit()
        pyautogui.click(coordinates[0], coordinates[1])


start = Main()
twitter = start.wait_for_picture(Pics['home']['twitter'], 1)
transfers_coo = start.wait_for_list_of_pictures([Pics.transfers_tab_selected, Pics.transfers_tab])
start.click_on_center(transfers_coo)

transfer_market_coo = start.wait_for_list_of_pictures([Pics.transfer_market_selected, Pics.transfer_market])
start.click_on_center(transfer_market_coo)

consumables_coo = start.wait_for_list_of_pictures([Pics.consumables_tab_selected, Pics.consumables_tab])
start.click_on_center(consumables_coo)



