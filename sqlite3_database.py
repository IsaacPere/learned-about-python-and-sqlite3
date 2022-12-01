#create empty database with python 

from multiprocessing import Value
from optparse import Values
import sqlite3 as database_module

connecting_database = database_module.connect("gta.db")

db_cursor = connecting_database.cursor()
db_cursor.execute(
    "create table gta(release_year integer, release_name text, city text)"
    )


release_list = [
    (1997, "Grand Theft Auto", "State of New Guernsey"),
    (1999, "Grand Theft Auto 2", "Anywhere, USA"),
    (2001, "Grand Theft Auto 3", "Liberty City"),
    (2002, "Grand Theft Auto : Vice City", "Vice City"),
    (2004, "Grand Theft Auto : Sans Andrea","State of San Andrea"),
    (2008, "Grand Theft Auto IV","Liberty City"),
    (2013, "Grand Theft Auto V", "Los Santos")
]

db_cursor.executemany(
    "insert into gta values(?,?,?)", release_list)


#print database rows
for row in db_cursor.execute("select * from gta"):
    print(row)


#print specific rows
print("*****************************************************")
db_cursor.execute(
    "select * from gta where city=:c", {"c":"Liberty City"}
    )
gta_search = db_cursor.fetchall()
print(gta_search)

#combine multiple database tables
db_cursor.execute(
    "create table cities (gta_city text, real_city text)"
    )
db_cursor.execute(
    "insert into cities values(?,?)", ("Liberty City", "New York"))
db_cursor.execute(
    "select * from cities where gta_city=:c", {"c":"Liberty City"}
)
searching_the_city = db_cursor.fetchall()
print(searching_the_city)

#Manipulate database fetched from database
print("*****************************************")
for database_inserting in gta_search:
    adjust= [searching_the_city[0][1] if Values==searching_the_city[0][0] else Values for Values in database_inserting]
    print(adjust)
    

connecting_database.close()