from login import CreditLogin
import unittest


class TestIndividualcustomers(unittest.TestCase):


    def setup(self):
        print('开始测试')

    def testhome_login(self):
        # 创建对象获取元素
        dr = CreditLogin('http://172.21.1.146:8180/xyjk-erp-app-pc/login')
        dr.getweb()
        dr.wait()
        dr.input_text('506024', '//*[@placeholder="请输入您的用户名"]')
        dr.input_text('1', '//*[@placeholder="请输入您的密码"]')

        # 获取点击按钮,点击登录
        # c.button_click('//*[@id="loginForm"]/div/div[7]/button')
        dr.find_element('//*[@id="loginForm"]/div/div[7]/button').click()

    def teardown(self):
        print('测试结束')


if __name__ == '__main__':
    unittest.main()
