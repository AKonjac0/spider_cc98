from selenium import webdriver
import time

def Get_html(url_base):
    #option = webdriver.ChromeOptions()
    #option.add_experimental_option("detach", True)
    # 将option作为参数添加到Edge中
    #driver = webdriver.Chrome(chrome_options=option)
    driver = webdriver.Edge()
    cnt=0
    for i in url_base:

        print(i)
        driver.get(i)
        if cnt==0:
            time.sleep(30)
        else:
            time.sleep(1)
        cnt+=1
        driver.encoding = 'UTF-8'
        print(driver.page_source)
    '''for i in range(0, 60):
        # 控制网页向下滚动1000像素值
        driver.execute_script("window.scrollBy(0,1000)")
        time.sleep(1)'''
    driver.encoding = 'UTF-8'
    #with open('tmp.html', 'w') as f:
    #    f.write(driver.page_source)
    # print(driver.page_source)
    return driver.page_source


def init():
    driver = webdriver.Edge()
    return driver
def get_html(driver, url_base, cnt):
    driver.get(url_base)
    if cnt==0:
        time.sleep(30)
    else:
        time.sleep(1)
    driver.encoding = 'UTF-8'
    return driver.page_source
