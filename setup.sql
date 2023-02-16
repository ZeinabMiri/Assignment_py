
-- Create Table country with 3 columns
CREATE Table 
country (
    id INTEGER NOT NULL PRIMARY KEY,
	country_name TEXT NOT NULL,
	country_code TEXT  NOT NULL
);

-- Create Table city with 3 columns 
CREATE Table 
city (
   id INTEGER NOT NULL PRIMARY KEY,
   city_name  TEXT NOT NULL,
   country_id   INTEGER NOT NULL,
    FOREIGN KEY (country_id) REFERENCES country (id)
);

--Create Table travelagency with 5 columns
CREATE Table 
travelagency (
    id INTEGER NOT NULL PRIMARY KEY,
	travelagency_name  TEXT NOT NULL,
	travellagency_code INTEGER,
	address TEXT, 
	city_id INTEGER  NOT NULL,
	FOREIGN KEY (city_id) REFERENCES city (id)
);