from typing import Union
from fastapi import FastAPI
import asyncio
import uvicorn

app = FastAPI()


@app.get("/sync/say-hello")
def read_root():
    return {"Hello": "World"}

@app.get("/async/say-hello")
async def async_read_root():
    return {"async Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


async def main():
    config = uvicorn.Config("main:app", port=8000, log_level="info")
    server = uvicorn.Server(config)
    await server.serve()

if __name__ == "__main__":
    asyncio.run(main())