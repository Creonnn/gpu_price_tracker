import requests
from bs4 import BeautifulSoup
from tools.const.links import cc_links
import pandas as pd
import warnings
warnings.filterwarnings("ignore")

class Extract:
    
    def __init__(self, links):
        self.df = pd.DataFrame(columns=["name", "link", "price"])

        for link in links:
            response = requests.get(link)
            soup = BeautifulSoup(response.text, "html.parser")
            name = Extract._get_item_name(soup)
            price = Extract._get_item_price(soup)
            self.df.loc[len(self.df)] = [link, name, price]


    def _get_item_name(self, soup):
        pass

    def _get_item_price(self, soup):
        pass

    def _get_availability(self, soup):
        pass

if __name__ == "__main__":  
    import asyncio
    from playwright.async_api import async_playwright

    url = "https://www.memoryexpress.com/Products/MX00132651"
    async def main():
        async with async_playwright() as p:
            browser = await p.chromium.launch()
            page = await browser.new_page()
            await page.goto(url)
            print(await page.title())
            await browser.close()
    asyncio.run(main())