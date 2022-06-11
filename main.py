from flask import Flask,render_template
import csv

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/index')
def home():
    # return render_template("index.html")
    return index()

@app.route('/city')
def city():
    return render_template("city.html")

@app.route('/shanghai')
def shanghai():
    shanghai_list: list[list[str]] = []
    with open('上海.csv', 'r', encoding='utf-8') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            shanghai_list.append(row)
    return render_template("shanghai.html",shanghai_list=shanghai_list)

@app.route('/lijiang')
def lijiang():
    lijiang_list: list[list[str]] = []
    with open('丽江.csv', 'r', encoding='utf-8') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            lijiang_list.append(row)
    return render_template("lijiang.html", lijiang_list=lijiang_list)

@app.route('/beijing')
def beijing():
    beijing_list: list[list[str]] = []
    with open('北京.csv', 'r', encoding='utf-8') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            beijing_list.append(row)
    return render_template("beijing.html", beijing_list=beijing_list)

@app.route('/xiamen')
def xiamen():
    xiamen_list: list[list[str]] = []
    with open('厦门.csv', 'r', encoding='utf-8') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            xiamen_list.append(row)
    return render_template("xiamen.html", xiamen_list=xiamen_list)

@app.route('/chengdu')
def chengdu():
    chengdu_list: list[list[str]] = []
    with open('成都.csv', 'r', encoding='utf-8') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            chengdu_list.append(row)
    return render_template("chengdu.html", chengdu_list=chengdu_list)

@app.route('/hangzhou')
def hangzhou():
    hangzhou_list: list[list[str]] = []
    with open('杭州.csv', 'r', encoding='utf-8') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            hangzhou_list.append(row)
    return render_template("hangzhou.html", hangzhou_list=hangzhou_list)

@app.route('/wuhan')
def wuhan():
    wuhan_list: list[list[str]] = []
    with open('武汉.csv', 'r', encoding='utf-8') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            wuhan_list.append(row)
    return render_template("wuhan.html", wuhan_list=wuhan_list)

@app.route('/hainan')
def hainan():
    hainan_list: list[list[str]] = []
    with open('海南.csv', 'r', encoding='utf-8') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            hainan_list.append(row)
    return render_template("hainan.html", hainan_list=hainan_list)

@app.route('/xian')
def xian():
    xian_list: list[list[str]] = []
    with open('西安.csv', 'r', encoding='utf-8') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            xian_list.append(row)
    return render_template("xian.html", xian_list=xian_list)

@app.route('/guizhou')
def guizhou():
    guizhou_list: list[list[str]] = []
    with open('贵州.csv', 'r', encoding='utf-8') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            guizhou_list.append(row)
    return render_template("guizhou.html", guizhou_list=guizhou_list)

@app.route('/qingdao')
def qingdao():
    qingdao_list: list[list[str]] = []
    with open('青岛.csv', 'r', encoding='utf-8') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            qingdao_list.append(row)
    return render_template("qingdao.html", qingdao_list=qingdao_list)

@app.route('/xianggang')
def xianggang():
    xianggang_list: list[list[str]] = []
    with open('香港.csv', 'r', encoding='utf-8') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            xianggang_list.append(row)
    return render_template("xianggang.html", xianggang_list=xianggang_list)

@app.route('/hot')
def hot():
    return render_template("hot.html")

@app.route('/travel')
def travel():
    return render_template("travel.html")

@app.route('/map')
def map():
    return render_template("map.html")


if __name__ == '__main__':
    app.run()