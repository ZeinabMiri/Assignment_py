from dotenv import load_dotenv

load_dotenv()

import os
from typing import List
import requests
from models import Country

DB_URL = os.getenv("http://127.0.0.1:8000")


def url(route: str):
    return f"http://127.0.0.1:8000{route}"


print("Hello from country app")


def print_menu():
    print(
        """
    1: Add Country
    2: Get Country
    3: Delete Country
    4: Update Country
    5: Exit program
    """
    )
    pass


def add_country():
    print("Add country")
    country_name = input("Country country_name: ")
    country_code= input("Country country_code: ")
    new_country = Country(country_name=country_name, country_code=country_code)
    res = requests.post(url("/add_country"), json=new_country.dict())
    print(res)


def get_country():
    countries = []
    print("Get country")
    res = requests.get(url("/countries"))
    if not res.status_code == 200:
        return
    data = res.json()
    for country in data:  
        country = Country(**country) 
       
        print("_________")
        print(f"ID: {country.id}")
        print(f"Country_name: {country.country_name}")
        print(f"Country_code: {country.country_code}")
        countries.append(country)
    return countries


def delete_country():
    print("Delete country")
    country_to_delete = input("Id of country you wish to delete: ")
    if not str.isdigit(country_to_delete):
        print("Ids are integers")
        return
    res = requests.delete(url(f"/delete_country/{country_to_delete}"))
    print(res.json())


def update_country(countries: List[Country]):
    print("Update country", countries)
    country_to_update = input("Id of todo you wish to update: ")
    if not str.isdigit(country_to_update):
        print("Ids are integers")
        return

    index = None
    for i, country in enumerate(countries):
        print(country.id)
        if country.id == int(country_to_update):
            index = i
            break



    if index == None:
        print("No such country")
        return
    country = countries[index]

    country_name = input("Country country_name (leave blank if same): ")
    country_code = input("Country country_code (Leave blank if same): ")


    if not country_name:
        country_name = country.country_name
    if not country_code:
        country_code = country.country_code

    new_country = Country(country_name=country_name, country_code=country_code)
    res = requests.put(url(f"/update_country/{country_to_update}"), json=new_country.dict())
    print(res.json())


def main():
    print_menu()
    choice = input("Please choose your action: ")
    choice = choice.strip()
    if not str.isdigit(choice):
        print("Please enter a valid option")
        return

    match int(choice):
        case 1:
            add_country()
        case 2:
            countries = get_country()
        case 3:
            delete_country()
        case 4:
            countries = get_country()
            update_country(countries)
        case 5:
            exit()
        case _:
            print("Please enter a valid choice")


while __name__ == "__main__":
    main()