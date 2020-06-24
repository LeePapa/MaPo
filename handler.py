#coding:utf-8

import custom
from inspect import isclass
from crawlers import Crawler,build_in_crawlers


class ApiServer:

    crawlers = [i() for k,i in custom.__dict__.items()
                if isclass(i) and issubclass(i,Crawler)
                and hasattr(i,'urls')] + [i() for i in build_in_crawlers]
    urls = [i for x in crawlers for i in x.urls]


