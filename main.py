import uvicorn
from typing import Annotated
from fastapi import FastAPI, Header, APIRouter
from midllewares import CheckBodyMidlleware
from scheme import Test, WrongTest

app = FastAPI()
router = APIRouter(prefix="/route")

app.add_middleware(CheckBodyMidlleware)


@router.get("/")
async def root(custom_header: Annotated[str | None, Header()]):
    return {"custom header": custom_header}


@router.get("/items")
async def root():
    return {"items": "items"}


@router.post("/test")
async def test(custom_header: Annotated[str | None, Header()], data: Test):
    return {"custom_header": custom_header, "data": data}


@router.post("/wrong_test")
async def wrong_test(custom_header: Annotated[str | None, Header()], data: WrongTest):
    return {"custom_header": custom_header, "data": data}


@router.post("/hello")
async def hello():
    return "hello"


if __name__ == "__main__":
    app.include_router(router)
    uvicorn.run(app, port=8080)
