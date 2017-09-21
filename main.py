import datetime
import time
# import yaml
import sys
# import webbrowser
# import os
from itertools import count
from multiprocessing import Process

from PIL import ImageGrab
import Pics
# import smtplib
import pyautogui
# from pywinauto.application import Application
import win32gui
import re


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

    @staticmethod
    @timing
    def wait_for_picture(picture, global_browser_size, wait_time=1, screenshot=False):
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

    # @staticmethod
    # @timing
    # def wait_for_list_of_pictures(list_to_search, wait_time=1, screenshot=False):
    #     coordinates = None
    #     for picture in list_to_search:
    #         print("Waiting for picture: %s for %s seconds" % (picture, str(wait_time)))
    #         coordinates = pyautogui.locateOnScreen(picture, wait_time, region=browser_size, grayscale=True)
    #         if coordinates is None:
    #             print("Picture: %s not found" % picture)
    #             if screenshot:
    #                 take_screenshot(picture)
    #         else:
    #             print(coordinates)
    #             break
    #     return coordinates

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


class Search:
    def __init__(self):
        w = WindowMgr()
        w.find_window_wildcard(".*EA SPORTS.*")
        w.set_foreground()
        self.global_browser_size = w.getWindowSizes()
        self.global_browser_size_top = w.getWindowTopSizes()
        self.global_browser_size_bottom = w.getWindowBottomSizes()

    @staticmethod
    def go_to_search(price):
        # start.click_on_center(start.wait_for_list_of_pictures((Pics.Tabs.transfers_selected, Pics.Tabs.transfers)))
        # start.click_on_center(start.wait_for_list_of_pictures((Pics.Tabs.TransferMarket.transfers_market_selected,
        #                                                        Pics.Tabs.TransferMarket.transfers_market)))
        # start.click_on_center(start.wait_for_list_of_pictures((Pics.Tabs.TransferMarket.consumables_selected,
        #                                                        Pics.Tabs.TransferMarket.consumables)))
        # start.click_on_center(start.wait_for_picture(Pics.Tabs.TransferMarket.reset_button))
        # start.click_on_center(start.wait_for_list_of_pictures((Pics.Tabs.TransferMarket.consumables_selected,
        #                                                        Pics.Tabs.TransferMarket.consumables)))
        # start.click_on_center(start.wait_for_picture(Pics.Tabs.TransferMarket.Consumables.type_player_training))
        # start.click_on_center(start.wait_for_picture(Pics.Tabs.TransferMarket.Consumables.type_contracts))
        #
        # start.click_right_down_corner(start.wait_for_picture(Pics.Tabs.TransferMarket.Consumables.Quality.quality))
        # start.click_on_center(start.wait_for_picture(Pics.Tabs.TransferMarket.Consumables.Quality.quality_gold))
        #
        # start.click_right_down_corner(start.wait_for_picture(Pics.Tabs.TransferMarket.Pricing.buy_now_max),
        #                               horizontal=-50)
        # pyautogui.typewrite(price)

        # self.click_on_center(self.wait_for_picture(Pics.Tabs.TransferMarket.search_button))
        # pyautogui.moveTo(100, 200, 1)
        print('doing SEARCH')

    # @staticmethod
    def wait_for_search_result(self):
        result1 = Main.wait_for_picture(Pics.Test.pic1, self.global_browser_size, 5, True)
        if result1 is None:
            print('Exiting from search func1')
            pass
        else:
            print('call buy method')
            Test.count_contracts(self.global_browser_size)

    def wait_for_search_result2(self):
        result2 = Main.wait_for_picture(Pics.Test.pic2, self.global_browser_size, 5)
        if result2 is None:
            print('Exiting from search func2')
            pass
        else:
            print('call buy method2')

    def wait_for_search_result3(self):
        result3 = Main.wait_for_picture(Pics.Test.pic3, self.global_browser_size, 5)
        if result3 is None:
            print('Exiting from search func3')
            pass
        else:
            print('call buy method3')


class Test:
    @staticmethod
    def count_contracts(global_browser_size):
        print('SIZE for searching contracts: %s' % str(global_browser_size))
        print('Counting contracts:')
        print(global_browser_size)
        locate_players = pyautogui.locateAllOnScreen(
            Pics.Tabs.TransferMarket.Consumables.Contracts.contract_player_small,
            region=global_browser_size, grayscale=True)
        # print(len(list(locate_players)))
        print('LIST OF PLAYERS:')
        for player in locate_players:
            print(player)
    #
    # print("NEW PARALLEL starting")
    # search_for_contract_second = Search()
    # p10 = Process(target=search_for_contract_second.wait_for_search_result3)
    # p10.start()
    # print("NEW PARALLEL ending")

if __name__ == '__main__':

    # webbrowser.open('https://www.easports.com/fifa/ultimate-team/web-app')

    run = 0
    search_for_contract = Search()
    search_for_contract.go_to_search(300)
    print('DONE')
