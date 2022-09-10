import requests
from selenium import webdriver
import time
import start

#item = input('请输入要进入的网站：' + str())
item = "https://www.baidu.com"
print('即将进入' + item)
if __name__ == '__main__':
    start.main(item)
