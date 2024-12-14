from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware

from backend.database import sessionmanager
from backend.api.routers.groups import router as groups_router
from backend.utils.templates import templates

@asynccontextmanager
async def lifespan(app: FastAPI):
    await sessionmanager.create_all_tables()

    yield
    if sessionmanager._engine is not None:
        await sessionmanager.close()


app = FastAPI(lifespan=lifespan, docs_url="/api/docs")

origins = [
    "http://localhost:3000",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")



@app.get("/", response_class=HTMLResponse)
def read_root(req: Request):
    return templates.TemplateResponse(
        request=req, name="index.html", context={"request": req}
    )


app.include_router(groups_router)
