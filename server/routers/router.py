import select
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from fastapi import APIRouter, Depends, HTTPException
from selenium import webdriver
from selenium.webdriver.common.by import By
from db.database import get_session
from db.models import Link
from sqlalchemy.ext.asyncio import AsyncSession
from crud import crud


api_router = APIRouter()

from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


@api_router.get("/")
async def search_and_store_links(
    query: str, session: AsyncSession = Depends(get_session)
):
    try:
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install())
        )
        driver.get("https://www.google.com/")
        search_input = driver.find_element(By.NAME, "q")
        search_input.send_keys(query)
        search_input.submit()
        print("successfully")
        links = driver.find_elements(By.TAG_NAME, "a")
        print(links)
        link_urls = [link.get_attribute("href") for link in links]
        # for link in link_urls:
        #     print(link)
        #     query = Link(url=link)
        #     session.add(query)

        # await session.commit()
        await driver.quit()

        return len(link_urls)
    except Exception as e:
        raise HTTPException(detail=f"{e}", status_code=500)


@api_router.get("/links")
async def get_links(session: AsyncSession = Depends(get_session)):
    try:
        return await crud.get_links(session)
    except Exception as e:
        raise HTTPException(detail=f"database error{e}", status_code=500)
