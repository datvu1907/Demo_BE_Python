def BookingEntity(booking) -> dict:
    return {
        "id": str(booking["_id"]),
        "flightId": booking["flightId"],
        "userId": booking["userId"],
        "isPaid": booking["isPaid"]
    }


def bookingListEntity(booking) -> list:
    return [BookingEntity(item) for item in booking]
