from Sikuli import *


round=0
contracts_bought=0
sell="n"

items_to_sell=100
sell_min=str(350)
sell_max=str(400)
sell_min_rare=str(700)
sell_max_rare=str(750)


full_contract=Pattern("full_player_manager.png").exact().targetOffset(-1,-38)
player=Pattern("manager_contract.png").similar(0.90).targetOffset(-6,-42)

player=Pattern("player_contract.png").similar(0.80).targetOffset(-1,-38)
player_rare=Pattern("player_rare.png").exact()
full_contract=Pattern("full_player_contract.png").similar(0.89)
won_contract=Pattern("won_contract.png").similar(0.90)

full_contract_reg = Region(8,335,590,261)
bid_reg = Region(368,381,472,185)
trans_target_reg=Region(559,445,267,47)
con_reg = Region(32,536,975,308)

transfers_tab_selected = Pattern("transfers_tab_selected.png").similar(0.90)
transfers_tab = Pattern("transfers_tab.png").similar(0.90)
consumables_tab_selected = Pattern("consumables_tab_selected.png").similar(0.90)
consumables_tab = Pattern("consumables_tab.png").similar(0.90)

trans_target=Pattern("trans_target_50.png").exact()
both_contract=Pattern("common_contract.png").similar(0.80) #any item


quick_list_png = Pattern("quick_list.png").exact()
min_price_sel = Pattern("min_price_sell.png").similar(0.95).targetOffset(21,-1)
ok_yellow = Pattern("submit_list_ok.png").similar(0.90)
home = Pattern("home.png").similar(0.60)
remove_all_experied = Pattern("remove_all_experied.png").similar(0.50)
send_to_the_club = Pattern("send_to_the_club.png").similar(0.80)
transfer_target = Pattern("transfer_target.png").similar(0.80)
min_pirce_buy = Pattern("min_pirce_buy.png").similar(0.96).targetOffset(88,2)
search_button = Pattern("search_button.png").similar(0.80)
