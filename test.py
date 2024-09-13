import asyncio
from playwright.async_api import async_playwright

# ==========================
from langgraph.graph.message import add_messages
from langgraph.graph import END, START, StateGraph, MessagesState
from langgraph.prebuilt import ToolNode

# ==========================
from typing import Literal, List, Annotated, Sequence, TypedDict


async def main():
    playwright = await async_playwright().start()
    browser = await playwright.chromium.launch(headless=False)
    page = await browser.new_page()
    await page.set_viewport_size({"width": 800, "height": 600})
    await page.goto("https://www.mvdis.gov.tw/m3-emv-vil/vil/penaltyQueryPay#gsc.tab=0")
    await page.locator("#id1").fill("B223456789")
    await page.locator("#birthday").fill("1130911")
    captcha_image = await page.get_by_role("img", name="驗證碼").screenshot(
        path="captcha.png"
    )
    print(captcha_image)
    await page.pause()
    await browser.close()
    await playwright.stop()


async def open_browser():
    playwright = await async_playwright().start()
    browser = await playwright.chromium.launch(headless=False)
    page = await browser.new_page()
    await page.set_viewport_size({"width": 800, "height": 600})
    await page.goto("https://www.mvdis.gov.tw/m3-emv-vil/vil/penaltyQueryPay#gsc.tab=0")
    await page.locator("#id1").fill("B223456789")
    await page.locator("#birthday").fill("1130911")
    captcha_image = await page.get_by_role("img", name="驗證碼").screenshot(
        path="captcha.png"
    )
    return playwright, browser, page


# asyncio.run(main())


class GraphState(TypedDict):
    round: int
    inputs: str
    playwright_status: List # 儲存playwright page等等目前狀態
    bot_status: List # 儲存linebot目前狀態，ex: response token
    status: str # 目前狀態，等待user、等待LLM、等待playwright


def get_website_result(graph_state: GraphState):
    pass


def get_captcha_image(graph_state: GraphState):
    pass
