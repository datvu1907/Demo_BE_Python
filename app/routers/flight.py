from datetime import datetime, timedelta
from bson.objectid import ObjectId
from fastapi import APIRouter, Response, status, Depends, HTTPException
from app.database import User, Flight, Booking
from app.serializers.bookingSerializers import BookingEntity, bookingListEntity
from app.serializers.flightSerializers import flightEntity, flightResponseEntity, flightListEntity
from .. import schemas
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
    flight = Flight.find_one({'_id': ObjectId(str(id))})
    if not flight:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail='Invalid flight Id')
    result = flightEntity(flight)
    return {"status": "success", "data": result}


@router.post('/bookFlight', status_code=status.HTTP_201_CREATED)
def book_flight(payload: schemas.CreateBookingSchema):
    flight = Flight.find_one({'_id': ObjectId(str(payload.flightId))})
    if not flight:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail='Invalid flight Id')
    user = User.find_one({'_id': ObjectId(str(payload.userId))})
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail='Invalid user Id')
    booking = schemas.BookingBaseSchema(
        flightId=payload.flightId, userId=payload.userId)

    result = Booking.insert_one(booking.dict())
    # new_booking = BookingEntity(Booking.find_one(
    #     {'_id': result.inserted_id}))
    if not result:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='Server down')
    return {"status": "success", "Message": "Flight is added to cart"}


@router.post('/getFlight', status_code=status.HTTP_201_CREATED)
def get_flight(id: str):
    flight = Flight.find_one({'_id': ObjectId(str(id))})
    if not flight:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail='Invalid flight Id')
    result = flightEntity(flight)
    return {"status": "success", "data": result}


@router.post('/getBooking', status_code=status.HTTP_201_CREATED)
def get_booking(payload: schemas.GetBookingSchema):
    user = User.find_one({'_id': ObjectId(str(payload.userId))})
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail='Invalid user Id')
    bookings = Booking.find({'userId': payload.userId, 'isPaid': False})
    result = bookingListEntity(bookings)
    if not result:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='Server down')
    return {"status": "success", "data": result}
