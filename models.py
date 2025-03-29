from pydantic import BaseModel
from typing import List

class MovieRequest(BaseModel):
    title: str
    year: int

class MovieResponse(BaseModel):
    titulo: str
    ano: int
    sinopse: str

"""
class MovieResponse(BaseModel):
    titulo: str
    ano: int
    sinopse: str
    reviews: List[str]
"""
