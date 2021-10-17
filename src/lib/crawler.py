import requests
from bs4 import BeautifulSoup


import warnings
warnings.filterwarnings('ignore')

class Crawler:
    def __init__(self, seed, base_url):
        self.seed = seed
        self.base_url = base_url
        self.urls_to_visit = [seed]
        self.visited_urls = []

    def get_products_data(self):
        pass


    def run(self):
        for url in self.urls_to_visit:
            try:
                content = self.get_html_content(url)
                links = self.get_links_from_html(content)

                for item in links:
                    product_url = self.base_url+item
                    product_content = self.get_html_content(product_url)

                    # products_info = scraper.get_product_data(product_content)
                    # print(products_info)


            except Exception as err:
                print(err)
            else:
                self.visited_urls.append(url)
                self.urls_to_visit.remove(url)

    def get_html_content(self, url):
        try:
            # create request(se     ed=seed, escaping SSL Certificate)
            response = requests.get(url, verify=False)

            # set encoding of page
            response.encoding = "utf-8"

            # set variable for html text
            content = response.text

            return content
        except requests.RequestException as error:
            print(error)

    def save_content_to_file(self,content):
        filename = utils.get_project_folder()+'/html_data/motor_oils.html'
        with open(filename, 'w') as f:
            f.write(content)

    def get_links_from_html(self, content):
        # create a list
        links = []

        # loop through all a tags
        # TODO: make it more eficient: use find_all('a') only on products links container
        for link in BeautifulSoup(content, features='html.parser').find_all('a', href=True):
            # add just the href tags to a list(links)
            if '/bg/autokelly/item/' in link['href']:
                links.append(link['href'])

        # loop through all href tags to check what returns web crawler
        for link in links:
            print(link)

        return links


if __name__ == '__main__':
    import utils as utils

    crawler = Crawler(
        seed="https://www.autokelly.bg/bg/products/43758570.html?ids=39849642;51224611",
        base_url='https://www.autokelly.bg'
    )
    # crawler.run()
    crawler.save_content_to_file('tst')

else:
    import lib.utils as utils





