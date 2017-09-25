from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pdb
import pickle
import time
import locators


# driver = webdriver.Firefox(executable_path=r'geckodriver.exe')
# driver = webdriver.Chrome(executable_path=r'chromedriver.exe')
pdb.set_trace()
options = webdriver.ChromeOptions()
options.add_argument(r"user-data-dir=C:\Users\qadmin\AppData\Local\Google\Chrome\User Data")

driver = webdriver.Chrome(executable_path="chromedriver.exe", chrome_options=options)

# Click Search
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/section/article/div[1]/div[2]/div/div[1]/div[1]/span[1]"))).click()




# fp = webdriver.FirefoxProfile(r'C:\Users\qadmin\AppData\Roaming\Mozilla\Firefox\Profiles\0rnj92jz.default')
# driver = webdriver.Firefox(fp)

driver.implicitly_wait(10)
#driver.get('https://www.easports.com/fifa/ultimate-team/web-app')

#driver.get("https://www.easports.com/fifa/ultimate-team/web-app/")

pdb.set_trace()

# Transfers
driver.find_element_by_xpath(".//*[@id='footer']/button[5]").click()
# Transfer Search
driver.find_element_by_xpath("/html/body/section/article/div[1]").click()
# Consumables
driver.find_element_by_xpath("/html/body/section/article/div[1]/div[1]/div/a[4]").click()
# Button Search
driver.find_element_by_xpath("/html/body/section/article/div[1]/div[2]/div/div[1]/div[1]/span[1]").click()


# Transfers
driver.find_element_by_xpath(".//*[@id='footer']/button[5]").click()
# Transfer Search
driver.find_element_by_xpath("/html/body/section/article/div[1]").click()


# Consumables
driver.find_element_by_xpath("/html/body/section/article/div[1]/div[1]/div/a[4]").click()

driver.find_element_by_xpath("/html/body/section/article/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/ul/li[6]").click()
driver.find_element_by_css_selector('btnFooter.btnTransfers').click()
driver.find_element_by_class_name("tile col-mobile-1-2 col-1-2 transferListTile").click()
content = driver.find_elements_by_class_name("tileContent")
content[1].click()

driver.find_element_by_class_name("btn-text").click()
driver.find_element_by_xpath("/html/body/section/article/div[2]").click()
driver.find_element_by_xpath("/html/body/section/article/section/section[2]/div/div/div[3]/div[2]/button").click()
driver.find_element_by_css_selector('standard.call-to-action.bidButton').click()
driver.find_element_by_class_name("slick-slide slick-current slick-active").click()

