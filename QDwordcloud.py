import imageio
import wordcloud
import jieba
jieba.setLogLevel(jieba.logging.INFO)
import csv

qingdao_list: list[list[str]] = []
with open('青岛.csv', 'r', encoding='utf_8_sig') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        qingdao_list.append(row[0])


with open('qingdao.txt', 'w', encoding='utf_8_sig') as f1:
    for i in range(len(qingdao_list)):
        f1.write(str(qingdao_list[i]))



txt = open("qingdao.txt", 'r', encoding = "utf_8_sig").read()

words = jieba.lcut(txt)
text = " "
counts = {}

for word in words:
    text +=  word
    if len(word) == 1:
        continue
    else:
        counts[word] = counts.get(word, 0) + 1

text=" "
items = list(counts.items())
items.sort(key = lambda x:x[1], reverse = True)
for i in range(50):
    word, count = items[i]
    print("{0}:{1}".format(word, count))
    text += ' '+word



img = imageio.imread('wordcloud.png')
wc = wordcloud.WordCloud(
    background_color='white',
    mask=img,
    font_path="C:\Windows\Fonts\方正粗黑宋简体.ttf"
).generate(text)

wc.to_file("qingdaowordcloud.jpg")