import time

from sqlalchemy import select
from db.models import Link
from sqlalchemy.ext.asyncio import AsyncSession
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


async def check_if_query_unique(query: str, session: AsyncSession):
    stmt = select(Link).where(Link.query == query)
    row = await session.execute(stmt)
    result = row.scalars().all()
    if result:
        return result
    else:
        return False


async def get_links(session: AsyncSession):
    stmt = select(Link.url)
    result = await session.execute(stmt)
    return result.scalars().all()


async def search_links_and_store(query: str, session: AsyncSession):
    if await check_if_query_unique(query, session):
        return await get_links(session)
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://www.google.com/search")
    button = driver.find_element(By.CLASS_NAME, "QS5gu.sy4vM")
    button.click()

    search_input = driver.find_element(By.NAME, "q")
    search_input.send_keys(query)
    search_input.submit()
    time.sleep(3)

    html = driver.page_source

    soup = BeautifulSoup(html, "html.parser")

    links = soup.find_all(class_="yuRUbf")
    link_urls = [link.a["href"] for link in links]
    for url in link_urls:
        link = Link(query=query, url=url)
        session.add(link)
    await session.commit()
    driver.quit()

    return {"Загружено ссылок": len(link_urls)}
