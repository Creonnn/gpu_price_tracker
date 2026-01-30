import asyncio
from playwright.async_api import async_playwright

# Todo: refactor so that it works for any bestbuy and newegg
async def get_5090_memexp_paths(base_url, path=None, filter_id=None):
        async with async_playwright() as p:
            browser = await p.chromium.launch()
            assembled_url = assemble_url(base_url, path, filter_id)
            page = await browser.new_page()
            await page.goto(assembled_url)

            # Get the paths to the item
            # Todo: refactor this?
            paths = page.locator('[data-role="product-list-container"]')\
                        .locator('[class="c-shca-icon-item__body-name"]')\
                        .locator('a')
            paths = [await paths.nth(i).get_attribute("href") for i in range(await paths.count())]

            await browser.close()
          
            return paths
        
def assemble_url(base_url, path=None, filter_id=None):
     """
     Assembles base_url with path and/or filter_id
     
     :param base_url: Base URL of website
     :param path: Path to the webpage on website
     :param filter_id: Apply filters if any

     :return URL: The assembled URL

     >>> base_url = "https://www.memoryexpress.com"
     >>> path = "/Category/VideoCards"
     >>> filter_id = "FilterID=825f91ad-c322-6b30-5411-a027616f0c32"
     >>> assemble_url(base_url, path, filter_id)
     'https://www.memoryexpress.com/Category/VideoCards?FilterID=825f91ad-c322-6b30-5411-a027616f0c32'

     >>> base_url = "https://www.memoryexpress.com"
     >>> path = "/Category/VideoCards"
     >>> filter_id = None
     >>> assemble_url(base_url, path, filter_id)
     'https://www.memoryexpress.com/Category/VideoCards'
     """
     if path and filter_id:
          return f"{base_url}{path}?{filter_id}"
     
     elif path:
          return f"{base_url}{path}"
     
     return base_url
     

if __name__ == "__main__":
    base_url = "https://www.memoryexpress.com"
    path = "/Category/VideoCards"
    filter_id = "FilterID=825f91ad-c322-6b30-5411-a027616f0c32"
    print(asyncio.run(get_5090_memexp_paths(base_url, path, filter_id)))