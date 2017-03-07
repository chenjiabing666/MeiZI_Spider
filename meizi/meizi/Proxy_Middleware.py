#coding:utf-8
import random
import scrapy
import logging
#ip代理的设置
class proxMiddleware(object):
    # def __init__(self):
    #     # self.file=open('reviewed_ips','r')
    #     self.proxy_list=[]
    #     # lines = self.file.readlines()
    #     for line in lines:
    #         self.proxy_list.append(line.strip('\n'))
    #     print self.proxy_list
    proxy_list=['http://114.217.132.14:8998', 'http://106.46.136.49:808', 'http://171.122.97.20:80', 'http://106.46.136.83:808', 'http://61.178.221.228:8998', 'http://124.88.67.14:80', 'http://124.88.67.21:843', 'http://106.46.136.221:808', 'http://106.46.136.78:808', 'http://59.63.154.226:808', 'http://106.46.136.97:808', 'http://106.46.136.213:808', 'http://106.46.136.101:808', 'http://101.200.48.60:8118', 'http://222.187.227.40:10000', 'http://58.23.122.79:8118', 'http://183.32.88.141:808', 'http://139.213.135.81:80', 'http://106.46.136.231:808', 'http://106.46.136.192:808', 'http://123.157.146.116:8123', 'http://106.46.136.13:808', 'http://180.76.154.5:8888', 'http://106.46.136.210:808', 'http://110.73.10.21:8123', 'http://222.169.193.162:8099']

    def process_request(self, request, spider):  #必须实现的方法
        # self.get_list_ips()
        request.meta['proxy']=random.choice(self.proxy_list)   #设置代理

