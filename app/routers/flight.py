from datetime import datetime, timedelta
from bson.objectid import ObjectId
from fastapi import APIRouter, Response, status, Depends, HTTPException

from app import oauth2
from app.database import User, Flight
from app.serializers.userSerializers import userEntity, userResponseEntity
from app.serializers.flightSerializers import flightEntity, flightResponseEntity, flightListEntity
from .. import schemas, utils
from app.oauth2 import AuthJWT
from ..config import settings
router = APIRouter()


@router.post('/addFlight', status_code=status.HTTP_201_CREATED)
def add_flight(payload: schemas.FlightBaseSchema):
    # user = userResponseEntity(User.find_one({'_id': ObjectId(str(user_id))}))
    result = Flight.insert_one(payload.dict())
    new_flight = flightResponseEntity(
        Flight.find_one({'_id': result.inserted_id}))
    return {"status": "success", "data": new_flight}


@router.get('/getAllFlights', status_code=status.HTTP_201_CREATED)
def get_all_flights():
    cursor = Flight.find({})
    result = flightListEntity(cursor)
    return {"status": "success", "data": result}


@router.post('/getFlight', status_code=status.HTTP_201_CREATED)
def get_flight(id: str):
    result = flightEntity(Flight.find_one({'_id': ObjectId(str(id))}))
    return {"status": "success", "data": result}
