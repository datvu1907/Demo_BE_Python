from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.routers import auth, user, flight, payment
from fastapi.security import OAuth2PasswordBearer


app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
origins = [
    settings.CLIENT_ORIGIN,
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(auth.router, tags=['Auth'], prefix='/api/auth')
app.include_router(user.router, tags=['User'], prefix='/api/user')
app.include_router(flight.router, tags=['Flight'], prefix='/api/flight')
app.include_router(payment.router, tags=['Payment'], prefix='/api/payment')


@app.get("/api/healthchecker")
def root():
    return {"message": "Welcome to FastAPI with MongoDB"}


# @app.get('/books', dependencies=[Depends(reusable_oauth2)])
# def list_books():
#     return {'data': ['Sherlock Homes', 'Harry Potter', 'Rich Dad Poor Dad']}
