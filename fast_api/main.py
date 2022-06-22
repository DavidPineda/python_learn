#Python
from typing import Optional
from enum import Enum

#Pydantic
from pydantic import BaseModel, Field

#FastApi
from fastapi import FastAPI, Body, Path, Query

app = FastAPI()

#Models

class HairColor(Enum):
    white = 'white'
    brown = 'brown'
    black = 'black'
    blonde = 'blonde'
    red = 'red'

class Location(BaseModel):
    country: int
    state: int
    city: int

class Person(BaseModel):
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50
    )
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=50
    )
    age: int = Field(
        ...,
        gt=0,
        le=115
    )
    hair_color: Optional[HairColor] = Field(default=None)
    is_married: Optional[bool] = Field(default=None)

@app.get('/')
def home():
    return {'hello': 'Wolrd'}

# Request and Response body

@app.post('/person/new')
def create_person(person: Person = Body(...)):
    return person

#Validations: Query Parameters

@app.get('/person/detail')
def show_person(
    name: Optional[str] = Query(
        None,
        min_length=1,
        max_length=50,
        title='Person Name',
        description='This is the person name. Its between 1 and 50 charactares'
    ),
    age: int = Query(
        ...,
        title='Person Age',
        description='This is the person age. Its required'
    )
):
    return {name, age}

#Validations: Path Parameters

@app.get('/person/detail/{person_id}')
def show_person(
    person_id: int = Path(
        ...,
        gt=0,
        title='Person Id',
        description='This is required and grater than 0'
    )
):
    return {person_id: "It exists!"}

#Validations: Request Body

@app.put('/persons/{person_id}')
def update_person(
    person_id: int = Path(
        ...,
        gt=0,
        title='Person ID',
        description='This is the person id'
    ),
    person: Person = Body(...),
    location: Location = Body(...)
):
    results = person.dict()
    results.update(location.dict())
    return results
