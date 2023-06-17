import select
from sqlalchemy.ext.asyncio import AsyncSession
from db.models import Link


async def get_links(session: AsyncSession):
    stmt = select(Link)
    result = await session.execute(stmt)
    return result.scalars().all()
