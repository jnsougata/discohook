import traceback
from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.responses import JSONResponse


async def catch_exceptions_middleware(request: Request, call_next):
    try:
        return await call_next(request)
    except Exception as e:
        err = traceback.format_exception(type(e), e, e.__traceback__)
        return JSONResponse(content={"traceback": err}, status_code=500)
