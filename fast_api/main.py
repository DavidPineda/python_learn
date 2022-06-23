#Python
from doctest import Example
from typing import Optional
from enum import Enum

#Pydantic
from pydantic import BaseModel, Field, HttpUrl

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
    country: int = Field(..., gt=0)
    state: int = Field(..., gt=0)
    city: int = Field(..., gt=0)

    class Config:
        schema_extra = {
            'example': {
                'country': 57,
                'state': 1,
                'city': 1,
            }
        }

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
    password: str = Field(..., min_length=8)
    hair_color: Optional[HairColor] = Field(default=None)
    is_married: Optional[bool] = Field(default=None)
    web_site: Optional[HttpUrl] = Field(default=None)

    class Config:
        schema_extra = {
            'example': {
                'first_name': 'David',
                'last_name': 'Pineda',
                'age': 31,
                'password': '12345678',
                'hair_color': 'blonde',
                'is_married': True,
                'web_site': 'https://davidpineda.com',
            }
        }

class PersonOut(BaseModel):
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
    web_site: Optional[HttpUrl] = Field(default=None)

@app.get('/')
def home():
    return {'hello': 'Wolrd'}

# Request and Response body

@app.post('/person/new', response_model=Person, response_model_exclude={'password'})
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
        description='This is the person name. Its between 1 and 50 charactares',
        example='Tatiana'
    ),
    age: int = Query(
        ...,
        title='Person Age',
        description='This is the person age. Its required',
        example=25
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
        description='This is required and grater than 0',
        example=1
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
        description='This is the person id',
        example=1
    ),
    person: Person = Body(...),
    location: Location = Body(...)
):
    results = person.dict()
    results.update(location.dict())
    return results
