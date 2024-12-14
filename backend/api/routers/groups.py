from backend.api.dependencies.core import DBSessionDep
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from backend.services.group import get_group
from backend.utils.templates import templates

router = APIRouter(
    prefix="/groups",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)

@router.get("/", response_class=HTMLResponse)
def get_index(req: Request):
    return templates.TemplateResponse(
        request=req, name="groups/index.html", context={"req": req}
    )

@router.get("/{group_id}")
async def group_details(db_session: DBSessionDep, group_id: int):
    user = await get_group(db_session, group_id)
    return user
