from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi_limiter import FastAPILimiter
from fastapi_limiter.depends import RateLimiter
import redis.asyncio as redis

from src.routes import contacts, auth, users


app = FastAPI(debug=True)

origins = [
    "http://localhost:6379"
    ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(contacts.router, prefix='/api')
app.include_router(auth.app, prefix='/api')
app.include_router(users.router, prefix='/api')


@app.on_event("startup")
async def startup():
    r = await redis.Redis(host='localhost', port=6379, db=0,
                          encoding="utf-8", decode_responses=True)
    await FastAPILimiter.init(r)


@app.get('/', dependencies=[Depends(RateLimiter(times=2, seconds=5))])
def read_root():
    return {'GoIT': 'Python web homework 13'}