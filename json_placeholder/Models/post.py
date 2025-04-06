from pydantic import BaseModel, ValidationError


class Post(BaseModel):
    userId: int
    id: int
    title: str
    body: str