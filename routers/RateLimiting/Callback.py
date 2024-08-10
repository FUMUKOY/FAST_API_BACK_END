from fastapi import HTTPException, Request, Response, status
from math import ceil

async def default_callback(request: Request, response: Response, pexpire: int):
    """
    Default callback when too many requests
    :param request:
    :param pexpire: The remaining milliseconds
    :param response:
    :return:
    """
    expire = ceil(pexpire / 1000)

    raise HTTPException(
        status.HTTP_429_TOO_MANY_REQUESTS, "Too Many Requests", headers={"Retry-After": str(expire)}
    )
