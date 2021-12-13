from gan.Page.basepage import PageCredit
from gan.service.login import CreditLogin
from selenium.webdriver.support.select import Select

url = 'http://172.21.1.146:8180/xyjk-erp-app-pc/login'
dr = CreditLogin(url)
dr.home_login()
dr.wait()
todo = '//*[@class="ng-scope"]//table/tbody/tr[1]/td[1]'
dr.button_click(todo)
dr.wait()
# tragile = '//*[@id="cnclAfVerfsaveCnclAfVerfTrans"]/div/form/div[4]/div/div[3]/div[2]/div/div/i'
# dr.button_click(tragile)
dr.show_select()
select_option = dr.find_element('//*[@id="cnclAfVerfsaveCnclAfVerfTrans"]/div/form/div[4]/div/div[3]/div[2]/select')
select_object = Select(select_option)
# 通过索引查找
# select_object.select_by_index(12)
# 通过value查找
select_object.select_by_value('CNY')
# 通过text查找
# select_object.select_by_visible_text('人民币')
