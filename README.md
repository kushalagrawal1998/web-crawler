# Scraping-Amazon-for-Mobile-details-with-Scrapy
In this repository I have build an Amazon scraper for extracting Mobile details and pricing using a python framework called scrapy. I 
the starting link is - https://www.amazon.in/s?k=mobile&ref=nb_sb_noss_2

Mobile Name
Mobile Reviews
Mobile Prices
After extracting the information, I have saved it into a JSON file.

# Requirements
Scrapy = 1.6.0
pypiwin32 = 224
scrapy-user-agents = 0.1.1

After coding , now you're ready to run the script. But to prevent Amazon from blocking you, you may use the following tricks to bypass their security.

# GoogleBot - Confuse the site by faking your user-agent to be google's bot agent. Amazon allows access to google to crawl it's website. Add the code to your settings.py -> USER_AGENT = 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'

# Rotating User-Agents and Spoofing - Spoof the User Agent by creating a list of user agents and picking a random one for each request. Websites do not want to block genuine users so you should try to look like one. Add the code to your settings.py -> DOWNLOADER_MIDDLEWARES = { 'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None, 'scrapy_user_agents.middlewares.RandomUserAgentMiddleware': 400, }


Now run the project on the terminal using the command scrapy crawl spidername and you can see the responses on the terminal. To generate json file with the responses run the command scrapy crawl spidername -o example.json. A JSON file will be created with the name "example.json".
