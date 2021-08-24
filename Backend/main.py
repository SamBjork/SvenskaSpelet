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


class PostUser(Resource):
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


class UpdateUser(Resource):
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


class GetUsers(Resource):
    def get(self):
        mariadb_connection = mariadb.connect(
            user='root', password='secret', host='127.0.0.1', port=3306, database='SvenskaSpelet')
        create_cursor = mariadb_connection.cursor()
        create_cursor.execute('Select * From users')

        myresult = create_cursor.fetchall()
        # return

        return "{}".format(myresult)


class DeleteUser(Resource):
    def delete(self):
        mariadb_connection = mariadb.connect(
            user='root', password='secret', host='127.0.0.1', port=3306, database='SvenskaSpelet')
        mycursor = mariadb_connection.cursor()
        sql = "DELETE FROM users WHERE id = '1'"

        mycursor.execute(sql)

        mariadb_connection.commit()

        print(mycursor.rowcount, "record(s) deleted")
        return(mycursor.rowcount, "record(s) deleted")


api.add_resource(HelloWorld, "/hw")

api.add_resource(PostUser, "/pu")

api.add_resource(GetUsers, "/gu")

api.add_resource(UpdateUser, "/uu")

api.add_resource(DeleteUser, "/du")


@app.route('/db')
def database():
    config = {'host': '127.0.0.1:5000', 'port': 3306, 'user': 'root',
              'password': 'secret', 'database': 'SvenskaSpelet'}
    conn = mariadb.connect(**config)
    cur = conn.cursor()
    sql = "Select * From users"
    cur.execute(sql)
    myresult = cur.fetchall()
    return "{}".format(myresult)


if __name__ == "__main__":
    app.run(debug=True)
