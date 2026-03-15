from flask import Flask
import psycopg2





app = Flask(__name__)





@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/db_test')
def db_test():
    conn = psycopg2.connect("your_db_url_here") 
    conn.close()
    return  "Database Connection Successful"
    