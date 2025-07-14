from flask import Flask, render_template, request
import pymysql


app = Flask(__name__)

HOST=''
USER=''
PASSWORD=''
DB=''

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/wake')
def wake():
    connection = pymysql.connect(host=HOST, user=USER, password=PASSWORD, database=DB, cursorclass=pymysql.cursors.DictCursor)
    with connection.cursor() as cursor:
        sql = "INSERT INTO `test` (`test`) VALUES (%s)"
        cursor.execute(sql, ('success'))
        connection.commit()
    print('WAKE UP DEVS')
    return 'uwu'

if '__name__' == '__main__':
    app.run(host='0.0.0.0',port='80',debug=True)
