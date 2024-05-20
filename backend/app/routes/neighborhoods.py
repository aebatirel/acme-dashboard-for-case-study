from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
import json
from ..database import database
from ..models import Neighborhood
from bson import ObjectId
from bson.json_util import dumps

router = APIRouter()

@router.get('/neighborhoods')
async def get_neighborhoods():
    neighborhoods = await database.neighborhoods.find().to_list(1000)
    return JSONResponse(content=json.loads(dumps(neighborhoods)))

@router.post('/neighborhoods')
async def create_neighborhood(neighborhood: Neighborhood):
    result = await database.neighborhoods.insert_one(neighborhood.dict())
    return {"id": str(result.inserted_id)}

@router.put('/neighborhoods/{id}')
async def update_neighborhood(id: str, neighborhood: Neighborhood):
    result = await database.neighborhoods.update_one({"_id": ObjectId(id)}, {"$set": neighborhood.dict()})
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Neighborhood not found")
    return {"id": id}

@router.delete('/neighborhoods/{id}')
async def delete_neighborhood(id: str):
    result = await database.neighborhoods.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Neighborhood not found")
    return {"id": id}
