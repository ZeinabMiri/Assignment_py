from pydantic import BaseModel


class Country(BaseModel):
    id: int 
    country_name : str
    country_code : str


class City(BaseModel):
    id: int 
    city_name: str
    country_id: int





    
