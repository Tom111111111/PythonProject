import imageio
import wordcloud
import jieba
jieba.setLogLevel(jieba.logging.INFO)
import csv

chengdu_list: list[list[str]] = []
with open('成都.csv', 'r', encoding='utf_8_sig') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        chengdu_list.append(row[0])


with open('chengdu.txt', 'w', encoding='utf_8_sig') as f1:
    for i in range(len(chengdu_list)):
        f1.write(str(chengdu_list[i]))



txt = open("chengdu.txt", 'r', encoding = "utf_8_sig").read()

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

wc.to_file("chengduwordcloud.jpg")