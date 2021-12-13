import time
import re
from gan.service.login import CreditLogin
from gan.service.login import login_read
from gan.service.login import login_write
from gan.element.getelement import Summary
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select



basicurl = ['http://172.21.1.146:8180/xyjk-erp-app-pc/login', 'http://172.21.4.34:8080/xyjk-erp-app-pc/login']


class NewContracts(CreditLogin):

    def __init__(self, url):
        super().__init__(url)
        self.end_flag = 0
        with open(r'D:\test\146\data\prj_num.txt', encoding='utf-8') as f:
            self.prj_number = f.read()
        self.ctr_numb = None
    contract_data_list = login_read('B', '../../146/data/quota.xlsx')
    print(contract_data_list)

    def contracts_first_apply(self):
        self.home_login()
        self.driver.implicitly_wait(10)
        # 鼠标移动到合同管理模块
        self.move(Summary.contract_management)
        # 点击新增合同
        self.button_click(Summary.contract_new_contract)
        self.move(Summary.contract_fast)
        self.driver.implicitly_wait(10)
        # # 输入新增合同的客户名称进行筛选
        # self.input_text(NewContracts.contract_data_list[0], Summary.contract_cust_name_input)
        # 输入业务编号进行筛选
        self.input_text(self.prj_number, Summary.contract_prj_numb_input)
        self.driver.implicitly_wait(10)
        # 点击新增合同页面的查询按钮
        self.button_click(Summary.contract_search_button)
        time.sleep(1)
        self.button_click(Summary.contract_select_button)
        # 点击制作合同按钮
        self.button_click(Summary.contract_make_button)
        time.sleep(3)
        # 获取当前合同编号
        js = 'return document.getElementById("ctrNumb").value'
        self.ctr_numb = self.driver.execute_script(js)
        print(self.ctr_numb)
        with open(r'D:\test\146\data\ctr_num.txt', 'w') as f:
            f.write(self.ctr_numb)

        # 输入纸质合同编号
        self.input_text(NewContracts.contract_data_list[9], Summary.contract_paper_id_input)
        # 点击贷款投向输入框
        self.button_click(Summary.contract_loan_invested)
        self.driver.implicitly_wait(10)
        self.button_click(Summary.contract_loan_invested_first_plus)
        self.driver.implicitly_wait(10)
        self.button_click(Summary.contract_loan_invested_second_plus)
        self.driver.implicitly_wait(10)
        self.button_click(Summary.contract_loan_invested_info)
        # 输入贷款用途详细说明
        self.input_text(NewContracts.contract_data_list[10], Summary.contract_loan_invested_detail_input)
        # 选择是否新增贷款
        self.button_click(Summary.contract_newloan_judge)
        self.button_click(Summary.contract_newloan)
        # 点击保存以上信息
        self.button_click(Summary.contract_first_save_button)
        time.sleep(3)
        # 使用TAB键转到第二个保存按钮的位置，利率信息保存
        second_save = self.find_element(Summary.contract_second_save_button)
        self.find_element(Summary.contract_second_save_button).send_keys(Keys.TAB)
        self.driver.execute_script("arguments[0].click();", second_save)
        time.sleep(3)
        # 使用TAB键转到第二个保存按钮的位置，进行还款账户填写
        self.find_element(Summary.contract_tab).send_keys(Keys.TAB)
        # 输入放款账户
        self.input_text(NewContracts.contract_data_list[11], Summary.contract_lending_account_input)
        # 输入还款账户
        self.driver.implicitly_wait(10)
        self.find_element(Summary.contract_repay_account_input).clear()
        self.input_text(NewContracts.contract_data_list[11], Summary.contract_repay_account_input)
        self.wait()
        # 贴息贷款用
        # self.button_click(Summary.contract_discount_loan)
        # self.button_click(Summary.contract_discount_loan_true)
        # self.wait()
        # 点击保存按钮
        self.button_click(Summary.contract_third_save_button)
        time.sleep(3)
        # 使用他tab键转到贷款试算按钮位置，并进行点击操作
        loan_trial_calculation_button = self.find_element(Summary.contract_Loan_trial_calculation_button)
        self.find_element(Summary.contract_Loan_trial_calculation_button).send_keys(Keys.TAB)
        self.driver.execute_script("arguments[0].click();", loan_trial_calculation_button)
        self.driver.implicitly_wait(10)
        self.find_element(Summary.loan_area_province).send_keys(Keys.TAB)
        time.sleep(3)
        self.find_element(Summary.loan_area_province).click()
        self.driver.implicitly_wait(10)
        time.sleep(1)
        self.find_element(Summary.loan_area_province_select).click()
        self.find_element(Summary.loan_area_city).click()
        time.sleep(1)
        self.driver.implicitly_wait(10)
        self.find_element(Summary.loan_area_city_select).click()
        time.sleep(1)
        self.find_element(Summary.loan_area_line).click()
        self.driver.implicitly_wait(10)
        self.find_element(Summary.loan_area_line_select).click()

        fouth_save_button = self.find_element(Summary.contract_fouth_save_button)
        self.find_element(Summary.contract_fouth_save_button).send_keys(Keys.TAB)
        self.driver.execute_script("arguments[0].click();", fouth_save_button)


        self.scroll_bar()
        self.wait()
        # 点击同意按纽
        self.button_click(Summary.contract_admit_button)
        end_flag = self.contract_process_end_judgment()
        return end_flag

    def contract_people_choice(self):
        contract_login_name = self.regular_expression(self.find_element(Summary.contract_next_login_name).text)
        print(contract_login_name)
        self.driver.implicitly_wait(10)
        # 点击下一节点审批人
        self.button_click(Summary.first_approver_button)
        # 点击选人页面的提交按钮
        self.driver.implicitly_wait(10)
        self.button_click(Summary.approver_list_button)
        return contract_login_name

    def contract_process_end_judgment(self):
        try:
            self.button_click(Summary.select_person_button)
        except:
            self.end_flag = 1
            print("当前审批流程已结束")

        else:
            self.contract_login_name_write()
            self.wait()
        finally:
            input_opinion = NewContracts.contract_data_list[12]
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
            self.contract_second_application()
        return self.end_flag

    def contract_login_name_write(self):
        contract_next_login_name = self.contract_people_choice()
        if contract_next_login_name:
            login_write(contract_next_login_name[0], '../../146/data/contract.xlsx')
        else:
            login_write(0)

    def contract_second_application(self):
        login_name = login_read('C', '../../146/data/contract.xlsx')[0]
        print(login_name)
        if self.end_flag != 1:
            # 点击退出登录
            self.button_click(Summary.sign_out)
            # 切换账户,进行登录
            self.wait()
            self.home_login(login_name)
            self.wait()
            # 从待办列表中点击要审批的业务
            contract_to_do_list = f'//*[@class="module_box"]/div/div/table/tbody/tr/td[text()="{NewContracts.contract_data_list[0]}"]'
            self.button_click(contract_to_do_list)
            self.wait()
            # 滚动到页面最底部
            self.scroll_bar()
            time.sleep(1)
            self.scroll_bar()
            # # 点击同意按钮
            self.wait()
            self.button_click(Summary.final_admit_button)
            self.contract_process_end_judgment()
        else:
            self.driver.quit()
        return self.end_flag


# c = NewContracts(basicurl[0])
# c.contracts_first_apply()
