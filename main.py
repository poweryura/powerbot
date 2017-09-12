import random
import inspect
import datetime
from functools import wraps
import time
import yaml
import sys
import traceback
import webbrowser
import os
from PIL import ImageGrab
import Pics
import smtplib
import pyautogui
from pywinauto.application import Application
import win32con
import win32gui
import re


#webbrowser.open('https://www.easports.com/fifa/ultimate-team/web-app')
# def get_config_file(file):
#     f = open(file)
#     Pics = yaml.safe_load(f)
#     f.close()
#     return Pics
#
#Pics = get_config_file('Pics.yaml')

def timing_old(f):
    @wraps(f)
    def wrapper(*args, **kwds):
        start_time = time.time()
        result = f(*args, **kwds)
        elapsed = time.time() - start_time
        print("%s took %d time to finish" % (f.__name__, elapsed))
        return result
    return wrapper


def timing(f):
    def wrap(*args):
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()
        print ('%s function took %0.3f ms' % (f.__name__, (time2-time1)*1000.0))
        return ret
    return wrap


class Main:
    def __init__(self):
        pass

    @staticmethod
    def take_screenshot(prefix=''):
        current_time = str(datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')) + prefix+".jpg"
        ImageGrab.grab().save(current_time, "JPEG")
        print("Saved screenshot: %s" % current_time)

    @timing
    def wait_for_picture(self, picture, time=5, screenshot=False):
        print("Waiting for picture: %s for %s seconds" % (picture, str(time)))
        coordinates = pyautogui.locateOnScreen(picture, time, grayscale=False)
        if coordinates is None:
            print("Picture: %s not found" % picture)
            if screenshot:
                self.take_screenshot(picture)
        else:
            print(coordinates)
            coordinates = pyautogui.center(coordinates)
        return coordinates

    @timing
    def wait_for_list_of_pictures(self, list_to_search, time=5, screenshot=False):
        coordinates = None
        for picture in list_to_search:
            print("Waiting for picture: %s for %s seconds" % (picture, str(time)))
            coordinates = pyautogui.locateOnScreen(picture, time, grayscale=False)
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


# start = Main()
# twitter = start.wait_for_picture(Pics.Home.twitter, 5)

# start.click_on_center(start.wait_for_list_of_pictures((Pics.Tabs.transfers_selected, Pics.Tabs.transfers)))
# start.click_on_center(start.wait_for_list_of_pictures((Pics.Tabs.TransferMarket.transfers_market_selected, Pics.Tabs.TransferMarket.transfers_market)))
# start.click_on_center(start.wait_for_list_of_pictures((Pics.Tabs.TransferMarket.consumables_selected, Pics.Tabs.TransferMarket.consumables)))
# start.click_on_center(start.wait_for_picture(Pics.Tabs.TransferMarket.reset_button))
#
# start.click_on_center(start.wait_for_list_of_pictures((Pics.Tabs.TransferMarket.consumables_selected, Pics.Tabs.TransferMarket.consumables)))
#




#Application().start('explorer.exe "C:\\Program Files"')

# connect to another process spawned by explorer.exe
app = Application(backend="uia").connect(path="firefox.exe", title="FUT")
#app.Kill_()
print(app.is_process_running())




def isRealWindow(hWnd):
    '''Return True iff given window is a real Windows application window.'''
    if not win32gui.IsWindowVisible(hWnd):
        return False
    if win32gui.GetParent(hWnd) != 0:
        return False
    hasNoOwner = win32gui.GetWindow(hWnd, win32con.GW_OWNER) == 0
    lExStyle = win32gui.GetWindowLong(hWnd, win32con.GWL_EXSTYLE)
    if (((lExStyle & win32con.WS_EX_TOOLWINDOW) == 0 and hasNoOwner)
      or ((lExStyle & win32con.WS_EX_APPWINDOW != 0) and not hasNoOwner)):
        if win32gui.GetWindowText(hWnd):
            return True
    return False

def getWindowSizes():
    '''
    Return a list of tuples (handler, (width, height)) for each real window.
    '''
    def callback(hWnd, windows):
        if not isRealWindow(hWnd):
            return
        rect = win32gui.GetWindowRect(hWnd)
        print(rect)
        windows.append((hWnd, (rect[2] - rect[0], rect[3] - rect[1])))
    windows = []
    print(windows)
    win32gui.EnumWindows(callback, windows)
    return windows

#getWindowSizes()

class WindowMgr:
    """Encapsulates some calls to the winapi for window management"""
    def __init__ (self):
        """Constructor"""
        self._handle = None

    def find_window(self, class_name, window_name = None):
        """find a window by its class_name"""
        self._handle = win32gui.FindWindow(class_name, window_name)

    def _window_enum_callback(self, hwnd, wildcard):
        '''Pass to win32gui.EnumWindows() to check all the opened windows'''
        if re.match(wildcard, str(win32gui.GetWindowText(hwnd))) != None:
            self._handle = hwnd

    def find_window_wildcard(self, wildcard):
        self._handle = None
        win32gui.EnumWindows(self._window_enum_callback, wildcard)

    def set_foreground(self):
        """put the window in the foreground"""
        win32gui.SetForegroundWindow(self._handle)

w = WindowMgr()
w.find_window_wildcard(".*Firefox.*")
w.set_foreground()


hwnd = win32gui.FindWindow('Google - Mozilla Firefox', 'Google - Mozilla Firefox')
print(hwnd)