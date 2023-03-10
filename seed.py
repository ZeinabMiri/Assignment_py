import json
from  db import DB


db = DB("Country.db")

create_country = """
INSERT INTO country (
country_name,
country_code
) VALUES (
 ?,?
)
"""
# create_city = """
# INSERT INTO city (
# city_name,
# country_id
# ) VALUES (
#  ?,?
# )
# """

with open("seed.json" , "r") as f:
    seed_data = json.load(f)
    #print(seed_data)

    for country in seed_data["country"]:
        db.call_db(create_country,country["country_name"], country["country_code"])

    # for city in seed_data["city"]:
    #     db.call_db(create_city, city["city_name"], city["country_id"])
    
   