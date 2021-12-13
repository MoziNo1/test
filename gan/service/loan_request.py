import time
import re
from gan.service.login import CreditLogin
from gan.service.login import login_read
from gan.service.login import login_write
from gan.element.getelement import Summary
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


basicurl = ['http://172.21.1.146:8180/xyjk-erp-app-pc/login', 'http://172.21.1.34:8180/xyjk-erp-app-pc/login']


class LoanRequest(CreditLogin):

    def __init__(self, url):
        super().__init__(url)
        self.end_flag = 0
        with open(r'D:\test\146\data\ctr_num.txt', encoding='utf-8') as f:
            self.ctr_numb = f.read()

    loan_data_list = login_read('B', '../../146/data/quota.xlsx')
    print(loan_data_list)

    def loan_first_apply(self):
        self.home_login()
        self.driver.implicitly_wait(10)
        # 鼠标移动到要“放款申请”的元素
        # ActionChains(c).move_to_element('/html/body/div[1]/div/div[2]/div[1]/div/div/ul/li[4]/a/span').perform()
        self.move(Summary.loan_request_management)
        self.button_click(Summary.loan_request_button)
        self.driver.implicitly_wait(10)
        # # 输入用户名称
        # self.input_text(LoanRequest.loan_data_list[0], Summary.loan_request_cust_name_input)
        # 输入合同号进行过滤查询
        self.input_text(self.ctr_numb, Summary.loan_request_ctr_numb_input)
        # 进行查询过滤
        self.button_click(Summary.loan_request_search_button)
        self.wait()
        # 点击需要进行放款的合同
        self.button_click(Summary.loan_request_select_cust)
        # 点击发起按钮
        self.button_click(Summary.loan_request_launch)
        # 点击页面的第一个保存按钮
        self.button_click(Summary.loan_request_first_save_button)
        # 点击弹出框中的确认按钮
        self.button_click(Summary.loan_request_pop_up_box)
        # 滚动到第二个保存按钮并点击保存
        time.sleep(3)
        self.find_element(Summary.loan_request_second_save_button).send_keys(Keys.TAB)
        self.button_click(Summary.loan_request_second_save_button)
        # # 滚动到第三个保存按钮并点击保存
        time.sleep(3)
        self.find_element(Summary.loan_request_third_save_button).send_keys(Keys.TAB)
        self.button_click(Summary.loan_request_third_save_button)
        # 滚动到试算按钮并点击
        time.sleep(3)
        self.button_click(Summary.loan_request_calc_button)
        # 滚动到最终的提交按钮，并点击同意按钮
        self.scroll_bar()
        time.sleep(0.5)
        self.scroll_bar()
        # self.find_element(Summary.loan_request_last_submit_button).send_keys(Keys.TAB)
        self.button_click(Summary.loan_request_first_admit_button)
        self.loan_process_end_judgment()

    def loan_people_choice(self):
        loan_login_name = self.regular_expression(self.find_element(Summary.loan_request_next_login_name).text)
        print(loan_login_name)
        self.driver.implicitly_wait(10)
        # 点击下一节点审批人
        self.button_click(Summary.loan_request_choose_person)
        # 点击选人页面的提交按钮
        self.driver.implicitly_wait(10)
        self.button_click(Summary.loan_request_first_submit_button)
        return loan_login_name

    def loan_process_end_judgment(self):
        try:
            time.sleep(1)
            self.button_click(Summary.select_person_button)
        except:
            self.end_flag = 1
            print("当前审批流程已结束")

        else:
            self.loan_login_name_write()
            self.wait()
        finally:
            input_opinion = LoanRequest.loan_data_list[12]
            self.input_text(input_opinion, Summary.approval_opinions)
            # 最后点击提交
            self.button_click(Summary.finally_submit_button)
            self.wait()
            self.page_refresh()
            time.sleep(1)
            try:
                if self.find_element(Summary.end_card_info):
                    try:
                        self.button_click(Summary.end_card_info)
                    except Exception as e:
                        pass
            except Exception as e:
                pass
            self.loan_second_application()

    def loan_login_name_write(self):
        loan_next_login_name = self.loan_people_choice()
        if loan_next_login_name:
            login_write(loan_next_login_name[0], '../../146/data/loan.xlsx')
        else:
            login_write(0)

    def loan_second_application(self):
        login_name = login_read('C', '../../146/data/loan.xlsx')[0]
        print(login_name)
        if self.end_flag != 1:
            # 点击退出登录
            self.button_click(Summary.sign_out)
            # 切换账户,进行登录
            self.wait()
            self.home_login(login_name)
            self.wait()
            # 从待办列表中点击要审批的业务
            loan_to_do_list = '//*[@class="module_box"]/div/div/table/tbody/tr/td[text()="{}"]'.format(LoanRequest.loan_data_list[0])
            self.button_click(loan_to_do_list)
            self.wait()
            # 滚动到页面最底部
            self.scroll_bar()
            time.sleep(1)
            self.scroll_bar()
            # # 点击同意按钮
            self.button_click(Summary.loan_request_first_admit_button)
            self.loan_process_end_judgment()
        else:
            self.driver.quit()

#
# a = LoanRequest(basicurl[0])
# a.loan_first_apply()