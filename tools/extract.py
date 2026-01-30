import pandas as pd
import warnings
import asyncio
from tools.scraper import assemble_url, get_5090_memexp_paths
from playwright.async_api import async_playwright
warnings.filterwarnings("ignore")

class Extract:
    
    def __init__(self, base_url, paths):
        self.df = pd.DataFrame(columns=["name", "link", "price"])
        self.base_url = base_url
        self.paths = paths


    async def extract_data(self):
        async with async_playwright() as p:
            browser = await p.chromium.launch()
            page = await browser.new_page()
            for path in self.paths:
                url = assemble_url(base_url=self.base_url, path=path)
                await page.goto(url)
                name = self._clean_name(await page.title())
                price = self._clean_price(await page.locator('[class="c-capr-pricing__totals"]')\
                                .first\
                                .inner_text())
                new = {'name': name, 'link': url, 'price': price}
                self.df.loc[len(self.df)] = new
            await browser.close()

    def _clean_name(self, name):

        name = name.split(",")[0]\
                .replace("Dual HDMI", "")\
                .replace("HDMI", "")\
                .replace("w/", "")\
                .replace("PCI-E", "")\
                .replace("Triple DP", "")\
                .replace("Graphics Card", "")\
                .replace("32GB", "")\
                .strip()
    
        return " ".join(name.split())

    def _clean_price(self, price):
        
        price = price.replace("Only", "")\
                    .replace("$", "")\
                    .replace(",", "")
        return float(price)


if __name__ == "__main__":  
    base_url = "https://www.memoryexpress.com"
    catalog_path = "/Category/VideoCards"
    filter_id = "FilterID=825f91ad-c322-6b30-5411-a027616f0c32"
    paths = asyncio.run(get_5090_memexp_paths(base_url, catalog_path, filter_id))
    data = Extract(base_url, paths)
    asyncio.run(data.extract_data())
    print(data.df)