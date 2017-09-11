from Sikuli import *
import random
import inspect
import datetime
import sys
import traceback
import webbrowser
import os
import smtplib
#from picturesfifa import *

round=0
contracts_bought=0
sell="n"
items_to_sell=100
sell_min=str(200)
sell_max=str(250)
sell_min_rare=str(750)
sell_max_rare=str(800)



to_random=(200, 200)

#full_contract=Pattern("full_player_manager.png").exact().targetOffset(-1,-38)
#player=Pattern("manager_contract.png").similar(0.90).targetOffset(-6,-42)
player="player_contract.png"
player_rare=Pattern("player_rare.png").similar(0.79)
to_sell_player=Pattern("to_sell_player.png").similar(0.80)
full_contract=Pattern("full_player_contract.png").exact()
won_contract=Pattern("won_contract.png").similar(0.90)

#regions
full_contract_reg = Region(12,136,806,436)
bid_reg = Region(368,381,472,185)
trans_target_reg=Region(559,445,267,47)
con_reg = Region(18,468,1008,292)

transfers_tab_selected = "transfers_tab_selected.png"
transfers_tab = "transfers_tab.png"
transfer_market_selected = "transfer_market_selected.png"
transfer_market = "transfer_market.png"  
consumables_tab_selected = Pattern("consumables_tab_selected.png").similar(0.90)
consumables_tab = Pattern("consumables_tab.png").similar(0.90)
trans_target=Pattern("trans_target_50.png").exact()
both_contract=Pattern("common_contract.png").similar(0.80) #any item
store_all_in_the_club = Pattern("store_all_in_the_club.png").exact()
quick_list_png = Pattern("quick_list_png.png").similar(0.99)
min_price_sel = Pattern("min_price_sel.png").similar(0.90)
ok_yellow = "ok_yellow.png"
home = Pattern("home.png").similar(0.60)
remove_all_experied = Pattern("remove_all_experied.png").similar(0.60)
send_to_the_club = Pattern("send_to_the_club.png").similar(0.80)
transfer_target = "transfer_target.png"
min_pirce_buy = Pattern("min_pirce_buy.png").similar(0.96).targetOffset(88,2)
search_button = Pattern("search_button.png").similar(0.80)
account_locked = Pattern("account_locked.png").similar(0.80)

def send_mail(): 
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("yyura2014@gmail.com", "Power1234")     
    msg = "Check BOT"
    server.sendmail("yyura2014@gmail.com", "poweryura@gmail.com", msg)
    server.quit()

def restart_browser(): 
    os.system("taskkill /im firefox.exe")
    sleep(10)
    os.system("taskkill /im firefox.exe")
    sleep(10)
    webbrowser.open('https://www.easports.com/fifa/ultimate-team/web-app')    
    try:
        wait("twitter.png",60)        
    except FindFailed:
        if exists(account_locked):
            send_mail()        
        else:
            try:
                click("accept.png")
                WaitAndClick(store_all_in_the_club,10)
            except FindFailed:
                click(Pattern("page_refresh.png").similar(0.90))
                wait("twitter.png",60)


#Settings.MoveMouseDelay = 0
#sys.setrecursionlimit(10000)
restart_browser()

first_hour = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H')
mozilla_size = App("Mozilla Firefox").focusedWindow()
print mozilla_size

def timing(f):
    def wrap(*args):
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()
        print '%s function took %0.3f ms' % (f.func_name, (time2-time1)*1000.0)
        return ret
    return wrap

def order(match):
    return match.x 

def WaitAndClick(image_name, timeout):    
    #mozilla_size.click(image_name)
    wait(image_name,timeout)
    click(getLastMatch())

def ClickFirstOrSecond(image1,image2,timeout=0):
    if exists(image1,0): click(image1)
    else: WaitAndClick(image2,0)

def quick_list():
    if not full_contract_reg.exists(full_contract,2): 
        hover(player)
        sleep(1)
        WaitAndClick(to_sell_player, 2)
        print "0"
    try:
        for n in range(1, 100):
            print "1"
            wait(full_contract,8)
            print "2"
            hover(Location(520, 10))
            wait(quick_list_png,8)
            click(quick_list_png)            
            print "3"
            hover(Location(520, 10))
            print "4"
            #wait(quick_list_png,5)  
            #click(quick_list_png)
            wait(min_price_sel,8)
            click(min_price_sel)
            print "5"
            if full_contract_reg.exists(player_rare,0):
                type(Key.BACKSPACE + Key.BACKSPACE + Key.BACKSPACE + Key.BACKSPACE + Key.BACKSPACE + sell_min_rare + Key.TAB + Key.TAB + Key.TAB + sell_max_rare)   
            else:
                type(Key.BACKSPACE + Key.BACKSPACE + Key.BACKSPACE + Key.BACKSPACE + Key.BACKSPACE + sell_min + Key.TAB + Key.TAB + Key.TAB + sell_max)   
            click(ok_yellow)
            sleep(10)
            wait(quick_list_png,8)
            print "Finished loop"
        click(home)            
    except FindFailed:
            print "no contracts"
            click(home) 

def QuickListBidWon():
    wait(won_contract,5)
    click(remove_all_experied)
    sleep(5)
    if not full_contract_reg.exists(full_contract,0): 
        click(won_contract)
    try:
        for n in range(1, 100):
            wait(full_contract,5)
            wait(send_to_the_club,5) 
            click(getLastMatch())
            hover(transfer_target)          
    except FindFailed:
            click(home)
            sleep(5) 
            
def SetBuyNowMinMax():
    print inspect.stack()[0][3]    
    WaitAndClick(min_pirce_buy,10)
    type(str(random.choice((0, 0, 100, 150))) + Key.TAB + Key.TAB + Key.TAB + str(random.choice(to_random)))  
    WaitAndClick(search_button,3)
    hover(Location(520, 10))

def ClickOnTransferTarget():
    print inspect.stack()[0][3]    
    WaitAndClick(transfer_target,3)

def ClickOnTransfer():
    print inspect.stack()[0][3]    
    ClickFirstOrSecond(transfers_tab_selected, transfers_tab,5)    

def ClickOnTransferMarket():
    print inspect.stack()[0][3]    
    ClickFirstOrSecond(transfer_market_selected, transfer_market,5)  

def ClickOnConsumables():
    print inspect.stack()[0][3]    
    ClickFirstOrSecond(consumables_tab_selected,consumables_tab,5)

def ClickOnMyClub():
    hover(Pattern("my_club.png").similar(0.50))

def ClickOnMyClubConsumables():
    ClickOnMyClub()
    hover(Pattern("staff.png").similar(0.80))
    WaitAndClick(Pattern("club_consumables.png").similar(0.90),3)
    
def ClickOnMyClubConsumablesContracts():
    hover(Pattern("home.png").similar(0.80))
    WaitAndClick(Pattern("my_CLub_Consumables_Contracts.png").similar(0.60), 10)
        
def GoToTransferListAndRelist():
    print inspect.stack()[0][3] 
    ClickOnTransfer()
    sleep(3)
    click("transfer_list.png")
    sleep(10)
    try:
        print "trying to remove all sold items"
        wait(player,15)
        WaitAndClick(Pattern("remove_all_sold.png").similar(0.50),15)      
    except FindFailed:
        pass
    try:
        print "trying to relist all sold items"
        sleep(10)
        WaitAndClick(Pattern("RE-LIST-ALL.png").similar(0.60),15)
        sleep(10)
    except FindFailed:
        pass

@timing
def SelectGoldContracts():
    print inspect.stack()[0][3]    
    WaitAndClick("reset_button.png",3)
    wait(Pattern("training_pic.png").similar(0.90),2)
    WaitAndClick(Pattern("player_traning.png").similar(0.90),3)
    WaitAndClick(Pattern("contracts-type.png").similar(0.90),3)
    wait(Pattern("contract_logo.png").similar(0.90),2)        
    WaitAndClick(Pattern("type.png").exact().targetOffset(1,48),5)
    WaitAndClick(Pattern("gold_search.png").similar(0.90),5)
    wait(Pattern("gold_logo.png").similar(0.80),3)
    
@timing
def GoToContracts():
    print inspect.stack()[0][3]
    ClickOnTransfer()
    ClickOnTransferMarket()
    ClickOnConsumables()
    SelectGoldContracts()
    
def GoToSavedContracts():
    print inspect.stack()[0][3]
    try:
        ClickOnMyClubConsumables()    
        ClickOnMyClubConsumablesContracts()
    except FindFailed:
        print "Navigation to consumables failed, trying again"
        StartScript()

def ListSavedContracts():
    print inspect.stack()[0][3]
    GoToSavedContracts()
    quick_list()

def SaveWonContracts():
    print inspect.stack()[0][3]
    ClickOnTransferTarget()
    QuickListBidWon() 

def BuyGoldContracts():
    print inspect.stack()[0][3]
    try:        
        if exists("back_button.png", 2):
            print "Something found, doing shopping"
            IterateAllContracts()
        else:
            find(Pattern("OK.png").similar(0.80).targetOffset(29,0))
            click(getLastMatch())               
    except FindFailed:
        print "failed with some capturing, starting from scratch"
        pass

@timing
def IterateAllContracts():
    print inspect.stack()[0][3]
    global player
    if exists(player,2):
        try:
            for x in findAll(player):
                con_reg.click(random.choice(list(findAll(player))))
                hover(Location(520, 10))
                if full_contract_reg.exists(full_contract,2): 
                    print "clicked on contract"
                    BuyingProcedure()
                else:
                    IterateAllContracts()
        except FindFailed:
            print "Starting search again"
            pass        
    try:
        ClickArrowAndContinue()
    except FindFailed:
        pass
    
def ClickArrowAndContinue():
    print " trying to click arrow"
    click(Pattern("next_page_arrow_active.png").similar(0.65).targetOffset(11,-1))
    hover(Location(520, 10))
    IterateAllContracts()
                   
def BuyingProcedure():   
    print inspect.stack()[0][3] 
    try:
        if exists(Pattern("buy_now_button.png").similar(0.50),1) and full_contract_reg.exists(full_contract,1):
        #if  full_contract_reg.exists(full_contract,3) and bid_reg.exists(Pattern("bid_price.png").similar(0.80),2) and bid_reg.exists(Pattern("make_bid_button.png").exact(),1):    
            click("buy_now_button.png")
            print "doing bind"
            #click(Pattern("make_bid_button.png").similar(0.90).targetOffset(104,1))
            WaitAndClick(Pattern("buy_now_button_ok.png").similar(0.80).targetOffset(-12,6),2)
            #succsess = BidNotAcceptedChecking()
            succsess = BuyNotAcceptedChecking()
            print "Contract bought : " + str(succsess) 
            if succsess == "yes": 
                SaveOrSell(sell)                    
        else:
            print "Failed to BID, starting search from again"
            #if trans_target_reg.exists(trans_target,0):            
            #    SaveWonContracts() 
    except FindFailed:
        print "failed with some capturing, starting search from again"
        #if trans_target_reg.exists(trans_target,0):
        #    SaveWonContracts()
        #pass

def SellContractImmediately():
    print inspect.stack()[0][3]
    WaitAndClick(quick_list_png,3)
    WaitAndClick(Pattern("min_price_sell.png").similar(0.90).targetOffset(20,0),2)
    type(Key.BACKSPACE + Key.BACKSPACE + Key.BACKSPACE + Key.BACKSPACE + Key.BACKSPACE + sell_min + Key.TAB + Key.TAB + sell_max)
    WaitAndClick("submit_list_ok.png",3)
    sleep(1)
    print "contract SENT to MARKET!!!"

def SaveOrSell(sell):
    print inspect.stack()[0][3] 
    if sell=="y":
        SellContractImmediately()
    else: 
        WaitAndClick(send_to_the_club,10) 
        print "Saved contract"

@timing
def InitiateMarketWipe(first_hour):
    print inspect.stack()[0][3]
    print first_hour 
    current_hour = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H')
    print current_hour
    if first_hour != current_hour:
        print "doing market WIPE"
        AutoAssignAll()        
        GoToTransferListAndRelist()
        print "Listing contracts"
        ListSavedContracts()
        first_hour = current_hour              
    else:
        pass
    return first_hour

def BuyNotAcceptedChecking():
    print inspect.stack()[0][3]
    if exists(send_to_the_club,2):
        bought = "yes"
        global contracts_bought 
        contracts_bought += 1
        print "bought CONTRACTS: " + str(contracts_bought)
    elif exists("bid_not_accepted.png",2):
        print "YOR BID outbid((("
        click("OK.png")
        bought = "no"
    else:
        global contracts_bought 
        contracts_bought += 1
        print "Probably bought CONTRACTS: " + str(contracts_bought)
        bought = "yes"
    return bought

def BidNotAcceptedChecking():
    print inspect.stack()[0][3]
    if exists(Pattern("green_check_box.png").similar(0.80),2):
        bought = "yes"
        global contracts_bought 
        contracts_bought += 1
        print "bought CONTRACTS: " + str(contracts_bought)
    elif exists("bid_not_accepted.png",1):
        print "YOR BID outbid((("
        click("OK.png")
        bought = "no"
    else:
        global contracts_bought 
        contracts_bought += 1
        print "Probably bought CONTRACTS: " + str(contracts_bought)
        bought = "yes"
    return bought

@timing
def AutoAssignAll():
    print inspect.stack()[0][3]
    if exists(Pattern("unassigned.png").similar(0.80),0):
        try:
            click(Pattern("unassigned.png").similar(0.80))
            print "Assigning unassigned"
            WaitAndClick("auto_assign_allss.png",2)
        except FindFailed:
            pass

def StartScript():
    print inspect.stack()[0][3]
    global round 
    global first_hour 
    round += 1
    print "Global attempt = " + str(round)
    if exists(Pattern("OK.png").similar(0.90),0):
        click(getLastMatch())
    elif exists(Pattern("application_error.png").similar(0.80),0):
        print "application_error!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
        click(Pattern("close_browser.png").targetOffset(32,-4))
        sleep (4)
        #type(Key.F5, KeyModifier.CTRL)
        click("firefox_icon.png")
        sleep(30)
    try:
        while True:
            first_hour = InitiateMarketWipe(first_hour)
            GoToContracts()
            SetBuyNowMinMax()
            BuyGoldContracts()
#              
    except FindFailed:
        try:
            click(Pattern("OK.png").similar(0.80))
            StartScript()
        except FindFailed:
            StartScript()        

 
#StartScript()
# 
AutoAssignAll()        
GoToTransferListAndRelist()
ListSavedContracts()
