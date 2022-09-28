import scrapy
from scrapy.crawler import CrawlerProcess
import sys
# sys.path.append(r"C:\Users\QuyenTKQ\Documents\Codes\smsaexpress\smsaexpress_crawler")
from items import SmsaexpressItem


class SmsSpiderSpider(scrapy.Spider):
    name = 'sms_spider'
    allowed_domains = ['www.smsaexpress.com']
    custom_settings = {
        'FEED_FORMAT': 'csv',
        'FEED_URI': 'test.csv'
    }
    with open("tracking-numbers.txt", "rt") as f:
        start_urls = ['https://www.smsaexpress.com/ae/trackingdetails?tracknumbers[0]=' + track_number.strip() for track_number in f.readlines()]

    def parse(self, response):
        timeline_row = response.xpath("//div[@class='tracking-details-container']/div[@class='row']")

        for row in timeline_row:
            for detail_dom in row.xpath(".//div[@class='trk-wrap']"):
                item = SmsaexpressItem()
                item["tracking_number"] = response.xpath("//div[@class='row tracking-border-bottom']/div[2]/div/div[2]/p/text()").get()
                item["latest_status"] = response.xpath("//div[@class='tracking-box-info']/div[2]/div[2]/div/div[1]/p/text()").get()
                item["latest_date"] = row.xpath(".(//div[@class='date-wrap'])[1]/h4/text()").get()
                item["date"] = row.xpath(".//div[@class='date-wrap']/h4/text()").get()
                item["status"] = detail_dom.xpath(".//h4[1]/text()").get()
                item["time"] = detail_dom.xpath(".//div[@class='trk-wrap-content-left']/span/text()").get()
                item["location"] = detail_dom.xpath(".//div[@class='trk-wrap-content-right']/span/text()").get()
                self.logger.info(item)
                yield item

if __name__ == "__main__":
    process = CrawlerProcess()

    process.crawl(SmsSpiderSpider)
    process.start() # the script will block here until the crawling is finished
