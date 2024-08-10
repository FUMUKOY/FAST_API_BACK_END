from fastapi import  HTTPException, Request

async def default_identifier(request: Request):
    forwarded = request.headers.get("X-Forwarded-For")
    if forwarded:
        client_identifier = forwarded.split(",")[0]
    else: 
        client_identifier = request.client.host + ":" + request.scope["path"]

    print("Client Identifier:", client_identifier)

    return client_identifier