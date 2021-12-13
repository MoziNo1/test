from selenium import webdriver
import time
import openpyxl
import xlrd


class Login(object):

    def auto_login_146(self):
        dr = webdriver.Chrome()
        url = 'http://172.21.1.146:8180/xyjk-erp-app-pc/login'
        dr.get(url)

        current_window = dr.current_window_handle

        dr.maximize_window()
        print(dr.current_url)
        time.sleep(3)

        excel = openpyxl.open('../146/data/146_login_name.xlsx')
        worksheet = excel.worksheets[0]

        row = worksheet.max_row
        column = worksheet.max_column

        login_name_list = []
        for rows in range(row + 1)[2:]:
            position = 'A' + str(rows)
            login_name = worksheet[position].value
            login_name_list.append(login_name)

        login_password_list = []
        for rows in range(row + 1)[2:]:
            position = 'B' + str(rows)
            login_name = worksheet[position].value
            login_password_list.append(login_name)

        # for i in range(len(login_name_list)):
        login_name = dr.find_element_by_xpath("//*[@placeholder='请输入您的用户名']")
        login_password = dr.find_element_by_xpath('//*[@placeholder="请输入您的密码"]')
        login_button = dr.find_element_by_css_selector('.btnlogin')
        login_name.send_keys(login_name_list[0])
        login_password.send_keys(login_password_list[0])
        time.sleep(3)
        login_button.click()
        # time.sleep(2)
        # dr.back()
        # time.sleep(2)
        # dr.get('http://172.21.1.146:8180/xyjk-erp-app-pc/login?operType=logout')
        return dr.current_url





