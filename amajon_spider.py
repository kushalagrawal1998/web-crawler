import scrapy

class Myspider(scrapy.Spider):
	name = "amajon_spider"

	def start_requests(self):
		urls = [

		"https://www.amazon.in/Honor-Blue-4GB-64GB-Storage/dp/B07R2W2WTS/ref=sr_1_1_sspa?keywords=mobile&qid=1559230457&s=gateway&sr=8-1-spons&psc=1",
		"https://www.amazon.in/Honor-Lite-Black-64GB-Storage/dp/B07QWLBPJW/ref=sr_1_2_sspa?keywords=mobile&qid=1559230457&s=gateway&sr=8-2-spons&psc=1",
		"https://www.amazon.in/Redmi-Pro-Black-32GB-Storage/dp/B07DJL15QT/ref=sr_1_5?keywords=mobile&qid=1559230457&s=gateway&sr=8-5",


		]
		for url in urls:
			yield scrapy.Request(url=url,callback=self.parse)

	def parse(self,response):
		page_id = response.url.split('/')[-2]
			

			

		mains = response.css("div.a-container")

		for main in mains:
			name = main.css("span.a-size-large::text").get().strip()
			price = main.css("span.a-size-medium::text").get()
			ratings = main.css("span.a-icon-alt::text").get()

			yield{

			    "name":name,
			    "price":price,
			    "ratings":ratings,
			}
			next_page_id = response.css("li.next a::attr(href)").get()
			if next_page_id is not None:
				next_page = response.urljoin(next_page_id)
				yield scrapy.Request(next_page,callback=self.parse)




