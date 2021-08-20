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
    def get(self):
        mariadb_connection = mariadb.connect(
            user='root', password='secret', host='127.0.0.1', port=3306, database='SvenskaSpelet')
        create_cursor = mariadb_connection.cursor()
        create_cursor.execute('Select * From users')
        # config = {'host': '127.0.0.1', 'port': 3306, 'user': 'root',
        #           'password': 'secret', 'database': 'SvenskaSpelet'}
        # conn = mariadb.connect(**config)
        # cur = conn.cursor()
        # sql = " "
        # cur.execute(sql)

        myresult = create_cursor.fetchall()
        # return

        return "{}".format(myresult)


api.add_resource(HelloWorld, "/hw")

api.add_resource(PostUser, "/pu")


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
