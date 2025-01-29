import sqlite3
from random import sample

connection = sqlite3.connect("projects.db")
cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS projects;")

cursor.execute("""
    CREATE TABLE projects
    (url TEXT, descr TEXT, income INTEGER)
""")

cursor.execute("""INSERT INTO projects VALUES 
    ('giraffes.io', 'Uber, but with giraffes', 1900),
    ('dronesweaters.com', 'Clothes for cold drones', 3000),
    ('hummingpro.io', 'Online humming courses', 120000)
""")

cursor.execute("DROP TABLE IF EXISTS five_columns_table;")

cursor.execute("""CREATE TABLE five_columns_table
    (column1 INTEGER, column2 INTEGER, column3 INTEGER, column4 INTEGER, column5 INTEGER)
""")

def raw_generator():
    insert_rows = []
    for i in range(0, 100):
        insert_rows.append(tuple(sample(range(0, 99999), 5))) #generate list of 100 5-numbered tuples.
    return str(insert_rows)[1:-1] #result is secuence of tuples (string without external square breaks)

cursor.execute(f"""INSERT INTO five_columns_table VALUES
    {raw_generator()}
    """)

connection.commit()