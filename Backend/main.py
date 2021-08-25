from flask import Flask, render_template, request
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

# Test


@app.route('/<name>')
def test(name):
    return 'Your name is ' + name

# User


@app.route('/gu', methods=["GET"])
def get():
    mariadb_connection = mariadb.connect(
        user='root', password='secret', host='127.0.0.1', port=3306, database='SvenskaSpelet')
    create_cursor = mariadb_connection.cursor()
    create_cursor.execute('Select * From users')
    myresult = create_cursor.fetchall()
    return "{}".format(myresult)


@app.route('/user', methods=["POST"])
def post():
    mariadb_connection = mariadb.connect(
        user='root', password='secret', host='127.0.0.1', port=3306, database='SvenskaSpelet')
    mycursor = mariadb_connection.cursor()
    form_username = request.form['username']
    form_password = request.form['password']
    mycursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)",
                     (form_username, form_password))
    mariadb_connection.commit()
    print(mycursor, "record inserted.")

    return ("record inserted")


@app.route('/user/<id>', methods=["PUT"])
def put(id):
    mariadb_connection = mariadb.connect(
        user='root', password='secret', host='127.0.0.1', port=3306, database='SvenskaSpelet')
    mycursor = mariadb_connection.cursor()
    form_username = request.form['username']
    form_password = request.form['password']
    mycursor.execute("""UPDATE users SET username = %s, password = %s WHERE id = %s
    """, (form_username, form_password, id))
    mariadb_connection.commit()
    return ("record inserted")


@app.route('/user/<id>', methods=["DELETE"])
def delete_user(id):
    mariadb_connection = mariadb.connect(
        user='root', password='secret', host='127.0.0.1', port=3306, database='SvenskaSpelet')
    mycursor = mariadb_connection.cursor()
    mycursor.execute('DELETE FROM users WHERE id = {0} ', (id))
    mariadb_connection.commit()
    return(mycursor.rowcount, "record(s) deleted")


if __name__ == "__main__":
    app.run(debug=True)
