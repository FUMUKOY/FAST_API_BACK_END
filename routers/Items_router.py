from fastapi import APIRouter, HTTPException, Request
from fastapi.params import Depends
from fastapi_limiter.depends import RateLimiter
from fastapi_limiter import FastAPILimiter
import redis.asyncio as redis
import sys
from contextlib import asynccontextmanager

sys.path.append(r'C:\Users\enochn\Documents\Projects\Python\FAST_API_Back_End')

from db.items import read_db_item
from routers.RateLimiting.Callback import default_callback
from routers.RateLimiting.Identifier import default_identifier

@asynccontextmanager
async def lifespan(_: APIRouter):     #function but also called an asynchronous resource
    redis_connection = redis.from_url("redis://localhost:6379", encoding="utf8")
    await FastAPILimiter.init(redis_connection)
    print("Initialized FastAPILimiter")
    yield
    await FastAPILimiter.close()
    print("Closed FastAPILimiter")

#This means that any routes defined within this router will have /items.
router = APIRouter(
    
    lifespan=lifespan,
    prefix="/items"   
)


@router.get("/{item_id}", dependencies=[Depends(RateLimiter(times=2, seconds=5),Depends(default_identifier))])
async def read_item(item_id: int):  # function but also called an asynchronous resource
    db_item = read_db_item(item_id)
    return db_item











    

    
        
    
  











