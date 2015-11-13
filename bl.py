#!/usr/bin/env python3

from bs4 import BeautifulSoup as sop
import urllib.request as reqa

global user_agent,headers
user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36'
headers = { 'User-Agent' : user_agent }

def getpage(url):
    req = requa.Request(url,None, headers)
    res = requa.urlopen(req)
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
        ipli = getcon('http://ipinfo.io/{0}'.format(ipli))
        for ip in ipli:
            ips.append(ip)
    return ips


def main():
    allasns = getcon('http://http://bgp.he.net/country/ID') + getcon('http://http://bgp.he.net/country/CN')
    ips = allips(allans)
    with open('blacklist.txt') as bl:
        bl.write("\n".join(ips))

if __name__ == '__main__':
    main()


