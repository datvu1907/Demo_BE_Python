from datetime import datetime, timedelta
from bson.objectid import ObjectId
from fastapi import APIRouter, Response, status, Depends, HTTPException
from app.database import User, Flight, Booking
from app.serializers.bookingSerializers import BookingEntity, bookingListEntity
from app.serializers.flightSerializers import flightEntity, flightResponseEntity, flightListEntity
from .. import schemas
from pymongo import ReturnDocument
router = APIRouter()


@router.post('/payBooking', status_code=status.HTTP_201_CREATED)
def pay_booking(payload: schemas.PayBookingSchema):
    booking = Booking.find_one_and_update(
        {'_id': ObjectId(str(payload.bookingId))}, {'$set': {'isPaid': True}},  return_document=ReturnDocument.AFTER)
    if not booking:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail='Invalid booking Id')
    result = BookingEntity(booking)
    return {"status": "success", "data": result}


@router.post('/orderHistory', status_code=status.HTTP_201_CREATED)
def order_history(payload: schemas.OrderHistorySchema):
    user = User.find_one({'_id': ObjectId(str(payload.userId))})
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail='Invalid user Id')
    history = Booking.find({'userId': payload.userId, 'isPaid': True})
    if history is None:
        return {"status": "success", "data": []}
    result = bookingListEntity(history)
    return {"status": "success", "data": result}
