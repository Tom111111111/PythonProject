import requests #帮助模拟发送http请求模块
from bs4 import BeautifulSoup #解析数据
import pandas as pd


filename = "上海.csv" #将爬取下来的信息存入filename这个文件里

#url是请求地址
url = "https://travel.qunar.com/travelbook/list/%25E4%25B8%258A%25E6%25B5%25B7/hot_heat/1.htm" #首先进入去哪儿网，选择攻略、攻略库，并搜索目的地址，进入后可以通过复制网址得到url，也可以通过检查--网络--标头--请求url获得

#请求头
headers = { #在标头找到user-agent
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.53'
    }

#发起网络请求
r = requests.get(url,headers=headers) #r是一个Response对象，从这个对象中获取所有想要的信息
r.encoding = "utf-8" #在控制台里输入document.charset，可以看到这个网页的编码格式是utf-8
html = r.text #r.text读取服务器响应的内容，将它存入html

#计算总页数
# pageNum = 0
bs = BeautifulSoup(html,"html.parser") #建立一个BeautifulSoup对象bs,用html.parser这个解析器解析html，形成树形结构
#把找到的结果存入strategyPageList列表
strategyPageList = bs.find("div",attrs = {"class":"b_paging"}).find_all("a") #查找所有a标签（超链接） find_all("a")字符串过滤--查找与字符串完全匹配的内容   find(name,attrs,recursive,string,**kwargs )
if(strategyPageList):
    pageNum = strategyPageList[-2].text
    pageNum = int(pageNum) + 1 #从1开始


#爬取每一页的数据
for i in range(1,pageNum):
    print("正在爬取",str(i),"页........")
    url = "https://travel.qunar.com/travelbook/list/%25E4%25B8%258A%25E6%25B5%25B7/hot_heat/" + str(i) + ".htm"
    bs = BeautifulSoup(html, "html.parser")
    strategyList = bs.find("ul", attrs={"class": "b_strategy_list"})
    for strategy in strategyList:
        link = "https://travel.qunar.com" + strategy.h2.a["href"]
        print("link:", link)
        title = strategy.h2.a.text
        print("title:", title)
        user_info = strategy.find("p", attrs={"class": "user_info"})

        intro = user_info.find("span", attrs={"class": "intro"})
        user_name = intro.find("span", attrs={"class": "user_name"}).text
        print("user_name:", user_name)
        date = intro.find("span", attrs={"class": "date"}).text
        print("date:", date)
        days = intro.find("span", attrs={"class": "days"}).text
        print("days:", days)

        photoTmp = intro.find("span", attrs={"class": "photo_nums"})
        if (photoTmp):
            photo_nums = photoTmp.text
        else:
            photo_nums = "没有照片"
        print("photo_nums:", photo_nums)

        peopleTmp = intro.find("span", attrs={"class": "people"})
        if (peopleTmp):
            people = peopleTmp.text
        else:
            people = ""
        print("people:", people)

        tripTmp = intro.find("span", attrs={"class": "trip"})
        if (tripTmp):
            trip = tripTmp.text
        else:
            trip = ""
        print("trip:", trip)

        feeTmp = intro.find("span", attrs={"class": "fee"})
        if (feeTmp):
            fee = feeTmp.text
        else:
            fee = ""
        print("fee:", fee)

        nums = user_info.find("span", attrs={"class": "nums"})
        icon_view = nums.find("span", attrs={"class": "icon_view"}).span.text
        print("icon_view:", icon_view)
        icon_love = nums.find("span", attrs={"class": "icon_love"}).span.text
        print("icon_love:", icon_love)
        icon_comment = nums.find("span", attrs={"class": "icon_comment"}).span.text
        print("icon_comment:", icon_comment)

        print("------" * 20)
        spotStrategy = [
            [title, link, user_name, date, days, photo_nums, people, trip, fee, icon_view, icon_love, icon_comment]]

        dataframe = pd.DataFrame(spotStrategy) #DataFrame数据类型一个表格
        dataframe.to_csv(filename, encoding='utf_8_sig', mode='a', index=False, sep=",", header=False)