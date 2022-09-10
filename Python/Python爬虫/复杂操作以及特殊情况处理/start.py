import requests
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

def main(item):
    # 指定调用某个地方的chrome浏览器
    options = webdriver.ChromeOptions()
    # chrome浏览器的主程序位置
    location = r"D:\IT社团\Python学习\chrome-win\chrome.exe"
    # 在options增加读取位置
    options.binary_location = location
    driver = webdriver.Chrome("D:\IT社团\Python学习\chromedriver.exe", options = options)

    # 使用get方法打开一个网站
    driver.get(item)


    time.sleep(3)
    # 关闭webdriver
    driver.quit()
    pass
