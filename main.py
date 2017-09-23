import datetime
import time
import yaml
import sys
# import webbrowser
# import os
from itertools import count
from multiprocessing import Process
import pdb
import inspect
from PIL import ImageGrab
import Pics
# import smtplib
import pyautogui
# from pywinauto.application import Application
import win32gui
import re
from random import randint
import smtplib
import random


# connect to another process spawned by explorer.exe
# app = Application(backend="uia").connect(path="firefox.exe", title="FUT")
# print(app.is_process_running())

# print(pyautogui.getWindows())
# windows = pyautogui.getWindow('FIFA Football | FUT Web App | EA SPORTS - Mozilla Firefox')

class Service(object):

    @staticmethod
    def send_mail():
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login("yyura2014@gmail.com", "Power1234")
        msg = "Check BOT"
        server.sendmail("yyura2014@gmail.com", "poweryura@gmail.com", msg)
        server.quit()

    @staticmethod
    def initiate_market_wipe(first_hour):
        print(inspect.stack()[0][3])
        print(first_hour)
        current_hour = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H')
        print(current_hour)
        if first_hour != current_hour:
            print("doing market WIPE")
            first_hour = current_hour
        else:
            pass
        return first_hour

    @staticmethod
    def take_screenshot(prefix, global_browser_size):
        current_time = str(datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')) + '_' + prefix + '_' ".jpg"
        ImageGrab.grab(bbox=global_browser_size).save(current_time, "JPEG")
        print("Saved screenshot: %s" % current_time)

    @staticmethod
    def timing(f):
        def wrap(*args):
            time1 = time.time()
            ret = f(*args)
            time2 = time.time()
            print('%s function took %0.3f ms' % (f.__name__, (time2 - time1) * 1000.0))
            return ret

        return wrap

    @staticmethod
    def get_config_file(file):
        f = open(file)
        Picsy = yaml.safe_load(f)
        f.close()
        return Picsy




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

    @Service.timing
    def wait_for_picture(self, picture, global_browser_size, wait_time=5, screenshot=False):
        print("Waiting for picture: %s for %s seconds" % (picture, str(wait_time)))
        coordinates = pyautogui.locateOnScreen(picture, wait_time, region=global_browser_size, grayscale=True)
        if coordinates is None:
            print("!!!!!!!!!!!!!Picture: %s not found!!!!!!!!!!!!!" % picture)
            if screenshot:
                Service.take_screenshot(picture, global_browser_size)
                return False
        else:
            print('*******Found: %s at %s *******' % (picture, coordinates))
            return coordinates

    @Service.timing
    def wait_for_list_of_pictures(self, list_to_search, global_browser_size, wait_time=5, screenshot=False):
        coordinates = False
        for picture in list_to_search:
            print("Waiting for picture: %s for %s seconds" % (picture, str(wait_time)))
            coordinates = pyautogui.locateOnScreen(picture, wait_time, region=global_browser_size, grayscale=True)
            if coordinates is None:
                print("!!!!!!!!!!!!!Picture: %s not found!!!!!!!!!!!!!, Searching for second picture" % picture)
                if screenshot:
                    Service.take_screenshot(picture, global_browser_size)
            else:
                print('*******Found: %s at %s *******' % (picture, coordinates))
                break
        return coordinates

    @staticmethod
    def click_on_center(coordinates):
        if coordinates is False:
            print('Exiting as no coordinates found!!!')
            sys.exit()
        coordinates = pyautogui.center(coordinates)
        pyautogui.click(coordinates[0], coordinates[1])

    @staticmethod
    def click_right_down_corner(coordinates, vertical=0, horizontal=0):
        if coordinates is False:
            print('Exiting as no coordinates found!!!')
            sys.exit()
        coordinates = (coordinates[0] + coordinates[2] + horizontal, coordinates[1] + coordinates[3] + vertical)
        pyautogui.click(coordinates)

    @Service.timing
    def buy_contracts(self, global_browser_size, contract_type):
        # pdb.set_trace()
        Main.wait_for_picture(self, Pics.Tabs.TransferMarket.watch, self.global_browser_size_top)

        while Main.wait_for_picture(self, Pics.Tabs.TransferMarket.nextarrow, self.global_browser_size_top, 3):
            counter = 0
            counter = counter + 1
            Main.wait_for_picture(self, Pics.Tabs.TransferMarket.watch, self.global_browser_size_top)
            if str(list(pyautogui.locateAllOnScreen(Picsy['Contracts'][contract_type]['contract_player_small'], region=global_browser_size, grayscale=True))) == '[]':
                print('No contract found')
                if Main.wait_for_picture(self, Pics.Tabs.TransferMarket.nextarrow, self.global_browser_size_top, 1):
                    print('Clicking on next page: %s' % str(counter))
                    Main.click_on_center(Main.wait_for_picture(self, Pics.Tabs.TransferMarket.nextarrow, self.global_browser_size_top, 1))
            else:
                for player in pyautogui.locateAllOnScreen(Picsy['Contracts'][contract_type]['contract_player_small'], region=global_browser_size, grayscale=True):
                    print(counter)
                    print(player)
                    Main.click_on_center(player)
                    if Main.wait_for_picture(self, Picsy['Contracts'][contract_type]['contract_player_full'], self.global_browser_size_right) is True:
                        Main.click_on_center(Main.wait_for_picture(self, Pics.Actions.buy_now, self.global_browser_size, 2))
                        pyautogui.typewrite(['enter'], interval=0.1)
                        Main.click_on_center(Main.wait_for_picture(self, Pics.Actions.send_to_my_club, self.global_browser_size_right, 1))


class Search(Main):

    def go_to_search(self, contract_type):

        Main.click_on_center(Main.wait_for_list_of_pictures(self, (Pics.Tabs.transfers_selected, Pics.Tabs.transfers), self.global_browser_size_left, 2))

        Main.click_on_center(Main.wait_for_picture(self, Pics.Tabs.TransferMarket.search_the_transfer_market, self.global_browser_size_top, 2))
        Main.click_on_center(Main.wait_for_picture(self, Pics.Tabs.TransferMarket.reset_button, self.global_browser_size_bottom))
        Main.click_on_center(Main.wait_for_list_of_pictures(self, (Pics.Tabs.TransferMarket.consumables_selected, Pics.Tabs.TransferMarket.consumables), self.global_browser_size_top, 3))
        Main.click_on_center(Main.wait_for_picture(self, Pics.Tabs.TransferMarket.Consumables.type_player_training_big, self.global_browser_size_top, 3))
        pyautogui.moveRel(80, 80, duration=0.3)
        pyautogui.scroll(-100)
        Main.click_on_center(Main.wait_for_picture(self, Pics.Tabs.TransferMarket.Consumables.type_contracts, self.global_browser_size))
        Main.click_on_center(Main.wait_for_picture(self, Pics.Tabs.TransferMarket.Consumables.Quality.quality, self.global_browser_size))
        Main.click_on_center(Main.wait_for_picture(self, Pics.Tabs.TransferMarket.Consumables.Quality.quality_gold, self.global_browser_size))

        pyautogui.moveRel(-200, -200, duration=0.1)
        pyautogui.typewrite(['tab'], interval=0.1)
        pyautogui.typewrite(Picsy['Contracts'][contract_type]['bid_min_price'], interval=0.1)
        pyautogui.typewrite(['tab'], interval=0.1)
        pyautogui.typewrite(['tab'], interval=0.1)
        pyautogui.typewrite(['tab'], interval=0.1)
        pyautogui.typewrite(Picsy['Contracts'][contract_type]['buy_max_price'], interval=0.1)

        Main.click_on_center(Main.wait_for_picture(self, Pics.Tabs.TransferMarket.search_button, self.global_browser_size))
        Main.wait_for_picture(self, Pics.Tabs.TransferMarket.watch, self.global_browser_size_top)

        self.buy_contracts(self.global_browser_size_left, contract_type)

    def relist_and_clear_sold(self):
        Main.click_on_center(Main.wait_for_list_of_pictures(self, (Pics.Tabs.transfers_selected, Pics.Tabs.transfers), self.global_browser_size_left, 2))
        Main.click_on_center(Main.wait_for_picture(self, Pics.Tabs.Transfer_list.transfer_list, self.global_browser_size))
        if Main.wait_for_picture(self, Pics.Tabs.TransferMarket.clear_sold, self.global_browser_size_top, 2):
            Main.click_on_center(Main.wait_for_picture(self, Pics.Tabs.TransferMarket.clear_sold, self.global_browser_size_top, 1))
        if Main.wait_for_picture(self, Pics.Tabs.TransferMarket.relist_all, self.global_browser_size_top, 2):
            Main.click_on_center(Main.wait_for_picture(self, Pics.Tabs.TransferMarket.relist_all, self.global_browser_size_top, 1))
            pyautogui.typewrite(['enter'], interval=0.1)


class Sell(Main):

    def go_to_consumables(self, contract_type):
        print(inspect.stack()[0][3])
        Main.click_on_center(Main.wait_for_list_of_pictures(self, (Pics.Tabs.Club.club, Pics.Tabs.Club.club_selected), self.global_browser_size, 2))
        Main.click_on_center(Main.wait_for_picture(self, Pics.Tabs.Club.club_consumables, self.global_browser_size))
        #pdb.set_trace()
        Main.click_on_center(Main.wait_for_picture(self, Pics.Tabs.Club.Consumables.cons_contracts, self.global_browser_size))
        Main.click_on_center(Main.wait_for_picture(self, Picsy['Contracts'][contract_type]['contract_player_small'], self.global_browser_size))

    def sell_item(self, contract_type):
        print(inspect.stack()[0][3])
        #pdb.set_trace()
        sell_count = 0
        for sell in range(1, 30):
            sell_count = sell_count + 1
            print(sell_count)
            Main.click_on_center(Main.wait_for_picture(self, Pics.Actions.list_on_transfer_market, self.global_browser_size))
            #str(pyautogui.locateOnScreen(Pics.Tabs.Club.Consumables.Contracts.contract_player_gold_RARE_small))
            pyautogui.typewrite(['tab'], interval=1)
            pyautogui.typewrite(Picsy['Contracts'][contract_type]['sell_min_price'], interval=0.1)
            pyautogui.typewrite(['tab'], interval=0.1)
            pyautogui.typewrite(['tab'], interval=0.1)
            pyautogui.typewrite(['tab'], interval=0.1)
            pyautogui.typewrite(Picsy['Contracts'][contract_type]['sell_max_price'], interval=0.1)
            Main.click_on_center(Main.wait_for_picture(self, Pics.Actions.list_item, self.global_browser_size))
            if Main.wait_for_picture(self, Pics.Messages.warning_message, self.global_browser_size,1):
                pyautogui.typewrite(['enter'], interval=0.1)
                break


if __name__ == '__main__':

    # webbrowser.open('https://www.easports.com/fifa/ultimate-team/web-app')
    run = 0

    Picsy = Service.get_config_file('Pics.yaml')

    # search_for_contract = Search()
    # search_for_contract.go_to_search('Gold')
    #
    # sell_contracts = Sell()
    # sell_contracts.go_to_consumables('Gold')
    # sell_contracts.sell_item('Gold')

while True:
    global first_hour

    run = run + 1
    print('Iteration: %s' % str(run))
    sell_contracts = Sell()
    contract = random.choice(['Rare', 'Gold'])
    print('Working with %s' % contract)
    try:

        sell_contracts.go_to_consumables(contract)
        sell_contracts.sell_item(contract)
    except:
         pass

    try:
        search_for_contract = Search()
        search_for_contract.go_to_search(contract)
    except:
          pass

    try:
        search_for_contract = Search()
        search_for_contract.relist_and_clear_sold()
    #except: TypeError
    #    print("Some pics was not found")
    except:
        pass

    print('DONE')
    time.sleep(randint(0, 30))
