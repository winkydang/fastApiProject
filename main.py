import os

import uvicorn
from fastapi import FastAPI
from application.test1.views import test1_router


def factory() -> FastAPI:
    app = FastAPI()
    app.include_router(test1_router)

    return app


app = factory()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/{var1}/{var2}")
async def say_hello(var1: str, var2: str):
    return {"message": f"{var1} {var2}"}


if __name__ == '__main__':
    # os.system('sh start.sh')
    uvicorn.run(app, host='127.0.0.1', port=8674)
