# Real Estate Agent Web Scraper
I had to do cold outreach to hundreds of real estate agents one summer. So, instead of manually getting their information from their websites, I created webscrapers using the selenium library in Python. The major agencies I was scraping from had fairly similar structures so I created a class, GeneralScraper, that contains methods for grabbing the data. GeneralScraper is the parent of MultiScraper -- a class that's geared for websites where the agents' contact info lived on a separate page from their name. 

Run scrape is the driver code which creates an instance of general scraper or its child class, multi-scraper. 
