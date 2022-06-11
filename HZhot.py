import requests
from bs4 import BeautifulSoup
import pandas as pd

# 获取连接网页数据
url_lst=[]
i=0
for i in range(2):
    url_lst='https://travel.qunar.com/p-cs300195-hangzhou-jingdian-1-' + str(i + 1)
    r = requests.get(url_lst)
    soupi = BeautifulSoup(r.text, 'lxml')
    info = soupi.find('ul', class_="list_item clrfix").find_all('li')

    datai = []
    n = 0
    for i in info:
        n += 1
        dic = {}
        dic['景点名称'] = i.find('span', class_="cn_tit").text
        dic['点评数量'] = i.find('div', class_="comment_sum").text
        datai.append(dic)  # 列表包字典
        # 分别获取字段内容
        print('已采集%s条数据' % (n * 10))

        df = pd.DataFrame()
        for u in url_lst:
            dfi = pd.DataFrame(datai)
            df = pd.concat([df, dfi])  # 将多个df拼接在一起
            df.reset_index(inplace=True, drop=True) #inplace=True,drop=True将原来的行索引列舍弃，生成一个新df

filename = "hangzhou.csv"
df.to_csv(filename,encoding='utf_8_sig',mode='a',index=False,sep=",",header=False)