import requests
import re
from bs4 import BeautifulSoup

# import extracted links from crawler
from crawler import links

# create variable with main page + single link from extracted links
for item in links:
    url = 'https://www.autokelly.bg'+item

    # set variable for document
    html = "./html_data/item_info.html"

    # create request(url=url, escaping SSL Certificate)
    r = requests.get(url, verify=False)

    # set encoding of page
    r.encoding = "utf-8"

    # get content only if response code is 200
    status_code = r.status_code
    if status_code == 200:

        # set variable for html text
        content = r.text

        # save html text of the response
        with open(html, 'w') as f:
            f.write(content)
            items = []
            # get only name of the product
            for item_info in BeautifulSoup(content, features='html.parser').find_all("div", class_="ordercode"):
                items.append(item_info.get_text())
                # trying to get only name of the item
                item_info = re.compile(r'\b[A-Z0-9][A-Z0-9]+\b')
                print(items)

    else:
        break
