import requests
from bs4 import BeautifulSoup
import re
import time
import random
import threading
import logging
import urllib3

logging.captureWarnings(True)     # 忽略所有警告信息


print("Started!")
user_agent_list = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
    "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0",
    "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
]


def iv_main():
    proxies = {}
    requests.packages.urllib3.disable_warnings()
    # proxy_ip = random.choice(proxy_list)
    url = 'http://www.cnblogs.com/hgzero/p/13121587.html'
    for proxy_ip in proxy_list:
        headers2 = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'accept-encoding': 'gzip, deflate, sdch, br',
            'accept-language': 'zh-CN,zh;q=0.8',
            'cache-control': 'max-age=0',
            # 'cookie': '_ga=GA1.2.481591223.1595765116; UM_distinctid=173bd649d3a47a-0dafb3bcfdc025-c7d6957-1fa400-173bd649d3b285; CNZZDATA1274152299=1071527655-1596606076-https%253A%252F%252Fgithub.com%252F%7C1596606076; __gads=ID=06cd4712d894cbfd:T=1596696622:S=ALNI_MYH61_8JmmQ_9i7p8uX8WBvtar2dw; Hm_lvt_742e9bdb6e867044bb348deab863d79d=1597037706; _gid=GA1.2.658579279.1599494411',
            'referer': 'https://www.cnblogs.com/',
            'upgrade-insecure-requests': '1',
            'user-agent': random.choice(user_agent_list),
        }
        proxies['HTTP'] = proxy_ip
        # user_agent = random.choice(user_agent_list)
        try:
            r = requests.get(url, headers=headers2, proxies=proxies, verify=False)  # verify是否验证服务器的SSL证书
            print("[*]" + proxy_ip + "访问成功！")
        except:
            print("[-]" + proxy_ip + "访问失败！")


##获取代理ip
def Get_proxy_ip():
    global proxy_list
    proxy_list = []
    url = "https://www.kuaidaili.com/free/inha/"
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, sdch, br",
        "Accept-Language": "zh-CN,zh;q=0.8",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Cookie": "channelid=0; sid=1599552334691695; Hm_lvt_7ed65b1cc4b810e9fd37959c9bb51b31=1599552335; _ga=GA1.2.975238057.1599552335; _gid=GA1.2.2007254696.1599552335; _gat=1; Hm_lpvt_7ed65b1cc4b810e9fd37959c9bb51b31=1599554740",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0",
        "Referrer Policy": "no-referrer-when-downgrade",
    }
    for i in range(1, 10):
        url = url = "https://www.kuaidaili.com/free/inha/" + str(i)
        html = requests.get(url=url, headers=headers).content
        soup = BeautifulSoup(html, 'html.parser')
        ip_list = ''
        port_list = ''
        protocol_list = ''
        for ip in soup.find_all('td'):
            if "IP" in ip.get('data-title'):
                ip_list = ip.get_text()  ##获取ip
            if "PORT" in ip.get('data-title'):
                port_list = ip.get_text()  ##获取port
            if ip_list != '' and port_list != '':
                proxy = ip_list + ":" + port_list
                ip_list = ''
                port_list = ''
                proxy_list.append(proxy)
        iv_main()
        time.sleep(2)
        proxy_list = []


th = []
th_num = 10
for x in range(th_num):
    t = threading.Thread(target=Get_proxy_ip)
    th.append(t)
for x in range(th_num):
    th[x].start()
for x in range(th_num):
    th[x].join()
