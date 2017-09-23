import datetime
import time
# import yaml
import sys
# import webbrowser
# import os
from itertools import count
from multiprocessing import Process
import pdb

from PIL import ImageGrab
import Pics
# import smtplib
import pyautogui
# from pywinauto.application import Application
import win32gui
import re
from random import randint

# def get_config_file(file):
#     f = open(file)
#     Pics = yaml.safe_load(f)
#     f.close()
#     return Pics
#
# Pics = get_config_file('Pics.yaml')


# connect to another process spawned by explorer.exe
# app = Application(backend="uia").connect(path="firefox.exe", title="FUT")
# print(app.is_process_running())

# print(pyautogui.getWindows())
# windows = pyautogui.getWindow('FIFA Football | FUT Web App | EA SPORTS - Mozilla Firefox')


class WindowMgr:
    """Encapsulates some calls to the winapi for window management"""

    def __init__(self):
        """Constructor"""
        self._handle = None

    def find_window(self, class_name, window_name=None):
        """find a window by its class_name"""
        self._handle = win32gui.FindWindow(class_name, window_name)

    def _window_enum_callback(self, hwnd, wildcard):
        """Pass to win32gui.EnumWindows() to check all the opened windows"""
        if re.match(wildcard, str(win32gui.GetWindowText(hwnd))) is not None:
            self._handle = hwnd

    def find_window_wildcard(self, wildcard):
        self._handle = None
        win32gui.EnumWindows(self._window_enum_callback, wildcard)

    def set_foreground(self):
        """put the window in the foreground"""

        if self._handle is None:
            raise Exception("Windows handle not found, Please make sure that Mozilla FUT page is opened")
        win32gui.SetForegroundWindow(self._handle)

    def getWindowSizes(self):
        """Return a list of tuples (handler, (width, height)) for each real window"""
        browser_size_v = win32gui.GetWindowRect(self._handle)
        print('Browser size is %s' % str(browser_size_v))
        return browser_size_v

    def getWindowTopSizes(self):
        """Return a list of tuples (handler, (width, height)) for each real window"""
        browser_size_top_v = win32gui.GetWindowRect(self._handle)
        browser_size_top_v = list(browser_size_top_v)
        browser_size_top_v[3] = int(browser_size_top_v[3] / 2)
        browser_size_top_v = tuple(browser_size_top_v)
        print('Browser TOP size is %s ' % str(browser_size_top_v))
        return browser_size_top_v

    def getWindowBottomSizes(self):
        """Return a list of tuples (handler, (width, height)) for each real window"""
        browser_size_bottom_v = win32gui.GetWindowRect(self._handle)
        browser_size_bottom_v = list(browser_size_bottom_v)
        browser_size_bottom_v[1] = int(browser_size_bottom_v[3] / 2) + browser_size_bottom_v[1]
        browser_size_bottom_v = tuple(browser_size_bottom_v)
        print('Browser BOTTOM size is %s ' % str(browser_size_bottom_v))
        return browser_size_bottom_v

    def getWindowLeftSizes(self):
        """Return a list of tuples (handler, (width, height)) for each real window"""
        browser_size_top_l = win32gui.GetWindowRect(self._handle)
        browser_size_top_l = list(browser_size_top_l)
        browser_size_top_l[2] = int(browser_size_top_l[2] / 2)
        browser_size_top_l = tuple(browser_size_top_l)
        print('Browser Left size is %s ' % str(browser_size_top_l))
        return browser_size_top_l

    def getWindowRightSizes(self):
        """Return a list of tuples (handler, (width, height)) for each real window"""
        browser_size_right = win32gui.GetWindowRect(self._handle)
        browser_size_right = list(browser_size_right)
        browser_size_right[0] = int(browser_size_right[0] + int(browser_size_right[2]/2))
        browser_size_right = tuple(browser_size_right)
        print('Browser Right size is %s ' % str(browser_size_right))
        return browser_size_right

def timing(f):
    def wrap(*args):
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()
        print('%s function took %0.3f ms' % (f.__name__, (time2 - time1) * 1000.0))
        return ret

    return wrap


def take_screenshot(prefix, global_browser_size):
    current_time = str(datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')) + '_' + prefix + '_' ".jpg"
    ImageGrab.grab(bbox=global_browser_size).save(current_time, "JPEG")
    print("Saved screenshot: %s" % current_time)


class Main:

    def __init__(self):
        w = WindowMgr()
        w.find_window_wildcard(".*EA SPORTS.*")
        w.set_foreground()
        self.global_browser_size = w.getWindowSizes()
        self.global_browser_size_top = w.getWindowTopSizes()
        self.global_browser_size_bottom = w.getWindowBottomSizes()
        self.global_browser_size_left = w.getWindowLeftSizes()
        self.global_browser_size_right = w.getWindowRightSizes()

    @timing
    def wait_for_picture(self, picture, global_browser_size, wait_time=5, screenshot=False):
        print("Waiting for picture: %s for %s seconds" % (picture, str(wait_time)))
        coordinates = pyautogui.locateOnScreen(picture, wait_time, region=global_browser_size, grayscale=True)
        if coordinates is None:
            print("!!!!!!!!!!!!!Picture: %s not found!!!!!!!!!!!!!" % picture)
            if screenshot:
                take_screenshot(picture, global_browser_size)
                return None
        else:
            print('*******Found: %s at %s *******' % (picture, coordinates))
            return coordinates

    @timing
    def wait_for_list_of_pictures(self, list_to_search, global_browser_size, wait_time=5, screenshot=False):
        coordinates = None
        for picture in list_to_search:
            print("Waiting for picture: %s for %s seconds" % (picture, str(wait_time)))
            coordinates = pyautogui.locateOnScreen(picture, wait_time, region=global_browser_size, grayscale=True)
            if coordinates is None:
                print("!!!!!!!!!!!!!Picture: %s not found!!!!!!!!!!!!!, Searching for second picture" % picture)
                if screenshot:
                    take_screenshot(picture, global_browser_size)
            else:
                print('*******Found: %s at %s *******' % (picture, coordinates))
                break
        return coordinates

    @staticmethod
    def click_on_center(coordinates):
        if coordinates is None:
            print('Exiting as NONE!!!')
            sys.exit()
        coordinates = pyautogui.center(coordinates)
        pyautogui.click(coordinates[0], coordinates[1])

    @staticmethod
    def click_right_down_corner(coordinates, vertical=0, horizontal=0):
        if coordinates is None:
            print('Exiting as NONE!!!')
            sys.exit()
        coordinates = (coordinates[0] + coordinates[2] + horizontal, coordinates[1] + coordinates[3] + vertical)
        pyautogui.click(coordinates)

    @staticmethod
    @timing
    def count_contracts(global_browser_size):
        print('SIZE for searching contracts: %s' % str(global_browser_size))
        locate_players = pyautogui.locateAllOnScreen(Pics.Tabs.TransferMarket.Consumables.Contracts.contract_player_small, region=global_browser_size, grayscale=True)
        print('Found the next items: %s ' % str(list(locate_players)))
        time.sleep(3)
        #print(locate_players[-1])
        #Main.click_on_center(locate_players[-1])
        #print('LIST OF PLAYERS:')
        counter = 0
        for player in locate_players:
            counter = + 1
            print(counter)


            print("Found")
        pyautogui.scroll(-1000)
          # print("NEW PARALLEL starting")
    # search_for_contract_second = Search()
    # p10 = Process(target=search_for_contract_second.wait_for_search_result3)
    # p10.start()
    # print("NEW PARALLEL ending")

class Search(Main):

    def go_to_search(self):
        Main.click_on_center(Main.wait_for_list_of_pictures(self, (Pics.Tabs.transfers_selected, Pics.Tabs.transfers), self.global_browser_size_left, 2))

        Main.click_on_center(Main.wait_for_picture(self, Pics.Tabs.TransferMarket.search_the_transfer_market, self.global_browser_size_top, 2))
        Main.click_on_center(Main.wait_for_picture(self, Pics.Tabs.TransferMarket.reset_button, self.global_browser_size_bottom))

        Main.click_on_center(Main.wait_for_list_of_pictures(self, (Pics.Tabs.TransferMarket.consumables_selected, Pics.Tabs.TransferMarket.consumables), self.global_browser_size_top, 3))
        Main.click_on_center(Main.wait_for_picture(self, Pics.Tabs.TransferMarket.Consumables.type_player_training_big, self.global_browser_size_top, 3))
        #Main.click_on_center(Main.wait_for_picture(self, Pics.Tabs.TransferMarket.Consumables.type_player_training, self.global_browser_size, 5))
        pyautogui.moveRel(80, 80, duration=0.3)
        pyautogui.scroll(-100)
        #pdb.set_trace()
        Main.click_on_center(Main.wait_for_picture(self, Pics.Tabs.TransferMarket.Consumables.type_contracts, self.global_browser_size))
        Main.click_on_center(Main.wait_for_picture(self, Pics.Tabs.TransferMarket.Consumables.Quality.quality, self.global_browser_size))
        Main.click_on_center(Main.wait_for_picture(self, Pics.Tabs.TransferMarket.Consumables.Quality.quality_gold, self.global_browser_size))
        pyautogui.moveRel(-200, -200, duration=0.1)

        Main.click_on_center(Main.wait_for_picture(self, Pics.Tabs.TransferMarket.Pricing.bid_price, self.global_browser_size))
        pyautogui.typewrite(['tab'], interval=0.1)
        pyautogui.typewrite(['tab'], interval=0.1)
        pyautogui.typewrite(['tab'], interval=0.1)
        pyautogui.typewrite('200', interval=0.1)

        Main.click_on_center(Main.wait_for_picture(self, Pics.Tabs.TransferMarket.search_button, self.global_browser_size))

        Main.wait_for_picture(self, Pics.Tabs.TransferMarket.Consumables.Contracts.watch, self.global_browser_size_top)

        self.count_contracts(self.global_browser_size)
        #pdb.set_trace()
        print('doing SEARCH')


# locate_players = pyautogui.locateAllOnScreen(Pics.Tabs.TransferMarket.Consumables.Contracts.contract_player_small, region=(0, 0, 999, 1400), grayscale=True)
# print(len(list(locate_players)))

if __name__ == '__main__':

    # webbrowser.open('https://www.easports.com/fifa/ultimate-team/web-app')

    run = 0
    while True:
        run = run + 1
        print(run)
        search_for_contract = Search()
        search_for_contract.go_to_search()
        print('DONE')
        time.sleep(randint(0, 9))
