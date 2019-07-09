# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html
import logging
import random
import time
import os
from scrapy import signals
from scrapy.downloadermiddlewares.retry import RetryMiddleware
from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware

from scrapy.utils.response import response_status_message

IPPOOL =['https://139.129.207.72:808','http://218.17.21.138:808','http://61.176.223.7:58822','https://210.5.10.87:53281','https://111.198.104.169:808','http://112.85.166.229:9999','http://123.146.236.34:53281','http://123.146.236.34:53281','http://218.17.21.138:808','https://111.198.104.169:808','https://139.129.207.72:808',]
IPDont = set()

class BossScrapySpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
class CookiesMiddleware(object):
    Cookies = [
        'callbackUrl="http://www.zhipin.com/c101010100-p100199/?ka=search_100199"; verifyIp=IfRE9G6oRHcIW3Q2PQ~~; verifyUserId=IA~~; lastCity=101010100; _uab_collina=155257470081104788858221; __c=1554113061; __g=-; __l=l=%2Fwww.zhipin.com%2Fc100010000%2F%3Fquery%3D%25E5%2590%258E%25E7%25AB%25AF%25E5%25BC%2580%25E5%258F%2591%26page%3D10%26ka%3Dpage-10&r=; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1553955445,1553957870,1554040675,1554113061; JSESSIONID=""; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1554115168; __a=97970414.1552574698.1554040675.1554113061.110.7.17.110',
        'lastCity=101010100; _uab_collina=155257470081104788858221; __c=1554113061; __g=-; __l=l=%2Fwww.zhipin.com%2Fc100010000%2F%3Fquery%3D%25E5%2590%258E%25E7%25AB%25AF%25E5%25BC%2580%25E5%258F%2591%26page%3D10%26ka%3Dpage-10&r=; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1553955445,1553957870,1554040675,1554113061; JSESSIONID=""; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1554115255; __a=97970414.1552574698.1554040675.1554113061.111.7.18.111',
        'lastCity=101010100; _uab_collina=155257470081104788858221; __c=1554113061; __g=-; __l=l=%2Fwww.zhipin.com%2Fc100010000%2F%3Fquery%3D%25E5%2590%258E%25E7%25AB%25AF%25E5%25BC%2580%25E5%258F%2591%26page%3D10%26ka%3Dpage-10&r=; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1553955445,1553957870,1554040675,1554113061; JSESSIONID=""; __a=97970414.1552574698.1554040675.1554113061.114.7.21.114; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1554115847',
    ]

    def process_request(self, request, spider):
        cookie = random.choice(self.Cookies)
        # print("this is cookie:" + cookie)
        request.headers['cookie'] = cookie


class MyUserAgentMiddleware(UserAgentMiddleware):

    USER_AGENTS = [
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36",
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.54 Safari/536.5',
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
    ]
    def process_request(self, request, spider):
        user_agent = random.choice(self.USER_AGENTS)
        # print("this is user-agent:" + user_agent)
        request.headers['User-Agent'] = user_agent

FLAG = 0
ip_list = set()
class IPProxyMiddleware(object):
    global IPPOOL,ip_list
    pool = IPPOOL
    def process_request(self, request, spider):
        '''对request对象加上proxy'''
        if  request.meta['proxy']=="":
            proxy = self.get_random_proxy()
            print("this is request ip:" + proxy)
            request.meta['proxy'] = proxy
        else:
            print("this is origin_request ip:" + request.meta['proxy'])

    # 对返回的response处理
    def process_response(self, request, response, spider):
        # 如果返回的response状态不是200，重新生成当前request对象
        if response.status == 200:
            self.write_txt(request.meta['proxy'])
        if response.status != 200:
            proxy = self.get_random_proxy()
            print("IP更换后为:" + proxy)
            # 对当前request加上代理
            request.meta['proxy'] = proxy
            return request
        return response

    def get_random_proxy(self):
        '''随机从文件中读取proxy'''
        if self.pool:
            proxy = self.pool.pop()
        else:
            with open('C:\\Users\\yue_luo\\Desktop\\Boss直聘\\boss_scrapy\\proxies.txt', 'r') as f:
                lines = f.readlines()
            index = random.randint(0,len(lines)-1)
            proxy = lines[index].strip('\n')
        return proxy
    #把可用ip存放到txt
    def write_txt(self,ip):
        ip = ip
        if ip in ip_list or ip=="":
            pass
        else:
            with open('C:\\Users\\yue_luo\\Desktop\\Boss直聘\\boss_scrapy\\proxies_enable.txt', 'a') as f:
                f.write(ip+"\n")
            ip_list.add(ip)

class MyRetryMiddleware(RetryMiddleware):
    logger = logging.getLogger(__name__)
    ipproxymiddkeware =IPProxyMiddleware()

    def process_response(self, request, response, spider):
        if request.meta.get('dont_retry', False):
            return response
        if response.status in self.retry_http_codes:
            reason = response_status_message(response.status)
            time.sleep(random.randint(3, 5))
            self.logger.warning('返回值异常, 进行重试...')
            proxy = self.ipproxymiddkeware.get_random_proxy()
            print("try3this is response ip:" + proxy)
            # 对当前reque加上代理
            request.meta['proxy'] = proxy
            return self._retry(request, reason, spider) or response
        return response

    def process_exception(self, request, exception, spider):
        if isinstance(exception, self.EXCEPTIONS_TO_RETRY) \
                and not request.meta.get('dont_retry', False):
            time.sleep(random.randint(0, 2))
            self.logger.warning('连接异常, 进行重试...')
            proxy = self.ipproxymiddkeware.get_random_proxy()
            print("try2this is response ip:" + proxy)
            # 对当前reque加上代理
            request.meta['proxy'] = proxy
            return request



