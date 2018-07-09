import scrapy
from scrapy.selector import Selector
from caipiao.items import CaipiaoItem
import csv
with open('shujubiao.csv', 'a', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['期次', '红球', '蓝球'])
class caipiaoSpider(scrapy.spiders.Spider):
    name = 'daletou'
    start_urls ={'http://trend.caipiao.163.com/dlt/?periodNumber=100',}

    def parse(self, response):
        item = CaipiaoItem()
        res = Selector(response)
        '//*tobdy//tr/@data-period'
        #中奖的红球
        lis_red_ball = res.xpath('//*[@id="cpdata"]//tr/td[@class="ball_red"]/text()|//*[@id="cpdata"]//tr/td[@class="ball_brown"]/text()').extract()
        #中奖的蓝球
        lis_blue_ball = res.xpath('//*[@id="cpdata"]//tr/td[@class="ball_blue"]/text()').extract()
        #近100期

        lis_number = res.xpath('//*[@id="cpdata"]//tr/@data-period').extract()
        "//*[@id='cpdata']/tr/td[@class='ball_red js-repeate-ball']/text()"
        # lis_red_ball2 = res.xpath('//*[@id="cpdata"]//tr/td[@class="ball_brown"]/text()').extract()
        # print(len(lis_red_ball),len(lis_blue_ball),len(lis_number))
        for i in lis_number:
            item['number'] = i
            red_ball = []
            for _ in range(5):
                ball = lis_red_ball.pop(0)
                red_ball.append(ball)
            item['red_ball'] = red_ball
            blue_ball = []
            for _ in range(2):
                ball = lis_blue_ball.pop(0)
                blue_ball.append(ball)
            item['blue_ball'] = blue_ball

   
            yield item
            with open('shujubiao.csv','a', encoding='utf-8',newline='') as f:
                writer = csv.writer(f)
                writer.writerow([item['number'],item['red_ball'],item['blue_ball']])
            #分别取出前几个数，加到数据库中再把里面的球删掉，进入下一次循环
            red_ball.clear()
            blue_ball.clear()