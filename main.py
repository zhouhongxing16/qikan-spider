import requests  # 导入requests包
from bs4 import BeautifulSoup
import random
import pymysql

ua_list = [
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Mozilla/5.0 (Windows NT 6.1; rv2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
    "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
]
proxies = {
    "http": "http://10.10.1.10:3128",
    "https": "http://10.10.1.10:1080",
}
headers = {}
headers[
    'User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36"
headers[
    'Cookie'] = "Ecp_ClientId=3190920170002392767; cnkiUserKey=b9dc540b-c554-b44f-4a4f-c3f75deca8f6; Ecp_IpLoginFail=200331222.209.34.112; ASP.NET_SessionId=umiiz5hh0sy5jvac02znjoi3; SID_navi=1201610; _pk_ses=*"
user_agent = random.choice(ua_list)
ip_list = []
dataList = []
i = 0

# --获得代理IP列表
def get_ip_list(urlip, headers2):
    web_data = requests.get(urlip, headers=headers2)
    soup = BeautifulSoup(web_data.text, 'lxml')
    ips = soup.find_all('tr')
    ip_list = []

    for k in range(1, len(ips)):
        ip_info = ips[k]
        tds = ip_info.find_all('td')
        ip_list.append(tds[1].text + ':' + tds[2].text)

    return ip_list
# -从代理IP列表里面随机选择一个
def get_random_ip(ip_list):
    proxy_list = []
    for ip in ip_list:
        proxy_list.append('http://' + ip)
    proxy_ip = random.choice(proxy_list)
    proxies = {'http': proxy_ip}
    return proxies
#核心期刊
def GetCoreData(page):
    print('正在抓取第' + str(page) + '页数据')
    data = {'tag': 'A', 'code': '1', 'title': '核心期刊', 'Order': '1', 'Page': page, 'ShowType': '0'}
    url = 'http://yuanjian.cnki.net/cjfd/home/Result?tag=A&code=1'
    response = requests.post(url, data, headers)
    soup = BeautifulSoup(response.text, "html.parser")

    for child in soup.find_all(name='div', attrs={"class": "box-outer"}):
        obj = {}
        # count = count + 1
        item = child.find_all(name='div', attrs={"class": "pic"})[0]
        # print(item)
        obj['imgUrl'] = item.img['src']
        obj['title'] = item.a['title']
        obj['href'] = item.a['href']
        dataList.append(obj)
    page = page + 1
    if page == 68:
        print("结束")
        # test()
        getItemData('core')
    else:
        GetCoreData(page)
#sci
def GetSCIData(page):
    print('正在抓取sci第' + str(page) + '页数据')
    data = {'tag': 'A', 'code': '3', 'title': 'SCI期刊', 'Order': '1', 'Page': page, 'ShowType': '0'}
    url = 'http://yuanjian.cnki.net/cjfd/Home/CJfdList?tag=A&code=3'
    response = requests.post(url, data, headers)
    soup = BeautifulSoup(response.text, "html.parser")

    for child in soup.find_all(name='div', attrs={"class": "box-outer"}):
        obj = {}
        # count = count + 1
        item = child.find_all(name='div', attrs={"class": "pic"})[0]
        # print(item)
        obj['imgUrl'] = item.img['src']
        obj['title'] = item.a['title']
        obj['href'] = item.a['href']
        dataList.append(obj)
    page = page + 1
    if page == 7:
        print("结束")
        # test()
        getItemData('SCI')
    else:
        GetSCIData(page)
#cscd
def getCSCDData(page):
    print('正在抓取cscd第' + str(page) + '页数据')
    data = {'tag': 'A', 'code': '4', 'title': 'CSCD期刊', 'Order': '1', 'Page': page, 'ShowType': '0'}
    url='http://yuanjian.cnki.net/cjfd/Home/CJfdList?tag=A&code=4'
    response = requests.post(url, data, headers)
    soup = BeautifulSoup(response.text, "html.parser")

    for child in soup.find_all(name='div', attrs={"class": "box-outer"}):
        obj = {}
        # count = count + 1
        item = child.find_all(name='div', attrs={"class": "pic"})[0]
        # print(item)
        obj['imgUrl'] = item.img['src']
        obj['title'] = item.a['title']
        obj['href'] = item.a['href']
        dataList.append(obj)
    page = page + 1
    if page == 41:
        print("结束")
        # test()
        getItemData('CSCD')
    else:
        getCSCDData(page)
#cssci
def getCSSCIData(page):
    print('正在抓取CSSCI第' + str(page) + '页数据')
    data = {'tag': 'A', 'code': '9', 'title': 'CSSCI期刊', 'Order': '1', 'Page': page, 'ShowType': '0'}
    url='http://yuanjian.cnki.net/cjfd/Home/CJfdList?tag=A&code=9'
    response = requests.post(url, data, headers)
    soup = BeautifulSoup(response.text, "html.parser")

    for child in soup.find_all(name='div', attrs={"class": "box-outer"}):
        obj = {}
        # count = count + 1
        item = child.find_all(name='div', attrs={"class": "pic"})[0]
        # print(item)
        obj['imgUrl'] = item.img['src']
        obj['title'] = item.a['title']
        obj['href'] = item.a['href']
        dataList.append(obj)
    page = page + 1
    if page == 33:
        print("结束")
        # test()
        getItemData('CSSCI')
    else:
        getCSSCIData(page)
#根据期刊名称进行查询
def getDataByName(qikanList):
    index = 0;
    for item in qikanList:
        print('正在抓取' + str(item[3]) + 'の数据')
        data = {'SearchType': '0', 'Name': item[3], 'Issn': '', 'Cn': '', 'Unit': '', 'PublicAddress': '', 'Order': '1'}
        url='http://yuanjian.cnki.net/cjfd/Home/Result'
        response = requests.post(url, data, headers)
        soup = BeautifulSoup(response.text, "html.parser")
        childList = soup.find_all(name='div', attrs={"class": "box-outer"})
        if len(childList)>0:
            child = soup.find_all(name='div', attrs={"class": "box-outer"})[0]
            obj = {}
            # count = count + 1
            o = child.find_all(name='div', attrs={"class": "pic"})[0]
            print(item)
            obj['id']=item[0]
            obj['code']=item[1]
            obj['imgUrl'] = o.img['src']
            obj['title'] = o.a['title']
            obj['href'] = o.a['href']
            dataList.append(obj)
            # for child in soup.find_all(name='div', attrs={"class": "box-outer"}):
            #     obj = {}
            #     # count = count + 1
            #     o = child.find_all(name='div', attrs={"class": "pic"})[0]
            #     print(item)
            #     obj['id']=item[0]
            #     obj['code']=item[1]
            #     obj['imgUrl'] = o.img['src']
            #     obj['title'] = o.a['title']
            #     obj['href'] = o.a['href']
            #     dataList.append(obj)

        else :
            print('-----------'+str(item[0])+item[3]+'未查询到')
        index = index + 1
    if index == len(qikanList):
        print(dataList)
        print("结束")
        # test()
        getItemData('core')
def getItemData(type):
     i =0
     print(dataList)
     for item in dataList:
        d = {}
        itemUrl  = item['href']
        # itemUrl = 'http://yuanjian.cnki.net/CJFD/Detail/Index/ALBJ'
        i = i + 1
        response = requests.post(itemUrl, {}, headers)
        bsoup = BeautifulSoup(response.text, "html.parser")
        child = bsoup.find_all(name='div', attrs={"class": "r-line"})
        unit = child[0].find(name='span',attrs={"class":"line-left left"}).contents[1]
        print("正在解析第"+str(i)+"条数据:"+item['title'])
        item['unit']=unit
        if child[0].find(name='span', attrs={"class": "line-right right"}) != None:
            issn = child[0].find(name='span',attrs={"class":"line-right right"}).contents[1]
            item['ISSN']=issn
        else:
            item['ISSN'] = ''
        if child[1].find(name='span', attrs={"class": "line-right right"}) != None:
            cn = child[1].find(name='span',attrs={"class":"line-right right"}).contents[1]
            item['CN']=cn
        else:
            item['CN'] = ''
     updateData(type)
     # saveData(type)
    # if len(child[0].find_all(name='span')[1].contents)>0:
    #     print('ISSN'+child.find_all(name='span')[1].contents[1])
    # else:
    #     print(child.find_all(name='span')[1].contents[0])
def getQiKanDataFromDataBase(num):
    db = pymysql.connect(host='127.0.0.1', user='root', password='root', db='python_test', port=3306, charset='utf8')
    print('连接数据库成功！')
    print('查询从！'+str(num)+"开始")
    conn = db.cursor()  # 获取指针以操作数据库
    conn.execute('set names utf8')
    # sql = "select a.* from qikan_core_temp a where id='297'"
    # sql = "select a.* from   qikan_core_temp a where status='0' limit "+str(num)+",10"
    sql = "SELECT * FROM qikan_core_temp  WHERE TYPE IS NULL limit "+str(num)+",10"
    conn.execute(sql)
    qikanList = conn.fetchall()
    db.commit()  # 提交操作
    print('数据查询成功!')
    # 关闭MySQL连接
    conn.close()
    db.close()

    getDataByName(qikanList)

def updateData(type):
    # 连接MYSQL数据库
    db = pymysql.connect(host='127.0.0.1', user='root', password='root', db='python_test', port=3306, charset='utf8')
    print('连接数据库成功！')
    conn = db.cursor()  # 获取指针以操作数据库
    conn.execute('set names utf8')
    # sql = "INSERT INTO qikan(title,href,img_url) VALUES('dceshi','href','http')"
    # conn.execute(sql)
    for item in dataList:
        title = item['title']
        unit = item['unit']
        imgUrl = item['imgUrl']
        href = item['href']
        CN = item['CN']
        ISSN = item['ISSN']
        id = item['id']
        # 写入MYSQL数据库
        # sql = "update  qikan set type=type,unit="+unit+",img_url=imgUrl,ISSN=ISSN,CN=CN where id = id"
        sql = "update  qikan_core_temp set type="+"'"+type+"'"+",unit="+"'"+unit+"'"+",href="+"'"+href+"'"+",img_url="+"'"+imgUrl+"'"+",ISSN="+"'"+ISSN+"'"+",CN="+"'"+CN+"'"+" ,status="'1'" where id = "+str(id)+""
        print('sql:'+sql)
        # sql = "INSERT INTO qikan(title,href,img_url) VALUES(%s,%s,%s)"
        conn.execute(sql)
    db.commit()  # 提交操作
    print('插入数据成功!')

    # 关闭MySQL连接
    conn.close()
    db.close()

def saveData(type):
    # 连接MYSQL数据库
    db = pymysql.connect(host='127.0.0.1', user='root', password='root', db='python_test', port=3306, charset='utf8')
    print('连接数据库成功！')
    conn = db.cursor()  # 获取指针以操作数据库
    conn.execute('set names utf8')
    # sql = "INSERT INTO qikan(title,href,img_url) VALUES('dceshi','href','http')"
    # conn.execute(sql)
    for item in dataList:
        # 写入MYSQL数据库
        sql = "INSERT INTO qikan(type,title,href,img_url,unit,CN,ISSN) VALUES("+"'"+type+"'"+","+"'"+item['title']+"'"+","+"'"+item['href']+"'"+","+"'"+item['imgUrl']+"'"+","+"'"+item['unit']+"'"+","+"'"+item['CN']+"'"+","+"'"+item['ISSN']+"'"+")"
        print(sql)
        # sql = "INSERT INTO qikan(title,href,img_url) VALUES(%s,%s,%s)"
        conn.execute(sql)
    db.commit()  # 提交操作
    print('插入数据成功!')

    # 关闭MySQL连接
    conn.close()
    db.close()

#期刊爬虫
if (__name__ == "__main__"):
    ## 得到一个代理 IP
    #urlip = 'http://www.xicidaili.com/nt/'  # 提供代理IP的网站
    #ip_list = get_ip_list(urlip, headers)  # 获得代理IP列表
    i = 0
    for i in range(i,50,10):
        dataList=[]
        print("正在抓取第"+str(i)+"☞"+str(i+10)+"条数据")
        getQiKanDataFromDataBase(i)
    # getCSSCIData(1)
    # GetSCIData(1)
     # getItemData()
    # print('共找到' + str(len(dataList)) + '条数据')
