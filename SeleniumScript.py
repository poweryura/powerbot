from selenium import webdriver
import pickle

import time
# driver = webdriver.Firefox(executable_path=r'geckodriver.exe')
# driver = webdriver.Chrome(executable_path=r'chromedriver.exe')


fp = webdriver.FirefoxProfile(r'C:\Users\qadmin\AppData\Roaming\Mozilla\Firefox\Profiles\0rnj92jz.default')
driver = webdriver.Firefox(fp)
driver.implicitly_wait(30)
#driver.get('https://www.easports.com/fifa/ultimate-team/web-app')

driver.get("https://www.easports.com/fifa/ultimate-team/web-app/")


try:
    content = driver.find_element_by_xpath('html/body/section/article/div/div/div[2]/div[2]/div/input')
    content.click()
    time.sleep(4)
    content.send_keys('Petrovich')
    #driver.find_element_by_class_name("btn btn-raised call-to-action").click()
except:
    pass
time.sleep(30)
try:
    driver.find_element_by_xpath(".//*[@id='footer']/button[5]").click()
except:
    driver.refresh()
driver.find_element_by_xpath(".//*[@id='footer']/button[5]").click()
driver.find_element_by_xpath("html/body/section/article/div[2]").click()
time.sleep(2)
driver.find_element_by_class_name("btn btn-raised section-header-btn mini call-to-action").click()
time.sleep(2)
# def load_cookie(file1):
#     with open(file1, 'rb') as cookie:
#         return pickle.load(cookie)


# cookie = load_cookie("chrome_cookies.pkl")
# driver.add_cookie(cookie)


# for cookie in pickle.load(open("fifa_.pkl", "rb")):
#     print(cookie)
#     driver.add_cookie(cookie)
#
# #driver.get('https://www.easports.com/fifa/ultimate-team/web-app')
# driver.get("https://www.easports.com/")


#pickle.dump(driver.get_cookies(), open("fifa_.pkl", "wb"))

