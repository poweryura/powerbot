from selenium.webdriver.common.by import By


class Buttons(object):
    MainLogin_FUT = (By.XPATH, '//*[@id="Login"]/div/div/div[1]/div/button')
    Login_EA = (By.XPATH, "//span[.='Log In']")
    Reset = (By.XPATH, "/html/body/section/article/div[1]/div[2]/div/div[1]/div[2]/span[1]")
    Search = (By.XPATH, "/html/body/section/article/div[1]/div[2]/div/div[1]/div[1]/span[1]")
    Watch = (By.XPATH, "/html/body/section/article/section/section[2]/div/div/div[3]/div[1]/div[3]/button")
    Re_listAll = (By.XPATH, "//span[.='Re-list All']")
    Clear_Sold = (By.XPATH, "//span[.='Clear Sold']")
    Next = (By.XPATH, "//*[@class='btn-flat pagination next']")
    Yes = (By.XPATH, "//*[@class='btn-flat' and contains(text(),'Yes')]")
    Ok = (By.XPATH, "//*[@class='btn-flat' and contains(text(),'Ok')]")
    Continue = (By.XPATH, "//*[@class='btn-text' and contains(text(),'Continue')]")

    class SellBar(object):
        List_on_Transfer_Market = (By.XPATH, "//*[@class='btn-text' and contains(text(),'List on Transfer Market')]")
        Start_Price = (By.CLASS_NAME, "numericInput filled")
        List_item = (By.XPATH, "//*[@class='standard call-to-action']")
        Buy_now = (By.XPATH, "//*[@class='btn-text' and contains(text(),'Buy Now')]")
        Send_to_My_Club = (By.XPATH, "//*[@class='btn-text' and contains(text(),'Send to My Club')]")


class Tabs(object):

    Logo = (By.XPATH, "//*[@class='btnFooter btnLogo']")
    Transfers = (By.XPATH, '//*[@id="footer"]/button[5]')
    Club = (By.XPATH, '//*[@id="footer"]/button[7]')

    class TransfersIn(object):
        Search_Transfer_market = (By.XPATH, "//*[@class='tile transferMarketTile']")
        Transfer_List = (By.XPATH, "//*[@class='tile col-mobile-1-2 col-1-2 transferListTile']")
        Transfer_Target = (By.XPATH, "//*[@class='tile col-mobile-1-2 col-1-2 transferTargetsTile']")

        class SearchTransferMarket(object):
            Consumables = (By.XPATH, "/html/body/section/article/div[1]/div[1]/div/a[4]")

    class ClubIn(object):
        Consumables = (By.XPATH, "//*[@class='tileHeader' and contains(text(),'Consumables')]")
        Contracts = (By.XPATH, "//*[@class='tileHeader' and contains(text(),'Contracts')]")

