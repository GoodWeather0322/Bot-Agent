import asyncio
from playwright.async_api import async_playwright


# two pages in one browser
async def main():
    playwright = await async_playwright().start()
    browser = await playwright.chromium.launch(headless=False)
    page_one = await browser.new_page()
    page_two = await browser.new_page()
    await page_one.goto("https://www.google.com")
    await page_two.goto("https://www.youtube.com")
    await page_one.wait_for_timeout(5000)
    await page_two.wait_for_timeout(5000)
    # await page_one.pause()
    await browser.close()
    await playwright.stop()


# two tabs in one browser
async def main2():
    playwright = await async_playwright().start()
    browser = await playwright.chromium.launch(headless=False)
    context = await browser.new_context()

    page_one = await context.new_page()
    page_two = await context.new_page()
    await page_one.set_viewport_size({"width": 800, "height": 600})
    await page_one.goto("https://www.google.com")
    await page_two.goto("https://www.youtube.com")
    await page_one.wait_for_timeout(5000)
    await page_two.wait_for_timeout(5000)
    await browser.close()
    await playwright.stop()


asyncio.run(main2())
