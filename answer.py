import os
import sys
import wda
from PIL import Image
import math
import time
import urllib.request,base64,json,os,time,baiduSearch
from aip import AipOcr


start = time.time()

height = 700
# 判断是否是最后一题，最后一题 自定义 高度
is_end = int(sys.argv[1])
if(is_end==1):
    height = 900
elif(is_end==0):
    height = 700



APP_ID = 'xxx'
API_KEY = 'xxx'
SECRET_KEY = 'xxx'
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

c = wda.Client()
s = c.session()
c.screenshot('screen.png')
im = Image.open(r"./screen.png")

img_size = im.size
w = im.size[0]
h = im.size[1]

# print("xx:{}".format(img_size))

region = im.crop((70,200, w-70,height))    #裁剪的区域
region.save(r"./keyword.png")


""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image = get_file_content(r"./keyword.png")
respon = client.basicGeneral(image)   #用完500次后可改respon = client.basicAccurate(image)
titles = respon['words_result']       #获取问题
answer = ['','','','','','']
ans = ''
countone = 0
answercount = 0
for title in titles:
    countone += 1
    if (countone >= len(titles) - 2):
        answer[answercount] = title['words']
        answercount += 1
    ans = ans +title['words']

tissue = ans[1:2]
if str.isdigit(tissue):            #去掉题目索引
     ans = ans[3:]
else:
     ans = ans[2:]


print('问题是：'+ ans)       #打印问题
print('  A:'+answer[0]+' B:'+answer[1]+' C:'+answer[2])       #打印答案

keyword = ans    #识别的问题文本

convey = 'n'

if convey == 'y' or convey == 'Y':
    results = baiduSearch.search(keyword, convey=True)
elif convey == 'n' or convey == 'N' or not convey:
    results = baiduSearch.search(keyword)
else:
    print('输入错误')
    exit(0)
count = 0

print  ('————————————答案 start —————————————')

for result in results:

    print ('——————————'+ str(count) +' ：——————————')

    print('{0}'.format(result.abstract))
    count = count + 1
    if(count == 2):
        break

print ('—————————— end ——————————')

end = time.time()
endstr = '耗费时间：'+str(end-start)+'秒'
print (endstr)







