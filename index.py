#coding:utf-8

'''
启动模块，无需改动，除非增加数据库支持等
'''

import logging
import tornado.log
import tornado.ioloop
import tornado.options
from handler import ApiServer
from config import PORT
from tornado.web import Application

SETTINGS = {
    'autoreload':True,
}

class LogFormatter(tornado.log.LogFormatter):
    def __init__(self):
        super(LogFormatter, self).__init__(
            fmt='%(color)s[%(asctime)s %(filename)s:%(funcName)s:%(lineno)d %(levelname)s]%(end_color)s %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S',
        )

def main():
    tornado.options.parse_command_line()
    app = Application(ApiServer.urls,**SETTINGS)
    [i.setFormatter(LogFormatter()) for i in logging.getLogger().handlers]
    app.listen(PORT,xheaders=True)
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()