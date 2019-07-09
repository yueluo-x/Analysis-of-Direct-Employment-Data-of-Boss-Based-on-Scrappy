# -*- coding: utf-8 -*-
import scrapy


class BossIndexSpider(scrapy.Spider):
    name = "boss_index"
    allowed_domains = ["www.zhipin.com"]
    start_urls = ['https://www.zhipin.com/?sid=sem_pz_bdpc_dasou_title']
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
        'cookie': 'lastCity=101010100; sid=sem_pz_bdpc_dasou_title; JSESSIONID=""; __g=sem_pz_bdpc_dasou_title; _uab_collina=155257470081104788858221; __c=1552575458; __l=r=https%3A%2F%2Fsp0.baidu.com%2F9q9JcDHa2gU2pMbgoY3K%2Fadrc.php%3Ft%3D06KL00c00fDIFkY00nqx0KZEgsZbpcGT00000nPijNC00000T0B0fs.THdBULP1doZA80K85Hb3njDznj63g1FxuAT0T1dBPAwWmyDknH0snjFhPWuh0ZRqrjbYnRfLnjTvPHRLnWm1nHc4PjIjrHb4PH63n1K7rjb0mHdL5iuVmv-b5HnkrHDYPHbdnWDhTZFEuA-b5HDv0ARqpZwYTZnlQzqLILT8Xh9GTA-8QhPEUitOTv-b5gP-UNqsX-qBuZKWgvw9TvqdgLwGIAk-0APzm1Y1rjDdP0%26tpl%3Dtpl_11534_18997_15000%26l%3D1510822595%26attach%3Dlocation%253D%2526linkName%253D%2525E6%2525A0%252587%2525E5%252587%252586%2525E5%2525A4%2525B4%2525E9%252583%2525A8-%2525E6%2525A0%252587%2525E9%2525A2%252598-%2525E4%2525B8%2525BB%2525E6%2525A0%252587%2525E9%2525A2%252598%2526linkText%253DBoss%2525E7%25259B%2525B4%2525E8%252581%252598%2525E2%252580%252594%2525E2%252580%252594%2525E6%252589%2525BE%2525E5%2525B7%2525A5%2525E4%2525BD%25259C%2525EF%2525BC%25258C%2525E6%252588%252591%2525E8%2525A6%252581%2525E8%2525B7%25259F%2525E8%252580%252581%2525E6%25259D%2525BF%2525E8%2525B0%252588%2525EF%2525BC%252581%2526xp%253Did(%252522m3191459521_canvas%252522)%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FH2%25255B1%25255D%25252FA%25255B1%25255D%2526linkType%253D%2526checksum%253D177%26ie%3Dutf-8%26f%3D8%26ch%3D8%26tn%3D98012088_2_dg%26wd%3Dboss%25E7%259B%25B4%25E8%2581%2598%26oq%3Dboss%25E7%259B%25B4%25E8%2581%2598%26rqlang%3Dcn&l=%2Fwww.zhipin.com%2F%3Fsid%3Dsem_pz_bdpc_dasou_title&g=%2Fwww.zhipin.com%2F%3Fsid%3Dsem_pz_bdpc_dasou_title; __a=97970414.1552574698.1552574698.1552575458.2.2.1.2; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1552574701,1552575458; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1552575458',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'max-age=0',
        'upgrade-insecure-requests:': '1'
    }
    def parse(self, response):
        for i in range(1,15):
            urls = response.xpath('//dl[@class][1]/div[@class="menu-sub"]/ul/li[%s]/div[@class="text"]/a/@href'%i).extract()
            # print(urls)
            types = response.xpath('//dl[@class][1]/div[@class="menu-sub"]/ul/li[%s]/div[@class="text"]/a/text()'%i).extract()
            classify = response.xpath('//dl[@class][1]/div[@class="menu-sub"]/ul/li[%s]/h4/text()'%i).extract()
            # print(types)
            for url,type in zip(urls,types):
                nationwide_url = 'https://www.zhipin.com/c100010000/h_101010100/?query={}&ka=sel-city-100010000'.format(type)
                url = ''.join(['https://www.zhipin.com',url])
                item = {
                    'url': url,
                    'classify':classify,
                    'type':type,
                    'nationwide_url':nationwide_url,
                }

                yield item
