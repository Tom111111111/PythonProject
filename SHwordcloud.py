import imageio
import wordcloud
import jieba
jieba.setLogLevel(jieba.logging.INFO)
import csv

shanghai_list: list[list[str]] = []
with open('上海.csv', 'r', encoding='utf_8_sig') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        shanghai_list.append(row[0])


with open('shanghai.txt', 'w', encoding='utf_8_sig') as f1:
    for i in range(len(shanghai_list)):
        f1.write(str(shanghai_list[i]))



txt = open("shanghai.txt", 'r', encoding = "utf_8_sig").read()

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




# import PIL.Image as Image
# # 如果当前位深是32的话，可以不用写转RGBA模式的这一句，但是写上也没啥问题
# # 从RGB（24位）模式转成RGBA（32位）模式
# img = Image.open('wordcloudbackground.png').convert('RGBA')
# W, L = img.size
# white_pixel = (0, 0, 0, 0)  # 白色
# for h in range(W):
#   for i in range(L):
#     if img.getpixel((h, i)) == white_pixel:
#       img.putpixel((h, i), (255, 255, 255, 0))   # 设置透明
# img.save('wordcloud.png')  # 自己设置保存地址


img = imageio.imread('wordcloud.png')
wc = wordcloud.WordCloud(
    background_color='white',
    mask=img,
    font_path="C:\Windows\Fonts\方正粗黑宋简体.ttf"
).generate(text)

wc.to_file("shanghaiwordcloud.jpg")