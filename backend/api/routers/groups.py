from backend.api.dependencies.core import DBSessionDep
from fastapi import APIRouter

from backend.services.group import get_group

router = APIRouter(
    prefix="/api/groups",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)


@router.get("/{group_id}")
async def group_details(db_session: DBSessionDep, group_id: int):
    """
    Get any gruop details
    """
    user = await get_group(db_session, group_id)
    return user
