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


class QuotaApply(CreditLogin):

    def __init__(self, url):
        super().__init__(url)
        self.end_flag = 0
        self.quota_data_list = login_read('B', '../../146/data/quota.xlsx')

    def people_choice(self):
        # 获取下一审批人的登录名
        quota_login_name = self.regular_expression(self.find_element(Summary.quota_next_login_name).text)
        print(quota_login_name)
        # 点击下一节点审批人
        time.sleep(2)
        self.button_click(Summary.quota_apply_next_Approval_button)
        # 点击选择审批人界面的提交按钮
        time.sleep(2)
        self.button_click(Summary.quota_select_person_submit_button)
        return quota_login_name

    def quota_first_apply(self):
        self.home_login()
        print(self.quota_data_list)
        self.driver.implicitly_wait(10)
        # 鼠标移动到额度管理模块
        self.move(Summary.quota_management)
        # 点击额度申请
        self.button_click(Summary.quota_apply)
        self.driver.implicitly_wait(10)
        # 点击新增额度
        self.button_click(Summary.quota_new_button)
        self.move(Summary.sign_out)
        self.driver.implicitly_wait(10)
        # 点击个人客户按钮
        self.button_click(Summary.quota_personal_cust_button)
        self.wait()
        # 输入申请额度的客户号进行查询

        self.input_text(self.quota_data_list[2], Summary.quota_cust_name_input)
        self.button_click(Summary.quota_cust_search_button)
        # 此处要强制等待3秒，等待界面加载完毕
        time.sleep(3)
        # 选中所要申请的客户
        for i in range(2, 4):
            try:
                self.button_click(Summary.quota_select_cust[i])
            except:
                print("未找到")
            else:
                break
        # 点击确定按钮
        self.button_click(Summary.quota_first_confirm_button)
        self.driver.implicitly_wait(10)
        # 清除输入框
        self.find_element(Summary.quota_special_input).send_keys(Keys.CONTROL, 'a')
        # 输入专项金额
        self.find_element(Summary.quota_special_input).send_keys(self.quota_data_list[3])
        time.sleep(1)
        self.button_click(Summary.quota_date_select)
        time.sleep(1)
        self.button_click(Summary.quota_date_select_year)
        # 输入额度有效时长
        self.input_text(self.quota_data_list[4], Summary.quota_effective_date)
        time.sleep(1)
        # 担保方式选择
        self.button_click(Summary.quota_Guaranteed_method_select)
        # 担保方式说明输入
        self.input_text(self.quota_data_list[5], Summary.quota_Guaranteed_method_input)
        # 保存以上输入信息
        self.button_click(Summary.quota_apply_save_button)
        self.wait()
        # 通过页面刷新,TAB键控制滚动条滚动到额度明细中的新增按钮
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
        self.find_element(Summary.quota_detail_new_apply_button).send_keys(Keys.TAB)
        # 点击额度明细中的新增按钮
        self.button_click(Summary.quota_detail_new_apply_button)
        # 点击额度类型选择专项额度
        time.sleep(1)
        self.button_click(Summary.quota_type_input)
        time.sleep(1)
        self.button_click(Summary.quota_type_input_special)
        # 点击选择额度分项框
        self.button_click(Summary.quota_item_input)
        # 点击一级加号
        self.button_click(Summary.quota_first_plus_expand)
        # 点击二级加号
        self.button_click(Summary.quota_second_plus_expand)
        # 点击个人政策性贷款
        self.button_click(Summary.quota_item_input_personal_quota)
        # 输入分项金额
        self.input_text(self.quota_data_list[3], Summary.quota_item_cash_input)
        # 是否可循环额度选择
        select = self.find_element(Summary.quota_loop_select)
        Select(select).select_by_index(2)
        # 点击保存额度明细信息
        self.button_click(Summary.quota_detail_save_button)
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
        # 控制滚动条滚至底部
        self.find_element(Summary.quota_finally_submit_button).send_keys(Keys.TAB)
        # 点击页面底部的同意按钮
        self.button_click(Summary.quota_first_admit_button)
        self.process_end_judgment()

    def quota_login_name_write(self):
        quota_next_login_name = self.people_choice()
        print(quota_next_login_name[0])
        # # 输入最终的审批意见
        # self.input_text(Summary.data_list[5], Summary.quota_apply_opinion_input)
        # # 点击最终的提交按钮
        # self.button_click(Summary.quota_finally_submit_button)
        if quota_next_login_name:
            login_write(quota_next_login_name[0], '../../146/data/quota.xlsx')
        else:
            login_write(0)

    def second_application(self):
        login_name = login_read('C', '../../146/data/quota.xlsx')[0]
        print(login_name)
        if self.end_flag != 1:
            # 点击退出登录
            self.button_click(Summary.sign_out)
            # 切换账户,进行登录
            self.wait()
            self.home_login(login_name)
            self.wait()
            # 从待办列表中点击要审批的业务
            quota_cust_name = self.quota_data_list[0]
            quota_to_do_list = '//*[@class="module_box"]/div/div/table/tbody/tr/td[text()="{}"]'.format(quota_cust_name)
            self.button_click(quota_to_do_list)
            self.wait()
            # 滚动到页面最底部
            self.scroll_bar()
            time.sleep(1)
            self.scroll_bar()
            # # 点击同意按钮
            self.button_click(Summary.quota_first_admit_button)
            self.process_end_judgment()
        else:
            self.driver.quit()
        return self.end_flag

    def process_end_judgment(self):
        try:
            self.button_click(Summary.select_person_button)
        except:
            self.end_flag = 1
            print("当前审批流程已结束")

        else:
            self.quota_login_name_write()
            # 输入审批意见
            self.wait()
        finally:
            input_opinion = self.quota_data_list[6]
            self.input_text(input_opinion, Summary.approval_opinions)
            # 最后点击提交
            self.wait()
            self.button_click(Summary.quota_finally_submit_button)
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
            self.second_application()



# a = QuotaApply(basicurl[0])
# a.quota_first_apply()

