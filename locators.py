from selenium.webdriver.common.by import By

class Buttons(object):
    MainLogin_FUT = (By.XPATH, '//*[@id="Login"]/div/div/div[1]/div/button')
    Login_EA = (By.XPATH, '//*[@id="btnLogin"]/span/span')
    Reset = (By.XPATH, "/html/body/section/article/div[1]/div[2]/div/div[1]/div[2]/span[1]")
    Search = (By.XPATH, "/html/body/section/article/div[1]/div[2]/div/div[1]/div[1]/span[1]")
    Watch = (By.XPATH, "/html/body/section/article/section/section[2]/div/div/div[3]/div[1]/div[3]/button")
    Re_listAll = (By.XPATH, "//span[.='Re-list All']")
    Clear_Sold = (By.XPATH, "//span[.='Clear Sold']")
    Next = (By.XPATH, "//*[@class='btn-flat pagination next']")
    Yes = (By.XPATH, "//*[@class='btn-flat' and contains(text(),'Yes')]")


    'class="'
    ''
class Tabs(object):
    Transfers = (By.XPATH, ".//*[@id='footer']/button[5]")

    class TransfersIn(object):
        Search_Transfer_market = (By.XPATH, "/html/body/section/article/div[1]")
        Transfer_List = (By.XPATH, "/html/body/section/article/div[2]")
        Transfer_Target = (By.XPATH,"/html/body/section/article/div[3]")

        class SearchTransferMarket(object):
            Consumables = (By.XPATH, "/html/body/section/article/div[1]/div[1]/div/a[4]")

        class Contracts(object):
            Contract_gold = (By.XPATH, "//div[contains(@class, 'small consumable item common gold')]")
            Contract_Rare = (By.XPATH, "//div[contains(@class, 'small consumable item rare gold')]")
