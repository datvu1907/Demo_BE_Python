from pymongo import mongo_client
import pymongo
from app.config import settings

client = mongo_client.MongoClient(
    settings.DATABASE_URL, serverSelectionTimeoutMS=5000)

try:
    conn = client.server_info()
    print(f'Connected to MongoDB {conn.get("version")}')
except Exception:
    print("Unable to connect to the MongoDB server.")

db = client[settings.MONGO_INITDB_DATABASE]
User = db.users
Flight = db.flights
Booking = db.bookings
User.create_index([("email", pymongo.ASCENDING)], unique=True)
Flight.create_index([("date", pymongo.ASCENDING)], unique=False)
Booking.create_index([("date", pymongo.ASCENDING)], unique=False)
#
# Flight.create_index([("date"), pymongo.ASCENDING])
