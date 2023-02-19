import json
from  db import DB


db = DB("Country.db")

create_country = """
INSERT INTO country (
id,
country_name,
country_code
) VALUES (
 ?,?,?
)
"""
create_city = """
INSERT INTO city (
id,
city_name,
country_id
) VALUES (
 ?,?,?
)
"""
# create_travelagency = """
# INSERT INTO travelagency (
# id,
# travelagency_name,
# travelagency_code,
# address
# ) VALUES (
# ?,?,?,?
# )
# """
with open("seed.json" , "r") as f:
    seed_data = json.load(f)
    # print(seed_data)

    for country in seed_data["country"]:
        db.call_db(create_country, country["id"],country["country_name"], country["country_code"])

    for city in seed_data["city"]:
        db.call_db(create_city, city["id"], city["city_name"], city["country_id"])
    
    # for travelagency in seed_data["travelagency"]:
    #     db.call_db(create_travelagency, travelagency["id"], travelagency["travelagency_name"], travelagency["travelagency_code"], travelagency["address"])