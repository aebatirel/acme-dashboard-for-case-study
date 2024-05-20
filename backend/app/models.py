from pydantic import BaseModel

class Restaurant(BaseModel):
    name: str
    cuisine: str
    borough: str

class Neighborhood(BaseModel):
    name: str
