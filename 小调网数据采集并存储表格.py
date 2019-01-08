import requests
from lxml import etree
import re

url = "https://www.dy2018.com/html/gndy/dyzz/index.html"
content = requests.get(url).text
root = etree.HTML(content)
pages = root.xpath("//select/option/@value")

f = open("movie.csv", "w")
num = 1

for page in pages:
    url = "https://www.dy2018.com" + page
    content = requests.get(url)
    content.encoding = content.apparent_encoding
    content = content.text
    root = etree.HTML(content)
    movie_titles = root.xpath("//b/a/@title")
    movie_hrefs = root.xpath("//b/a/@href")
    for movie_title, movie_href in zip(movie_titles, movie_hrefs):
        # 正则表达式
        pattern = re.compile(r"《(.*?)》")     #标题只保留尖括号里面的
        if "《" in movie_title and "》" in movie_title:  #有不一样的存在
            movie_title = pattern.findall(movie_title)[0]

        movie_href = "https://www.dy2018.com" + movie_href
        content = requests.get(movie_href)
        content.encoding = content.apparent_encoding
        content = content.text
        if content:
            root = etree.HTML(content)
            download_url = root.xpath("//td[@bgcolor='#fdfddf']/a/text()")

            if download_url:
                download_url = download_url[0]      #避免为空

                print(movie_title, download_url)
                f.write(str(num) + ',' + movie_title + ',' + download_url + '\n')
                f.flush()  # 将缓冲区的内容立即写入文件并清空缓冲区   = 保存
                num += 1
f.close()
#  也可以采用多线程