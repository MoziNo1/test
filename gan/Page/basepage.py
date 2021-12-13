from selenium import webdriver
from selenium.webdriver import ActionChains
import openpyxl
import re
import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By


class PageCredit(object):

    def __init__(self, url):
        self.driver = webdriver.Firefox()
        self.url = url

    def getweb(self):
        self.driver.get(self.url)

    # 定位元素
    def find_element(self, *loc):
        return self.driver.find_element_by_xpath(*loc)

    # 输入框输入文本
    def input_text(self, key, *loc):
        return self.find_element(*loc).send_keys(key)

    # 点击按钮
    def button_click(self, *loc):
        self.find_element(*loc).click()

    def move(self, *loc):
        ActionChains(self.driver).move_to_element(self.find_element(*loc)).perform()

    # 控制滚动条到底部
    def scroll_bar(self):
        js = "window.scrollTo(0,document.documentElement.scrollHeight)"
        self.driver.execute_script(js)

    def scroll_bar_top(self):
        js = "window.scrollTo(document.body.scrollHeight, 0)"
        self.driver.execute_script(js)

    def page_refresh(self):
        return self.driver.refresh()

    def wait(self):
        time.sleep(3.5)
        # self.driver.implicitly_wait(5)

    # 正则表达式，提取”（）“中的内容
    @staticmethod
    def regular_expression(string):
        rule = re.compile(r"[(](.*?)[)]", re.S)
        return re.findall(rule, string)

    # 执行js显示下拉框
    def show_select(self):
        js = 'document.querySelectorAll("select")[1].style.display="block"'
        self.driver.execute_script(js)

    # def select_choose(self, *loc, index):
    #     select = self.find_element(*loc)
    #     Select(select).select_by_value(index)



