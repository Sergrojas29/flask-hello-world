from flask import Flask
import os
import psycopg2





app = Flask(__name__)





@app.route('/')
def hello_world():
    return 'Hello, World!'



@app.route('/db_test')
def testing():
    DB_URL = os.getenv("DB_URL")
    if not DB_URL:
        return f"No .evn called DB_URL"
    conn = psycopg2.connect(DB_URL) 
    conn.close()
    return  "Database Connection Successful"
    
    