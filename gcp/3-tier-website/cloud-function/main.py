import functions_framework
import pymysql
import os

s_host = os.environ.get("host")
s_user = os.environ.get("user")
s_pwd = os.environ.get("password")

@functions_framework.http
def main(request):
    request_json = request.get_json(silent=True)

    email = request_json['email']
    password = request_json['password']

    connect = pymysql.connect(db="db",host=s_host,user=s_user,passwd=s_pwd,port=3306)
    cursor = connect.cursor()
    cursor.execute("INSERT INTO account (Email,Password) VALUES (%s,%s)",(email,password))
    connect.commit()
    data = cursor.fetchone()
    return "success"
