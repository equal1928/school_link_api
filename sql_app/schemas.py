from pydantic import BaseModel


class FlatBase(BaseModel):
    title: str
    description: str | None = None


class FlatCreate(FlatBase):
    pass


class Flat(FlatBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

class HouseBase(BaseModel):
    id: int
    description: str | None = None


class HouseCreate(HouseBase):
    pass


class House(HouseBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class SchoolBase(BaseModel):
    pass


class SchoolCreate(SchoolBase):
    pass


class School(SchoolBase):
    id: int
    is_active: bool


    class Config:
        orm_mode = True