from bs4 import BeautifulSoup
import re
class Scraper:
	def __init__(self):
		pass

	def get_product_data(self, content):
		items = []
		# get only name of the product
		for item_info in BeautifulSoup(content, features='html.parser').find_all("div", class_="ordercode"):
			items.append(item_info.get_text())
			# trying to get only name of the item
			item_info = re.compile(r'\b[A-Z0-9][A-Z0-9]+\b')

		return items