from pydantic import BaseModel


class GroupModel(BaseModel):
    id: str
    name: str
    description: str
