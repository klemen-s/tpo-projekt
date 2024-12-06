from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from backend.entities import Group
from backend.models import GroupModel


async def get_group(session: AsyncSession, group_id: int) -> GroupModel:
    group = (
        await session.scalars(select(Group).where(Group.id == group_id))
    ).one_or_none()
    if not group:
        raise HTTPException(status_code=404, detail="User not found")
    return group
