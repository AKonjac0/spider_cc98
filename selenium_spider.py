import selenium_get_html as sgh
import time
import requests
import re
import os
from bs4 import BeautifulSoup




headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0'
                  '.5112.102 Safari/537.36 Edg/104.0.1293.63'
}


def get_url(html):
    Img = re.compile(r'<article.*>(.*?)</article>')
    soup = BeautifulSoup(html, "html.parser")
    data = []
    for item in soup.find_all('article'):
        item = str(item)

        pic_list = re.findall(Img, item)
        for t in pic_list:

            #print(t)
            data.append(t)
    return data

def Url():
    with open("results/tmp_1.html", 'r', encoding='utf-8') as f:
        html = f.read()
    # html = html.replace('\n',' ')
    # with open("tmp_1.html", 'w', encoding='utf-8') as f:
    #    f.write(html)
    Img = re.compile(r'<article.*%;">(.*)</article>')
    soup = BeautifulSoup(html, "html.parser")
    data = []
    for item in soup.find_all('article'):
        item = str(item)

        pic_list = re.findall(Img, item)
        for t in pic_list:
            print(t)
            data.append(t)
    return data
def save_pic(data, lim):
    cnt = 0
    for i in data:
        if not i.lower().startswith('https:'):
            i = 'https:' + i
        try:
            img = requests.get(i)
            byte = img.content
            with open("image{}.jpg".format(cnt), "wb") as f:
                f.write(byte)
            cnt += 1
            print("downloaded:{}".format(cnt))
        except requests.exceptions.InvalidURL:
            pass
        time.sleep(0.25)
        if cnt >= lim:
            break


def get_image(url_base, target_dir, pic_num):
    if not os.path.exists(target_dir):
        os.mkdir(target_dir)
    html = sgh.get_html(url_base)
    data = get_url(html)
    os.chdir(target_dir)
    print("target dir: "+str(os.getcwd()))
    save_pic(data, pic_num)


if __name__ == '__main__':
    url = r'https://www.cc98.org/topic/5754231'
    tmp=[]
    for i in range(1, 19):
        if i == 1:
            tmp.append(url)
        else:
            tmp.append(r'https://www.cc98.org/topic/5754231/{}'.format(i))
    cnt=0
    res=[]
    driver=sgh.init()
    for i in tmp:
        print(sgh.get_html(driver, i, cnt))
        cnt+=1
    # print(res)
    # Url()
