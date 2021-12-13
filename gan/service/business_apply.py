import time
import re

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from gan.service.login import CreditLogin
from gan.service.login import login_read
from gan.service.login import login_write
from gan.service.login import login_write_sql
from gan.service.login import login_full_write
from gan.element.getelement import Summary
import pymysql
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from gan.service.quota_apply import QuotaApply

basicurl = ['http://172.21.1.146:8180/xyjk-erp-app-pc/login', 'http://172.21.4.34:8080/xyjk-erp-app-pc/login']


class Business(CreditLogin):

    # global  business_data_list
    cust_no = input("请输入您的证件号码：")

    def __init__(self, url):
        super().__init__(url)
        self.login_user = self.home_login()
        # 用于判断流程是否结束的变量
        self.end_flag = 0
        self.prj_numb = None
        self.wait_time = WebDriverWait(self.driver,10,0.5)


    def mysql(self):
        # 数据查询相关数据，并将数据写入excel
        login_full_write('B', 3, Business.cust_no, '../../146/data/quota.xlsx')
        db_connect = pymysql.connect(host="172.21.12.33", db="db_credit_0929",user="root", password="root1234")
        cur = db_connect.cursor()
        # 数据库查询该客户是否有额度
        cust_search_sql = f"""
               select Cust_Nm,Cust_Numb from cust_personal where Ctf_Nbr="{Business.cust_no}" and tenant_id in 
                (select tenant_id from sys_user where login_name="{self.login_user}")
                """
        cur.execute(cust_search_sql)
        cust_data = cur.fetchall()
        print(cust_data)
        login_write_sql(cust_data[0][0], cust_data[0][1], '../../146/data/quota.xlsx')
        cur.close()
        cur1 = db_connect.cursor()
        quota_search_sql = f"""select * from crlmt_crg_inf where Cst_Numb = "{cust_data[0][1]}" and Lmt_StCd = "1"
            """
        self.mm = cur1.execute(quota_search_sql)
        # business_data_list = login_read('B', '../../146/data/quota.xlsx')
        # print(business_data_list)
        # print(self.mm)

    business_data_list = login_read('B', '../../146/data/quota.xlsx')

    # 额度下的业务申请流程
    def under_quota(self):
        # 点击申请的额度流水号
        ele_id = self.find_element(Summary.business_change_id).get_attribute("id")
        apply_quota = []
        for i in range(1, 10):
            mi = '//*[@id="{}"]/table/tbody/tr[{}]/td[2]'.format(ele_id, i)
            apply_quota.append(mi)
            for i in range(2, 6):
                try:
                    self.button_click(apply_quota[i])
                except:
                    # print(apply_quota[i])
                    print("未找到")
                else:
                    break

    # 判断走业务流程还是非业务流程
    def quota_yes_no(self):
        if self.mm != 1:
            a = QuotaApply(basicurl[0])
            a.quota_first_apply()
            # 当客户额度表中无生效的数据，等到额度申请流程结束时,在进行业务申请
            if a.end_flag == 1:
                print("额度申请已结束")
                self.home_login(self.login_user)
        else:
            pass

    def business_first_apply(self):
        self.mysql()
        print(self.mm)
        self.quota_yes_no()
        print(self.mm)
        self.driver.implicitly_wait(10)

        # 鼠标移动到要“业务申请”的元素
        # ActionChains(c).move_to_element('/html/body/div[1]/div/div[2]/div[1]/div/div/ul/li[4]/a/span').perform()
        self.move(Summary.business_management)
        self.find_element('/html/body/div[1]/div/div[2]/div[1]/div/div/ul/li[4]/ul/li[2]/ul/li[1]/a')

        self.button_click(Summary.personal_business_applications)

        # 点击所需业务申请的客户
        # self.button_click(Summary.cust_personal_search)
        self.move(Summary.sign_out)

        # 输入要进行业务申请的客户证件号，进行业务申请操作
        id_card = Business.business_data_list[1]
        # print(id_card)
        self.input_text(id_card, Summary.id_card_input)
        self.button_click(Summary.cust_personal_search)

        self.wait()
        # 点击所要申请的客户
        self.button_click(Summary.individual_customer_quota)

        # 点击业务申请进入下一界面
        self.button_click(Summary.bussiness_apply_button)


        if self.mm != 1:
            self.under_quota()
        else:
            self.wait()
            self.button_click('//*[@id="prjApplyCustomForComCtrl"]/form/div/div/div/div/div[1]/div/input')
            # print(111)
            # business_way = self.find_element(Summary.business_module)
            # print(business_way.text)
            # Select(business_way).select_by_index(2)

            self.button_click(Summary.business_module_single)

        # self.button_click(apply_quota)
        # 点击产品输入框选择产品
        if self.mm != 1:

            self.button_click(Summary.product_name_input[0])
            self.button_click(Summary.product_name[0])
            self.button_click(Summary.confirm_button[0])
        else:
            self.button_click(Summary.product_name_input[1])
            # 点击产品名称
            # 点击一级产品加号
            self.button_click(Summary.one_product_plus)
            self.button_click(Summary.second_product_plus)
            self.button_click(Summary.third_product_plus)
            self.button_click(Summary.product_name[1])
            self.wait()
            self.button_click(Summary.confirm_button[1])
        # 点击页面确认按钮，进入业务信息填写界面
        # self.button_click(Summary.confirm_button)

        # 页面切换，进行业务信息填写
        # time.sleep(3)
        self.wait_time.until(EC.visibility_of_any_elements_located((By.XPATH, Summary.apply_amount)))
        js = 'return document.getElementById("prjNumb").value'
        self.prj_numb = self.driver.execute_script(js)
        print(self.prj_numb)
        with open(r'D:\test\146\data\prj_num.txt', 'w') as f:
            f.write(self.prj_numb)
        # 贷款金额输入
        input_cash = Business.business_data_list[6]
        self.input_text(input_cash, Summary.apply_amount)
        # 点击业务开始日期输入0
        self.button_click(Summary.business_start_date)
        # 点击日期确定按钮
        self.button_click(Summary.business_start_date_button)
        # 点击业务结束日期输入
        self.button_click(Summary.business_end_date)
        # 向后调整一年z
        self.button_click(Summary.next_date_adjust)
        # 点击日期确定按钮
        self.button_click(Summary.business_end_date_button)
        # 选择一次性放款
        self.button_click(Summary.lending_options)
        # 输入贷款执行利率
        input_rate = Business.business_data_list[7]
        self.input_text(input_rate, Summary.execution_rate)
        # 输入申请期限
        input_date = Business.business_data_list[8]
        self.find_element(Summary.application_period).clear()
        self.input_text(input_date, Summary.application_period)
        # 点击保存按钮
        self.button_click(Summary.save_button)
        self.scroll_bar()
        time.sleep(0.5)
        self.scroll_bar()
        # 控制滚动条滚到底部
        # 点击同意按钮前必须强制等待2秒，否则会点击不了元素
        # self.wait_time.until(EC.visibility_of_any_elements_located((By.XPATH, Summary.business_admit_button)))
        time.sleep(2)

        self.button_click(Summary.business_admit_button)
        end_flag = self.business_process_end_judgment()
        return end_flag

    def business_people_choice(self):
        business_login_name = self.regular_expression(self.find_element(Summary.next_login_name).text)
        print(business_login_name)

        # 点击下一节点审批人
        self.button_click(Summary.first_approver_button)
        # 点击选人页面的提交按钮

        self.button_click(Summary.approver_list_button)
        return business_login_name

    def business_process_end_judgment(self):
        try:
            self.button_click(Summary.select_person_button)

        except:
            self.end_flag = 1
            print("当前审批流程已结束")

        else:
            self.business_login_name_write()
            self.wait()
        finally:
            input_opinion = Business.business_data_list[12]
            self.input_text(input_opinion, Summary.approval_opinions)
            # 最后点击提交
            self.button_click(Summary.finally_submit_button)
            self.wait()
            self.page_refresh()
            self.driver.implicitly_wait(10)
            try:
                if self.find_element(Summary.end_card_info):
                    try:
                        self.button_click(Summary.end_card_info)
                    except Exception as e:
                        pass
            except Exception as e:
                pass
            self.business_second_application()
        return self.end_flag

    def business_login_name_write(self):
        business_next_login_name = self.business_people_choice()
        if business_next_login_name:
            login_write(business_next_login_name[0], '../../146/data/quota.xlsx')
        else:
            login_write(0)

    def business_second_application(self):
        # 判断业务流程是否完全结束，用于合同申请
        # business_judge = 0
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
            cust_name = Business.business_data_list[0]
            business_to_do_list = '//*[@class="module_box"]/div/div/table/tbody/tr/td[text()="{}"]'.format(cust_name)
            self.button_click(business_to_do_list)
            self.wait()
            # 滚动到页面最底部
            self.scroll_bar()
            time.sleep(1)
            self.scroll_bar()
            # # 点击同意按钮
            self.button_click(Summary.business_admit_button)
            self.business_process_end_judgment()
        else:
            self.driver.quit()

#
b = Business(basicurl[0])
b.business_first_apply()
# # prj_number = b.prj_numb
# print(prj_number)
