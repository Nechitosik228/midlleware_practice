from pydantic import BaseModel


class Test(BaseModel):
    test: str


class WrongTest(BaseModel):
    name: str
