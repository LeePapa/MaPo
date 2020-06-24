#coding:utf-8

'''
自定义模块
自己编写 接码平台采集爬虫及路由，所有自定义采集爬虫需要继承自基类 Crawler
'''

from crawlers import Crawler
from tornado.web import url

class MyCrawler(Crawler):
    '''
    自定义的接码平台号码爬虫 及路由
    '''
    urls = []






