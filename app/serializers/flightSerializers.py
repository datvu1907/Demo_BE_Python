def flightEntity(flight) -> dict:
    return {
        "id": str(flight["_id"]),
        "title": flight["title"],
        "description": flight["description"],
        "image": flight["image"],
        "price": flight["price"],
        "date": flight["date"],
    }


def flightResponseEntity(flight) -> dict:
    return {
        "id": str(flight["_id"]),
        "title": flight["title"],
        "description": flight["description"],
        "image": flight["image"],
        "price": flight["price"],
        "date": flight["date"],
    }


def flightListEntity(flights) -> list:
    return [flightEntity(item) for item in flights]
