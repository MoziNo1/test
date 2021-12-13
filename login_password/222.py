from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from browsermobproxy import Server
import time
import requests
import json


class BaseFramework(object):

    def __init__(self):
        # browsermob-proxy.bat的文件路径
        self.server = Server(r'D:\test\venv\Lib\site-packages\browsermob-proxy-2.1.4\bin\browsermob-proxy.bat')
        self.server.start()
        self.proxy = self.server.create_proxy()
        self.query_url = 'http://query.mallcoo.cn/DBAdmin/GetData'
        chrome_options = Options()
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument('--proxy-server={0}'.format(self.proxy.proxy))
        # chrome_options.add_argument('--headless')  # 无头模式
        # chromedriver.exe的文件路径
        self.browser = webdriver.Chrome(executable_path="C:\Program Files\Google\Chrome\Application\chromedriver.exe", options=chrome_options)

    def process_request(self, request, response):
        pass

    def process_response(self, response, request):
        pass

    def run(self, func, *args):
        self.proxy.new_har(options={
            'captureContent': True,
            'captureHeaders': True
        })
        func(*args)
        result = self.proxy.har
        for entry in result['log']['entries']:
            request = entry['request']
            response = entry['response']
            self.process_request(request, response)
            self.process_response(response, request)
        self.proxy.close()
        self.browser.close()

    def check_params(self, params: list) -> str:
        pass

    def check_mongo(self, track_data: dict) -> str:
        pass


class Framework(BaseFramework):

    def load(self, url):
        self.browser.get(url)
        time.sleep(3)
        self.browser.maximize_window()
        time.sleep(1)
        time.sleep(2)
        self.browser.find_element_by_xpath('//*[@placeholder="请输入您的用户名"]').send_keys('506025')
        self.browser.find_element_by_xpath('//*[@placeholder="请输入您的密码"]').send_keys('1')

        self.browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[7]/button').click()

    def process_request(self, request, response):
        pass

    def process_response(self, response, request):
        print(request['url'])
        # 查找需要数据的URL后即可进行解析
        if 'http://172.21.1.146:8180/xyjk-erp-app-pc/login' in request['url']:
            pass


if __name__ == '__main__':
    Framework = Framework()
    url = "http://172.21.1.146:8180/xyjk-erp-app-pc/login"
    Framework.run(Framework.load, url)
