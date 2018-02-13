'''
Created on 2018年2月1日

@author: admin
'''
import urllib3

url = "http://www.baidu.com"

response1 = urllib3.connection_from_url(url)
print(response1)
