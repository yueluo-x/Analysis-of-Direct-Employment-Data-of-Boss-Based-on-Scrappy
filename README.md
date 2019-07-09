# Analysis-of-Direct-Employment-Data-of-Boss-Based-on-Scrappy
基于Scrapy框架爬取Boss直聘首页技术分类以及细化爬取Boss直聘技术分类中的各个分支并保存至MongoDB数据库，其中包括招聘公司、职位、年薪、学历要求等数据；利用Highcharts
使数据可视化，并用Django构建页面展示数据及数据图表。

项目使用了填充header、构建随机User-Agent，简单IP池等方法对Boss直聘的反爬策略（判断header、同一IP爬取超过5000条左右数据进行302重定向等）进行应对。
