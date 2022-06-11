import requests #发送请求模块
from bs4 import BeautifulSoup
import pandas as pd


filename = "杭州.csv"

url = "https://travel.qunar.com/travelbook/list/%25E6%259D%25AD%25E5%25B7%259E/hot_heat/1.htm"

headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.53'
    }
#发起网络请求
r = requests.get(url,headers=headers)
r.encoding = "utf-8"
html = r.text

# pageNum = 0
bs = BeautifulSoup(html,"html.parser")
strategyPageList = bs.find("div",attrs = {"class":"b_paging"}).find_all("a")
if(strategyPageList):
    pageNum = strategyPageList[-2].text
    pageNum = int(pageNum) + 1


for i in range(1,pageNum):
    print("正在爬取",str(i),"页........")
    url = "https://travel.qunar.com/travelbook/list/%25E6%259D%25AD%25E5%25B7%259E/hot_heat/" + str(i) + ".htm"
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

        dataframe = pd.DataFrame(spotStrategy)
        dataframe.to_csv(filename, encoding='utf_8_sig', mode='a', index=False, sep=",", header=False)