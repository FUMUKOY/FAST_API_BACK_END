from fastapi import FastAPI
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded 
from fastapi_limiter.depends import RateLimiter
from fastapi_limiter import FastAPILimiter
import uvicorn


app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Server is listening..."}


if __name__ == "__main__":
    uvicorn.run("main:app", debug=True, reload=True)





