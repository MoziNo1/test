from selenium import webdriver
import time
import requests
from selenium.webdriver import ActionChains

url = 'https://v.qq.com/'
driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()
time.sleep(5)
login_picture = '/html/body/div[2]/div[1]/div[3]/div[5]/a'

driver.find_element_by_xpath(login_picture).click()
qq_login = '/html/body/div[45]/div[2]/div/div/div[2]/a[1]'
driver.find_element_by_xpath(qq_login).click()
# 切换到iframe登录
driver.switch_to.frame("_login_frame_quick_")
driver.switch_to.frame('ptlogin_iframe')
user_passwd_login = '//*[@id="switcher_plogin"]'
driver.find_element_by_xpath(user_passwd_login).click()
# 输入用户名密码
username_input = '//*[@id="u"]'
passwd_input = '//*[@id="p"]'
driver.find_element_by_xpath(username_input).send_keys('1144234520')
driver.find_element_by_xpath(passwd_input).send_keys('ZZH123*963.-+')
# 点击登录按钮
login_button = '//*[@id="login_button"]'
driver.find_element_by_xpath(login_button).click()
cookie = driver.get_cookies()
cookie_str = ''
for item_cookie in cookie:
    item_str = item_cookie["name"]+"="+item_cookie["value"]+"; "
    cookie_str += item_str
    # print(item_cookie)
print(cookie_str)
# 登陆成功标识
time.sleep(3)
driver.implicitly_wait(10)
login_success_picture = '//*[@id="mod_head_notice_trigger"]/img[1]'
qq_element = driver.find_element_by_xpath(login_success_picture)
ActionChains(driver).move_to_element(qq_element).perform()
time.sleep(1)
login_sucess = '//*[@id="mod_head_notice_pop"]/div/div[1]/a[1]'
text_name = driver.find_element_by_xpath(login_sucess).text
if text_name == '突突突':
    api_url = 'https://v.qq.com/biu/u/history/'
    headers = {
        "cookie": cookie_str,
        "User_Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
    }

    res = requests.get(url=api_url, headers=headers)

    response = res.content
    resp = str(response,encoding="utf-8")
    print(resp)