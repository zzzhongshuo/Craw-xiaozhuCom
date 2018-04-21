import requests
from bs4 import BeautifulSoup
import time
ALLInformation=[]
headers={'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
def GetAllHtml():#获取所有页面的URL
    Html=[]
    for i in range(1,14):
        Html.append('http://bj.xiaozhu.com/search-duanzufang-p{}-0/'.format(i))
    return Html
def GetSoup(html):#获取网页文档
    try:
        r = requests.get(html,timeout=30,headers=headers)
        time.sleep(2)
        r.raise_for_status()#若连接网页错误则抛出异常
        r.encoding='utf-8'
        soup=BeautifulSoup(r.text,'lxml')
        return soup
    except:
        print("获取错误!")
        return ''
def GetUrl(soup):#获取每个页面所包含的URL
    Url=[]
    links=soup.select('#page_list > ul > li > a')
    for link in links:
        url=link.get('href')
        Url.append(url)
    return Url
def Craw(soup):#爬取信息
    information=[]
    information.append(soup.select('body > div.wrap.clearfix.con_bg > div.con_l > div.pho_info > h4 > em').get_text())#标题
    information.append(soup.select('body > div.wrap.clearfix.con_bg > div.con_l > div.pho_info > p').get_text())#地址
    information.append(soup.select("#floatRightBox > div.js_box.clearfix > div.w_240 > h6 > a").get_text())#用户名
    information.append(soup.select('#introduce > li.border_none > p').get_text())#位置和面积
    information.append(soup.select('#pricePart > div.day_l > span').get_text())#价格
    return information
def main():
    Html=GetAllHtml()
    for i in range(13):
        Soup=GetSoup(Html[i])
        for Url in GetUrl(Soup):
            soup=GetSoup(Url)
            ALLInformation.append(Craw(soup))
    print(ALLInformation)
main()