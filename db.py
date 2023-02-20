import sqlite3
import os 
 
class DB:
    db_url: str

    def __init__(self, db_url: str):
        self.db_url = db_url

        if not os.path.exists(self.db_url):
            self.init_db()

    def call_db(self, query, *args):
        conn = sqlite3.connect(self.db_url)
        cur = conn.cursor()
        res = cur.execute(query,args)
        data = res.fetchall()
        cur.close()
        conn.commit()
        conn.close()
        return data

    def init_db(self):
        init_db_query = """
        CREATE TABLE IF NOT EXISTS country (
            id INTEGER NOT NULL PRIMARY KEY,
            country_name TEXT NOT NULL,
            country_code TEXT  NOT NULL
        );
        """

        init_db_query2 = """
        CREATE TABLE IF NOT EXISTS city (
            id INTEGER NOT NULL PRIMARY KEY,
            city_name  TEXT NOT NULL,
            country_id  INTRGER 
            )
        """
      
        insert_query = """
        INSERT INTO country (
            id,
            country_name,
            country_code
            ) VALUES (?,?,?)
        """
        insert_query2 = """
        INSERT INTO city (
            id,
            city_name, 
            country_id
            ) VALUES (?,?,?)
        """
       


        self.call_db(init_db_query)
        self.call_db(init_db_query2)
       
        self.call_db(insert_query)
        self.call_db(insert_query2)
       
    
    

    
    
