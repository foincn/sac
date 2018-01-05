#

import requests
from bs4 import BeautifulSoup
import threading

url = 'http://www.gb688.cn/bzgk/gb/std_list_type?p.p1=1&p.p90=circulation_date&p.p91=desc'
s = requests.session()
s.keep_alive = False
r = s.get(url)
html = r.content
soup = BeautifulSoup(html, "html.parser")
source = soup.select('tbody > tr')


import requests
from bs4 import BeautifulSoup
import threading


def check_page(index):
    url = 'http://www.gb688.cn/bzgk/gb/std_list_type?p.p1=1&p.p%s=15&p.p90=circulation_date&p.p91=desc' % index
    s = requests.session()
    s.keep_alive = False
    r = None
    while r == None:
        try:
            r = s.get(url, timeout=10)
        except:
            pass
    print(r.status_code)
    html = r.content
    soup = BeautifulSoup(html, "html.parser")
    source = soup.select('tbody > tr')
    if len(source) > 13:
        print('Success %s !' % index)




li = list(range(100))
se = []

for i in range(200):
    threading.Thread(target=check_page, args=(i,)).start()


    
