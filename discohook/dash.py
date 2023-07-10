from fastapi.responses import HTMLResponse


async def dashboard():
    with open("discohook/index.html", "rb") as f:
        return HTMLResponse(content=f.read(), status_code=200)
