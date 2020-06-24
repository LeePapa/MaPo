#coding:utf-8

"""
author  :linkin
date    :2020-06-24
"""

import re
import tornado.web
from tornado.web import url
from tools import check_params
from bs4 import BeautifulSoup as bs
from tornado.httpclient import AsyncHTTPClient

__all__ = ['Crawler','build_in_crawlers']

Headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36',
    'referer': 'https://f4.work/index.php',
    }

class Crawler:
    '''内置基类'''


class F4Crawler(Crawler):
    '''
    内置 https://f4.work/index.php 接码平台免费接码号码 采集爬虫及路由
    '''
    Server = '/F4'

    class PhonePatternHandler(tornado.web.RequestHandler):

        async def get(self,*args,**kwargs):
            params = check_params(self, 'pattern','phone','code','length')
            if not params:
                return
            pattern,phone,code,length = params
            url = 'https://f4.work/list_free.php?list=PHONELIST_1_1_{code}'.format(code=code)
            client = AsyncHTTPClient()
            ret = await  client.fetch(url,headers=Headers)
            html = ret.body.decode('utf-8')
            soup = bs(html,'lxml')
            rows = soup.findAll(attrs={'role':'button'})
            phones = {i.text.strip().split(' ')[-1].strip():'https://f4.work/'+i['href'] for i in rows }
            if phone in phones:
                href = phones[phone]
                response = await client.fetch(href)
                body = response.body.decode('utf-8')
                sp = bs(body,'lxml')
                div = sp('div',class_='col-xs-12 col-md-8')
                if div:
                    texts = {i.text.strip():i.previous_sibling.previous_sibling.text for i in div}
                    data = []
                    for i,ts in texts.items():
                        if pattern in i:
                            p = re.findall('\d+',i)
                            if not p:
                                continue
                            codes = [i for i in p if len(i)==int(length)]
                            if codes:
                                data.append({
                                    'text':i,
                                    'time':ts,
                                    'code':codes,
                                })
                    self.write({
                        'success':0,
                        'data':data,
                    })

    class PhoneSelectHandler(tornado.web.RequestHandler):

        async def get(self,*args,**kwargs):
            code = self.get_argument('code',None)
            home = 'https://f4.work/index.php'
            client = AsyncHTTPClient()
            response = await client.fetch(home,headers=Headers)
            html = response.body.decode('utf-8')
            soup = bs(html,'lxml')
            legend = soup('legend')
            _next = legend[0].next_sibling
            res = []
            for _ in range(10):
                if _next.name and _next.name != 'a':
                    break
                else:
                    if not _next.name:
                        continue
                    href = 'https://f4.work/'+_next['href']
                    pre = href.split('_')[-1]
                    if code and code != pre:
                        continue
                    else:
                        res.append({
                            'code':pre,
                            'url':href,
                            'area':_next.text
                        })
                    _next = _next.next_sibling.next_sibling
            for i in res:
                url = i['url']
                ret = await  client.fetch(url, headers=Headers)
                html = ret.body.decode('utf-8')
                soup = bs(html, 'lxml')
                rows = soup.findAll(attrs={'role': 'button'})
                phones = [i.text.strip().split(' ')[-1].strip() for i in rows]
                i.update({
                    'phones':phones
                })
            self.write({
                'success':0,
                'data':res
            })

    urls = [
        url(Server+'/fetch',PhonePatternHandler,name='f4_phone_code_fetch'),
        url(Server+'/phone',PhoneSelectHandler,name='f4_phone_query'),
    ]


build_in_crawlers = [F4Crawler,]