from flask import Flask, render_template
from flask_restful import Api, Resource
from datetime import datetime
import mysql.connector as mariadb


app = Flask(__name__)
api = Api(app)


@app.route('/')
def index():
    return 'Flask'


class HelloWorld(Resource):
    def get(self):
        return{'data': 'Hello World'}


api.add_resource(HelloWorld, "/hw")

# User


@app.route('/pu')
def post(self):
    mariadb_connection = mariadb.connect(
        user='root', password='secret', host='127.0.0.1', port=3306, database='SvenskaSpelet')
    mycursor = mariadb_connection.cursor()
    #create_cursor.execute('Select * From users')
    sql = "INSERT INTO users (username, password) VALUES (%s, %s)"
    val = ("John", "Highway 21")
    mycursor.execute(sql, val)
    mariadb_connection.commit()
    print(mycursor, "record inserted.")

    return ("record inserted")


@app.route('/uu')
def put(self):
    mariadb_connection = mariadb.connect(
        user='root', password='secret', host='127.0.0.1', port=3306, database='SvenskaSpelet')
    mycursor = mariadb_connection.cursor()
    #create_cursor.execute('Select * From users')
    sql = "UPDATE users SET username = 'first' WHERE id = 1"
    mycursor.execute(sql)
    mariadb_connection.commit()
    print(mycursor, "record inserted.")

    return ("record inserted")


@app.route('/gu')
def get(self):
    mariadb_connection = mariadb.connect(
        user='root', password='secret', host='127.0.0.1', port=3306, database='SvenskaSpelet')
    create_cursor = mariadb_connection.cursor()
    create_cursor.execute('Select * From users')

    myresult = create_cursor.fetchall()
    # return

    return "{}".format(myresult)


@app.route('/du')
def delete_user(self):
    mariadb_connection = mariadb.connect(
        user='root', password='secret', host='127.0.0.1', port=3306, database='SvenskaSpelet')
    mycursor = mariadb_connection.cursor()
    sql = "DELETE FROM users WHERE id = '1'"

    mycursor.execute(sql)

    mariadb_connection.commit()

    print(mycursor.rowcount, "record(s) deleted")
    return(mycursor.rowcount, "record(s) deleted")


if __name__ == "__main__":
    app.run(debug=True)
