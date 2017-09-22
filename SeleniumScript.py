from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pdb
import pickle
import time

# driver = webdriver.Firefox(executable_path=r'geckodriver.exe')
# driver = webdriver.Chrome(executable_path=r'chromedriver.exe')

options = webdriver.ChromeOptions()
options.add_argument(r"user-data-dir=C:\Users\qadmin\AppData\Local\Google\Chrome\User Data")
#driver = webdriver.Chrome(executable_path="chromedriver.exe", chrome_options=options)

driver = webdriver.Chrome(executable_path="chromedriver.exe", chrome_options=options)

# fp = webdriver.FirefoxProfile(r'C:\Users\qadmin\AppData\Roaming\Mozilla\Firefox\Profiles\0rnj92jz.default')
# driver = webdriver.Firefox(fp)


driver.implicitly_wait(3)
#driver.get('https://www.easports.com/fifa/ultimate-team/web-app')

driver.get("https://www.easports.com/fifa/ultimate-team/web-app/")

pdb.set_trace()

# try:
#     driver.find_element_by_xpath('html/body/section/article/div/div/div[2]/div[2]/div/input').send_keys('Petrovich')
#     content.click()
#     content
#     # driver.find_element_by_class_name("btn btn-raised call-to-action").click()
# except:
#     pass
#


# Transfers
driver.find_element_by_xpath(".//*[@id='footer']/button[5]").click()

# Transfer List
driver.find_element_by_xpath("/html/body/section/article/div[2]").click()

# Consumables
driver.find_element_by_xpath("/html/body/section/article/div[1]/div[1]/div/a[4]").click()


driver.find_element_by_xpath("/html/body/section/article/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/ul/li[6]").click()
driver.find_element_by_css_selector('btnFooter.btnTransfers').click()


driver.find_element_by_class_name("tile col-mobile-1-2 col-1-2 transferListTile").click()

content = driver.find_elements_by_class_name("tileContent")
content[1].click()



time.sleep(2)
driver.find_element_by_class_name("btn-text").click()

driver.find_element_by_xpath("/html/body/section/article/div[2]").click()

driver.find_element_by_xpath("/html/body/section/article/section/section[2]/div/div/div[3]/div[2]/button").click()
driver.find_element_by_css_selector('standard.call-to-action.bidButton').click()
driver.find_element_by_class_name("slick-slide slick-current slick-active").click()

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

