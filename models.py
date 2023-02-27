from pydantic import BaseModel


class Country(BaseModel):
    id: int = None
    country_name : str
    country_code : str


class City(BaseModel):
    id: int = None
    city_name: str
    country_id: int





    
