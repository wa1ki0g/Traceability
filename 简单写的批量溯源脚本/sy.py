##!/usr/bin/python3
# -*- coding: utf-8 -*-
 
'''
@Time    : 2021/4/19
@Author  : wa1ki0g
@FileName: sy.py
@Software: 瞎鸡儿写的垃圾代码
 
'''
import requests
import re
def api1():
  f=open('G:/python/工具/1.txt','r')
  for line in f:
    line = line.strip()
    url="https://site.ip138.com/"+str(line)+"/"
    headers={"User-Agent":'ua.random'}
    talk=requests.get(url,headers=headers)
    talk=talk.text
    result = re.findall(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b", talk)
    if result:
      print("您请求的ip:")
      print(result[0])
    else:
      print("re cannot find ip")
    re1=re.findall(r"<h3>(.+)</h3>",talk)
    print(re1)
    re2=re.findall(r'<li><span class="date">(.+)</a></li>',talk)
    #print(re2)
    for i in re2:
      i = re.sub("<[^>]*>","",i)
      str1 ="历史绑定域名:  "
      print(str1.strip())
      print(i.replace("<[^>]*>",""))
    print("---")
    
if __name__ == "__main__":
  api1()
