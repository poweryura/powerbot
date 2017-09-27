import datetime
import time
import yaml
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from selenium.webdriver.common.keys import Keys

import os
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
import locators as el


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
    def load_config_file(file):
        f = open(file)
        Picsy = yaml.safe_load(f)
        print('config file %s loaded' % file)
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
            raise Exception("Windows handle not found, Please make sure that FUT page is opened")
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
        # try:
        #     #os.system("taskkill /im chrome.exe")
        #     #os.system("taskkill /f /im  chrome.exe")
        # except:
        #     pass

        options = webdriver.ChromeOptions()
        options.add_argument(r"user-data-dir=C:\Users\qadmin\AppData\Local\Google\Chrome\User Data")
        self.driver = webdriver.Chrome(executable_path="chromedriver.exe", chrome_options=options)
        self.driver.get('https://www.easports.com/fifa/ultimate-team/web-app/')
        self.driver.implicitly_wait(1)

        #Main.wait_for_element(self, el.Tabs.Logo, 15)
        # w = WindowMgr()
        # w.find_window_wildcard(".*EA SPORTS.*")
        # w.set_foreground()
        # self.global_browser_size = w.getWindowSizes()
        # self.global_browser_size_top = w.getWindowTopSizes()
        # self.global_browser_size_bottom = w.getWindowBottomSizes()
        # self.global_browser_size_left = w.getWindowLeftSizes()
        # self.global_browser_size_right = w.getWindowRightSizes()
        #if Main.wait_for_picture(self, Pics.Tabs.TransferMarket.ok, self.global_browser_size, 1) is not None:
        #    Main.click_on_center(Main.wait_for_picture(self, Pics.Tabs.TransferMarket.ok, self.global_browser_size))


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

    def wait_for_element_click(self, element, time=5,):
        WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(element)).click()

    def wait_for_element(self, element, time=5,):
        WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(element))

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
    def buy_contracts(self, contract_type):

        # Main.wait_for_picture(self, Pics.Tabs.TransferMarket.search_results, self.global_browser_size_top)
        try:
            Main.wait_for_element(self, el.Buttons.Watch)
            # Main.wait_for_element_click(self, el.Buttons.Next)
        except:
            print("Nothing found in search query")
            return
        counter = 0
        found_item = 0
        print('Something found, doing shopping')
        # try:
        while Main.wait_for_element(self, el.Buttons.Next) is None:
            time.sleep(1)
            counter = counter + 1
            # for each in range(len(found_list) - 1, -1, -1):
            # found_list = self.driver.find_elements_by_xpath(Picsy['Contracts'][contract_type]['contract_player_small'])
            
            print(counter)
            # for each in found_list:
            # found_contract_item = found_contract_item + 1
            # print("Clicking on %s" % str(found_contract_item))
            # pdb.set_trace()
            #print(each)
            # found_list[1].click()
            #
            try:
                self.driver.implicitly_wait(1)
                found_list = self.driver.find_elements_by_xpath(Picsy['Contracts'][contract_type]['contract_player_small'])
                random.choice(found_list).click()
                found_item = found_item + 1
                print("Clicking on %s" % str(found_item))
                self.driver.find_elements_by_xpath(Picsy['Contracts'][contract_type]['contract_player_big'])
                Main.wait_for_element_click(self, el.Buttons.SellBar.Buy_now)
                try:
                    Main.wait_for_element(self, (By.XPATH, "//*[contains(text(), 'Are you sure you want to buy this item for 200 coins')]"))
                except:
                    pass
                try: 
                    Main.wait_for_element(self, (By.XPATH, "//*[contains(text(), 'Are you sure you want to buy this item for 250 coins')]"))
                except:
                    pass
                Main.wait_for_element_click(self, el.Buttons.Ok)
                Main.wait_for_element_click(self, el.Buttons.SellBar.Send_to_My_Club)

            except IndexError:
                print('Nothing found')
            except:
                print('Failed to buy')


            try:
                Main.wait_for_element_click(self, el.Buttons.Next, 3)
            except TimeoutException:
                print('Pagination is end')
                return
                
        print('done loop')
            # for each in found_list:
            #     print("clicking")
            #     each.click()


class Search(Main):

    def login(self):
        for i in 'poweryura':

            try:
                WebDriverWait(self.driver, 1).until(EC.element_to_be_clickable((By.CLASS_NAME, 'user-info')))
                break
            except:
                pass

            try:
                WebDriverWait(self.driver, 1).until(EC.element_to_be_clickable((By.XPATH, "//*[@class='standard call-to-action' and contains(text(),'Login')]")))
                self.driver.find_element_by_xpath("//*[@class='standard call-to-action' and contains(text(),'Login')]").click()

                try:
                    WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//span[.='Log In']")))
                    self.driver.find_element_by_xpath("//span[.='Log In']").click()
                except:
                    pass

                WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'user-info')))
                break
            except:
                pass

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'user-info')))

        print("Logged IN")

    def search_contracts(self, contract_type):
        print(inspect.stack()[0][3])
        #pdb.set_trace()

        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(el.Tabs.Transfers)); self.driver.find_element_by_xpath(el.Tabs.Transfers[1]).click()

        #Main.wait_for_element_click(self, el.Tabs.Transfers)

        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(el.Tabs.TransfersIn.Search_Transfer_market)); self.driver.find_element_by_xpath(el.Tabs.TransfersIn.Search_Transfer_market[1]).click()

        #Main.wait_for_element_click(self, el.Tabs.TransfersIn.Search_Transfer_market)

        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(el.Tabs.TransfersIn.SearchTransferMarket.Consumables));  self.driver.find_element_by_xpath(el.Tabs.TransfersIn.SearchTransferMarket.Consumables[1]).click()

        #Main.wait_for_element_click(self, el.Tabs.TransfersIn.SearchTransferMarket.Consumables);
        Main.wait_for_element_click(self, el.Buttons.Reset)

        Main.wait_for_element_click(self, (By.XPATH, "//*[@class='label' and contains(text(),'Player Training')]"))
        Main.wait_for_element_click(self, (By.XPATH, "//*[@class='with-icon' and contains(text(),'Contracts')]"))
        Main.wait_for_element_click(self, (By.XPATH, "//*[@class='label' and contains(text(),'Quality')]"))
        Main.wait_for_element_click(self, (By.XPATH, "//*[@class='with-icon' and contains(text(),'Gold')]"))

        #self.driver.find_element_by_xpath("//*[@class='numericInput']").clear()
        self.driver.find_element_by_xpath("//*[@class='numericInput']").send_keys(Picsy['Contracts'][contract_type]['bid_min_price'])

        #self.driver.find_elements_by_xpath("//*[@class='numericInput']")[3].clear()
        self.driver.find_elements_by_xpath("//*[@class='numericInput']")[3].send_keys(Picsy['Contracts'][contract_type]['buy_max_price'])


        Main.wait_for_element_click(self, el.Buttons.Search)
        Main.wait_for_element(self, el.Buttons.Watch)

        self.buy_contracts(contract_type)

    def relist_and_clear_sold(self):
        print(inspect.stack()[0][3])
        time.sleep(1)
        Main.wait_for_element_click(self, el.Tabs.Transfers)
        time.sleep(1)
        Main.wait_for_element_click(self, el.Tabs.TransfersIn.Transfer_List)

        print("Trying to re-list")
        try:
            time.sleep(1)
            Main.wait_for_element_click(self, el.Buttons.Re_listAll)
            time.sleep(1)
            Main.wait_for_element_click(self, el.Buttons.Yes)
            time.sleep(1)

        except:
            print('Nothing to relist')

        print("Trying to clear sold")
        try:
            Main.wait_for_element_click(self, el.Buttons.Clear_Sold, 5)
        except:
            print('Nothing to Clear')

    def sell_item(self, contract_type):
        print(inspect.stack()[0][3])
        time.sleep(2)
        Main.wait_for_element_click(self, el.Tabs.Club)
        time.sleep(2)
        Main.wait_for_element_click(self, el.Tabs.ClubIn.Consumables)
        time.sleep(2)
        Main.wait_for_element_click(self, el.Tabs.ClubIn.Contracts)
        Main.wait_for_element_click(self, (By.XPATH, Picsy['Contracts'][contract_type]['contract_player_small']))
        sell_count = 0
        try:
            for sell in range(1, 10):
                print("Starting selling")

                sell_count = sell_count + 1
                time.sleep(1)
                Main.wait_for_element(self, (By.XPATH, Picsy['Contracts'][contract_type]['contract_player_big']))
                Main.wait_for_element_click(self, el.Buttons.SellBar.List_on_Transfer_Market)
                Main.wait_for_element(self, (By.XPATH, "//*[@class='numericInput filled']"))

                self.driver.find_element_by_xpath("//*[@class='numericInput filled']").send_keys(Keys.BACKSPACE)
                self.driver.find_element_by_xpath("//*[@class='numericInput filled']").send_keys(Keys.BACKSPACE)
                self.driver.find_element_by_xpath("//*[@class='numericInput filled']").send_keys(Keys.BACKSPACE)

                self.driver.find_element_by_xpath("//*[@class='numericInput filled']").send_keys(Picsy['Contracts'][contract_type]['sell_min_price'])
                self.driver.find_elements_by_xpath("//*[@class='numericInput filled']")[1].send_keys(Keys.BACKSPACE)
                self.driver.find_elements_by_xpath("//*[@class='numericInput filled']")[1].send_keys(Keys.BACKSPACE)
                self.driver.find_elements_by_xpath("//*[@class='numericInput filled']")[1].send_keys(Keys.BACKSPACE)

                self.driver.find_elements_by_xpath("//*[@class='numericInput filled']")[1].send_keys(Picsy['Contracts'][contract_type]['sell_max_price'])

                Main.wait_for_element_click(self, el.Buttons.SellBar.List_item)
                print("Sent for selling: %s" % str(sell_count))

        except TimeoutException as ex:
            print(ex)
            pyautogui.typewrite(['enter'], interval=0.1)

    def exit(self):
        self.driver.close()



if __name__ == '__main__':

    # webbrowser.open('https://www.easports.com/fifa/ultimate-team/web-app')
    run = 0

    Picsy = Service.load_config_file('Pics.yaml')

    #
    # Start = Search()
    # Start.login()
    # Start.search_contracts("Rare")
    # Start.sell_item("Rare")
    # Start.relist_and_clear_sold()
    # Start.exit()
    Start = Search()
while True:
    global first_hour

    run = run + 1

    print('Iteration to search items : %s' % str(run))
    try:
        Start.login()
        Start.search_contracts(random.choice(['Rare', 'Gold']))
    except Exception as ex:
        print(ex)

    try:
        Start.sell_item(random.choice(['Rare', 'Gold']))
    except Exception as ex:
        print(ex)

    try:
        Start.relist_and_clear_sold()
    except Exception as ex:
        print(ex)

    time.sleep(randint(0, 60))

