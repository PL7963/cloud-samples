from flask import Flask, render_template, request
import pymysql
import os

PASSWORD = os.getenv('PASSWORD')
USER = os.getenv('USER')
HOST = os.getenv('HOST')
DB = os.getenv('DB')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def buy():
    email = request.form['email']
    connection = pymysql.connect(host=HOST, user=USER, password=PASSWORD, database=DB, cursorclass=pymysql.cursors.DictCursor)
    with connection.cursor() as cursor:
        sql = "INSERT INTO `contact` (`email`) VALUES (%s)"
        cursor.execute(sql, (email))
        connection.commit()
    connection.close()
    return 'success uwu'
