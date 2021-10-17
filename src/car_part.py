from lib.crawler import Crawler

crawler = Crawler(
	seed="https://www.autokelly.bg/bg/products/43758570.html?ids=39849642;51224611",
	base_url='https://www.autokelly.bg'
)
crawler.save_content_to_file('tests')