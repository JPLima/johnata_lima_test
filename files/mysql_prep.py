import pymysql
import json

with open("/tmp/credentials.json", "r") as f:
    credentials = json.load(f)

try:
    db = pymysql.connect(
         credentials["dbhost"],
         credentials["dbuser"],
         credentials["dbpass"],
         credentials["dbname"],
         credentials["dbport"])
    cursor = db.cursor()
    query = cursor.execute(" create table  name \
                            (name varchar(100),\
                             color varchar(10),\
                             animal varchar(10))")
    db.commit()
    status = {
            "status": "Table created"
             }

except Exception as e:
    status = {
            "status": e
            }
