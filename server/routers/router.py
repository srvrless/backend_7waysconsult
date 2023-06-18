from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from crud import crud
from db.database import get_session

api_router = APIRouter()


@api_router.get("/alfrted")
async def search_links(query: str, session: AsyncSession = Depends(get_session)):
    # try:
    return await crud.search_links_and_store(query, session)
    # except Exception:
    #     raise HTTPException(detail=f"Something went wrong", status_code=403)


@api_router.get("/links")
async def get_links(session: AsyncSession = Depends(get_session)):
    try:
        return await crud.get_links(session)
    except Exception:
        raise HTTPException(detail=f"Something went wrong", status_code=403)
