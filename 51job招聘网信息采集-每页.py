import requests
from lxml import etree
import re

url = "https://search.51job.com/list/000000,000000,0000,00,9,99,python,2,1.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=4&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="

content = requests.get(url)
content.encoding=content.apparent_encoding
content = content.text
root = etree.HTML(content)

name = root.xpath("//p/span/a/@title")    #职位名称
g_name = root.xpath("//div[@class='dw_table']/div/span/a/@title")     #公司名称
adds = root.xpath("//div[@class='el']/span[@class='t3']/text()")    #职位名称
salaries = root.xpath("//div[@class='el']/span[@class='t4']/text()")     #薪资
datas = root.xpath("//div[@class='el']/span[@class='t5']/text()")       #发布时间
# print(name)
# print(g_name)
# print(adds)
# print(salaries)
# print(datas)



for job, company, location, salary, data in zip(name, g_name, adds, salaries, datas):    # 循环单个拿出
    # print(job, company, location, salary, data)

    # 存储表格
    f = open("movie2.csv", "w", encoding="utf-8")
    f.write(job + ',' + company + ',' + location + ',' + str(salary) + ',' + str(data) + "\n")
    f.flush()  # 将缓冲区的内容立即写入文件并清空缓冲区   = 保存
    f.close()


