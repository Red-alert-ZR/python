import requests
from selenium import webdriver
import time

def main(item):
    # 指定调用某个地方的chrome浏览器
    options = webdriver.ChromeOptions()
    # chrome浏览器的主程序位置
    location = r"D:\IT社团\Python学习\chrome-win\chrome.exe"
    # 在options增加读取位置
    options.binary_location = location
    # 使用静默模式（不跳出浏览器还去操作）
    # options.add_argument("headless")
    driver = webdriver.Chrome("D:\IT社团\Python学习\chromedriver.exe", options = options)

    # 使用get方法打开一个网站
    driver.get(item)

    # 获取当前页面的地址（尚未切换标签）
    print(driver.current_url)
    # 获取当前页面的源码
    print(driver.page_source)
    # 获取当前页面的cookie
    print(driver.get_cookies())
    # 过了两秒
    time.sleep(2)
    #　刷新页面
    driver.refresh()

    # 加代理http, https, sock4, sock5
    options.add_argument("--proxy-server=%s" % 'sock4://1.2.3.4:54321')
    #　更改浏览器语言
    options.add_argument('--lang=end-US')
    # 翻页
    driver.find_element_by_xpath("//input[@id='kw']").send_keys('美国')
    driver.find_element_by_xpath("//input[@id='su']").click()
    time.sleep(1)
    driver.find_element_by_xpath("//a[@class='n']").click()

for page in range(12):
    print('现在是第%s页' % page)
    time.sleep(1)
    res = driver.find_elements_by_xpath("//div[@class='c-container']//a/em")
    for i in range(len(res)):
        print(res[i].text)

    # 点到下一页
    time.sleep(1)
    driver.find_element_by_xpath("//a[@class='n'][2]").click()

    # 获取目标元素的html代码
    html = driver.find_element_by_xpath("//input[@id='kw']").get_attribute("outerHTML")
    print(html)
    # 获取百度一下的位置,发现一个是link的，文字是text的element
    baidu = driver.find_element_by_link_text('百度一下')
    # 鼠标悬停
    ActionChains(driver).move_to_element(baidu).perform()










    # 组合键输入
    driver.find_element_by_xpath(
        "//div[@id='head']/div[@id='head_wrapper']//input[@id='kw']").send_keys(Keys.CONTROL,'a')
    # 根据id找到对应的目标，并输入对应的内容
    driver.find_element_by_id('kw').send_keys("白紫剑")
    # 找到按钮
    driver.find_element_by_xpath(
        "/html/body/div[@id='wrapper']/div[@id='head']/div[@id='head_wrapper']/div[@class='s_form s_form_nologin']/div[@class='s_form_wrapper soutu-env-nomac soutu-env-index']/form[@id='form']/span[@class='bg s_btn_wr']/input[@id='su']").click()
    # 打印文本
    ret = driver.find_element_by_xpath(
        "//div[@class='s_form s_form_nologin']//li[@class='hotsearch-item odd'][2]//span[@class='title-content-title']").text
    print(ret)
    # 移动鼠标位置
    action = ActionChains(driver).move_by_offset(400, 350).click()
    # 开始执行
    action.perform()
    # 鼠标移动回原点
    ActionChains(driver).move_by_offset(-400, 120).perform()












    # 移动鼠标位置
    action = ActionChains(driver).move_by_offset(400, 350).click()
    # 开始执行
    action.perform()
    # 鼠标移动回原点
    ActionChains(driver).move_by_offset(-400, 120).perform()

    a = ActionChains(driver).move_by_offset(200, 480).click()
    a.perform()
    ActionChains(driver).move_by_offset(-200, 480).perform()

    time.sleep(5)
    # 关闭webdriver
    driver.quit()
    pass
