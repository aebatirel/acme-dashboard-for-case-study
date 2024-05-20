from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
import json
from ..database import database
from ..models import Restaurant
from bson import ObjectId
from bson.json_util import dumps

router = APIRouter()

@router.get('/restaurants')
async def get_restaurants():
    restaurants = await database.restaurants.find().to_list(1000)
    return JSONResponse(content=json.loads(dumps(restaurants)))

@router.post('/restaurants')
async def create_restaurant(restaurant: Restaurant):
    result = await database.restaurants.insert_one(restaurant.dict())
    return {"id": str(result.inserted_id)}

@router.put('/restaurants/{id}')
async def update_restaurant(id: str, restaurant: Restaurant):
    result = await database.restaurants.update_one({"_id": ObjectId(id)}, {"$set": restaurant.dict()})
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Restaurant not found")
    return {"id": id}

@router.delete('/restaurants/{id}')
async def delete_restaurant(id: str):
    result = await database.restaurants.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Restaurant not found")
    return {"id": id}
