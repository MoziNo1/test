from selenium import webdriver
import time
url = 'http://172.21.12.57/webroot/decision/login'

dr = webdriver.Chrome()
for i in range(1,10):
    dr.get(url)
    user_input = dr.find_element_by_xpath('//*[@id="wrapper"]/div[1]/div/div[2]/div/div/div[1]/div[1]/div[1]/div[1]/div[2]/input')
    user_input.send_keys(i)
    password = dr.find_element_by_xpath('//*[@id="wrapper"]/div[1]/div/div[2]/div/div/div[1]/div[2]/div[1]/div[1]/div[2]/input')
    password.send_keys(i)
    login_button = dr.find_element_by_xpath('//*[@id="wrapper"]/div[1]/div/div[2]/div/div/div[1]/div[4]/div/div[1]')
    login_button.click()
    time.sleep(2)
dr.quit()


