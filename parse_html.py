
from bs4 import BeautifulSoup
import re
import selenium_get_html as sgh

def get_url(html):
    # Img = re.compile(r'img.*src="(.*?)"')
    arc = re.compile(r'<article.*>(.*)</arcitle>')
    soup = BeautifulSoup(html, "html.parser")
    data = []
    for item in soup.find_all('article'):
        item = str(item)
        txt_list = re.findall(arc, item)
        for t in txt_list:
            print(t)
            data.append(t)
    return data
    with open('results/tmp_1.html', 'w') as f:
        for i in data:
            f.write(i)

if __name__ == '__main__':
    tmp=[]
    tmp.append(get_url(sgh.get_html()))
