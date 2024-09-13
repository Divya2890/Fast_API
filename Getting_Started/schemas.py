
from pydantic import BaseModel


class Blogbase(BaseModel):
    title: str
    body : str