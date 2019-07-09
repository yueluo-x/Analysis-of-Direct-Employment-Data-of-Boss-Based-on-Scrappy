# -*- coding: utf-8 -*-


import scrapy, urllib.request

from scrapy import Request


class BossDetailsSpider(scrapy.Spider):
    name = "boss_details"
    allowed_domains = ["www.zhipin.com"]
    # 从boss_index.py获取start_urls
    start_urls = [
        'https://www.zhipin.com/c100010000/h_101010100/?query=后端开发&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=Java&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=C++&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=PHP&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=数据挖掘&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=C&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=C#&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=.NET&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=Hadoop&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=Python&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=Delphi&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=VB&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=Perl&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=Ruby&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=Node.js&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=搜索算法&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=Golang&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=自然语言处理&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=推荐算法&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=Erlang&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=算法工程师&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=语音/视频/图形开发&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=数据采集&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=移动开发&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=HTML5&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=Android&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=iOS&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=WP&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=移动web前端&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=Flash&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=JavaScript&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=U3D&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=COCOS2DX&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=测试工程师&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=自动化测试&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=功能测试&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=性能测试&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=测试开发&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=移动端测试&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=游戏测试&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=硬件测试&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=软件测试&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=运维工程师&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=运维开发工程师&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=网络工程师&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=系统工程师&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=IT技术支持&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=系统管理员&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=网络安全&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=系统安全&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=DBA&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=数据&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=ETL工程师&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=数据仓库&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=数据开发&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=数据挖掘&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=数据分析师&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=数据架构师&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=算法研究员&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=项目经理&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=项目主管&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=项目助理&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=项目专员&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=实施顾问&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=实施工程师&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=需求分析工程师&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=硬件&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=嵌入式&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=自动化&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=单片机&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=电路设计&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=驱动开发&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=系统集成&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=FPGA开发&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=DSP开发&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=ARM开发&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=PCB工艺&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=模具设计&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=热传导&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=材料工程师&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=精益工程师&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=射频工程师&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=前端开发&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=web前端&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=Javascript&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=Flash&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=HTML5&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=通信技术工程师&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=通信研发工程师&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=数据通信工程师&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=移动通信工程师&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=电信网络工程师&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=电信交换工程师&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=有线传输工程师&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=无线射频工程师&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=通信电源工程师&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=通信标准化工程师&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=通信项目专员&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=通信项目经理&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=核心网工程师&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=通信测试工程师&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=通信设备工程师&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=光通信工程师&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=光传输工程师&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=光网络工程师&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=电子工程师&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=电气工程师&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=FAE&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=电气设计工程师&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=高端技术职位&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=技术经理&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=技术总监&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=测试经理&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=架构师&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=CTO&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=运维总监&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=技术合伙人&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=人工智能&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=机器学习&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=深度学习&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=图像算法&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=图像处理&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=语音识别&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=图像识别&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=算法研究员&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=软件销售支持&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=售前工程师&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=售后工程师&ka=sel-city-100010000',
        'https://www.zhipin.com/c100010000/h_101010100/?query=其他技术职位&ka=sel-city-100010000',
    ]

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36',
        'cookie': 'lastCity=101010100; _uab_collina=155257470081104788858221; JSESSIONID=""; __c=1554113061; __g=-; __l=l=%2Fwww.zhipin.com%2Fc100010000%2F%3Fquery%3D%25E5%2590%258E%25E7%25AB%25AF%25E5%25BC%2580%25E5%258F%2591%26page%3D10%26ka%3Dpage-10&r=; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1553955445,1553957870,1554040675,1554113061; __a=97970414.1552574698.1554040675.1554113061.99.7.6.99; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1554113327',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'max-age=0',
        'upgrade-insecure-requests:': '1'
    }

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url=url, meta={"proxy": ""}, callback=self.parse,
                          headers=self.headers, dont_filter=True, )

    def parse(self, response):
        url = urllib.request.unquote(response.url)
        l_type = url.split('query=')[-1].split('&')[0]
        # l_href = response.xpath('//div[@class="info-primary"]//h3/a/@href').extract()
        # l = response.xpath('//div[@class="info-primary"]//p/text()').extract()
        l_title = response.xpath('//div[@class="info-primary"]//div[@class="job-title"]/text()').extract()
        l_salary = response.xpath('//div[@class="info-primary"]//span[@class="red"]/text()').extract()
        l_company = response.xpath('//div[@class="info-company"]//a/text()').extract()
        # //div[@class="info-company"]//p/text()[1]
        l_location = response.xpath('//div[@class="info-primary"]//p/text()[1]').extract()
        l_experience = response.xpath('//div[@class="info-primary"]//p/text()[2]').extract()
        l_education = response.xpath('//div[@class="info-primary"]//p/text()[3]').extract()
        # print(l_education,l_experience, l_location)
        # print(l_title,l_salary,l_company)
        for location, title, salary, experience, education, company in zip(l_location, l_title, l_salary,
                                                                           l_experience, l_education, l_company, ):
            item = {
                'location': location,
                'title': title,
                'salary': salary,
                'experience': experience,
                'education': education,
                'company': company,
                # 'l_type' :jobClass
            }
            item['type'] = l_type
            yield item
        if response.xpath('//div[@class="page"]'):
            if not response.xpath('//a[@class="next disabled"]'):
                # print('*' * 45, response.request.meta['proxy'],'*' * 46, )
                next_url = response.xpath('//div[@class="page"]/a/@href').extract()[-1]
                next_url = ''.join(['https://www.zhipin.com', next_url])
                # print('*' * 45, next_url, '*' * 46, )
                yield scrapy.Request(url=next_url, meta={"proxy": response.request.meta['proxy']}, callback=self.parse,
                                     dont_filter=True, )
                # yield scrapy.Request(url=next_url,callback=self.parse,dont_filter=True,)
