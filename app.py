from flask import Flask
import os
import psycopg2

DB_URL = os.getenv("DB_URL")



app = Flask(__name__)





@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/1')
def test1():
    return 'test1'


@app.route('/db_test')
def testing():
    conn = psycopg2.connect(DB_URL) 
    conn.close()
    return  "Database Connection Successful"
    
    