#!/usr/bin/env python3

from bs4 import BeautifulSoup as sop
import urllib.request as reqa
import re
global user_agent,headers
user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36'
headers = { 'User-Agent' : user_agent }
ipre = re.compile(r'(\d+\.\d+\.\d+\.\d+\?\d*)')
def getpage(url):
    req = reqa.Request(url,None, headers)
    res = reqa.urlopen(req)
    page = res.read()
    return page

def getcon(url):
    global headers
    li = []
    page = getpage(url)
    soup = sop(page,"html.parser")
    tds = soup('td')
    for content in tds:
        if content.a:
            txt = content.a.text
            if txt != '':
                li.append(txt)
    return li

def allips(lis):
    global headers
    ips = []
    for asn in lis:
        try:
            ipli = getcon('http://ipinfo.io/{0}'.format(asn))
            for ip in ipli:
                ip1 = ipre.findall(ip)[0]
                if ip1:
                    ips.append(ip1)
        except:
            pass
    return ips


def main():
    allasns = getcon('http://bgp.he.net/country/ID') + getcon('http://bgp.he.net/country/CN')
    ips = allips(allasns)
    with open('blacklist.txt', 'w') as bl:
        bl.write("\n".join(ips))

if __name__ == '__main__':
    main()


