from flask import Flask
import os
import psycopg2


DB_URL = os.getenv("DB_URL")


app = Flask(__name__)



@app.route('/')
def hello_world():
    return 'Hello World from Sergio Rojas-Aguilar in 3308'



@app.route('/db_test')
def testing():
    
    
    if not DB_URL:
        return f"No .evn called DB_URL"
    
    
    conn = psycopg2.connect(DB_URL) 
    conn.close()
    return  "Database Connection Successful"
    

@app.route('/db_create')
def create():
    conn = psycopg2.connect(DB_URL) 
    cur = conn.cursor()
    
    cur.execute('''
    CREATE TABLE IF NOT EXISTS Basketball(
        First varchar(255),
        Last varchar(255),
        City varchar(255),
        Name varchar(255),
        Number int
        );
    ''')
    
    conn.commit()
    conn.close()
    
    return "Basketball Table Successfully Created"

@app.route('/db_insert')
def insert():
    conn = psycopg2.connect(DB_URL) 
    cur = conn.cursor()
    
    cur.execute('''
    INSERT INTO Basketball (First, Last, City, Name, Number) Values
    ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
    ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
    ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
    ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2),
    ('Sergio', 'Rojas-Aguilar', 'CU Boulder', 'Penguins', 3308);
    ''')
    
    conn.commit()
    conn.close()
    
    return "Basketball Table Populated"


@app.route('/db_select')
def select():
    conn = psycopg2.connect(DB_URL) 
    cur = conn.cursor()
    
    cur.execute('''
        SELECT * FROM Basketball;
    ''')
    
    records = cur.fetchall()
    
    
    conn.close()
    
    response_string =""
    response_string += "<table>"
    for player in records:
        response_string+= "<tr>"
        for info in player:
            response_string += f"<td>{info}</td>"
        response_string+= "</tr>"
    response_string+="</table>"
    
    return response_string


@app.route('/db_drop')
def drop():
    conn = psycopg2.connect(DB_URL) 
    cur = conn.cursor()
    
    cur.execute('''
        DROP TABLE Basketball;
    ''')
    
    conn.commit()
    conn.close()
    
    return "Basketball Table Dropped"