from pydantic import BaseModel


class Country(BaseModel):
    id: int 
    country_name : str
    country_code : str


class City(BaseModel):
    id: int 
    city_name: str
    country_id: int 



class Travelagency(BaseModel):
    id: int
    travelagency_name: str
    travelagency_code: int 
    address: str
    city_id: int



    
