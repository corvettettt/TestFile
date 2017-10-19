import requests
import urllib
import re
import random
from time import sleep

def main():
    url='https://www.zhihu.com/question/22591304/followers'
    headers={}
    i=1
    for x in xrange(20,3600,20):
       data={'start':'0',
             'offset':str(x),
             '_xsrf':'a128464ef225a69348cef94c38f4e428'}
       content= requests.post(url,headers=hearders,data=data, timeout=10).text
       imgs.re.findall('<img src=\\\\\"(.*?)_m.jpg',content)
       for img in imgs:
           try:
               img=img.replace('\\','')
               pic=img+'.jpg'
               path='/Users/zhixingwang/Scripts/pic'+str(i)+'.jpg'
               urllib.urlretrieve(pic,path)
               i+=1
               sleep(random.uniform(0.5,1))
           except:
               print 'miss one'
               pass
       sleep(random.uniform(0.5,1))
if __name__=='__main__':
    main()
