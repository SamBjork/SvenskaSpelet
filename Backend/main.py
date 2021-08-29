from flask import Flask, render_template, request
from flask_cors import CORS, cross_origin
from flask_restful import Api, Resource
from datetime import datetime
import mysql.connector as mariadb
import json

app = Flask(__name__)
api = Api(app)
CORS(app, support_credentials=True)

mariadb_connection = mariadb.connect(
    user='root', password='secret', host='127.0.0.1', port=3306, database='SvenskaSpelet')


@app.route('/')
def index():
    return '<h1>Det Svenska Spelet!</h1>'


# Test
class HelloWorld(Resource):
    def get(self):
        return{'data': 'Hello World'}


api.add_resource(HelloWorld, "/hw")


@app.route('/<name>')
def test(name):
    return 'Your name is ' + name

# Login


@app.route('/login', methods=['GET', 'POST'])
@cross_origin(supports_credentials=True)
def login():
    create_cursor = mariadb_connection.cursor()
    form_username = request.form['username']
    form_password = request.form['password']
    create_cursor.execute(" SELECT * FROM Users WHERE username = %s AND password = %s",
                          (form_username, form_password))
    myresult = create_cursor.fetchall()
    if(myresult != []):
        username = myresult[0][1]
        password = myresult[0][2]
    else:
        return "you entered incorrect credentials", 403
    if(password == form_password and username == form_username):
        return "{}".format(myresult)
    else:
        return "you entered incorrect credentials", 403
# User


@app.route('/user', methods=["GET"])
def get_users():
    create_cursor = mariadb_connection.cursor()
    create_cursor.execute('Select * From Users')
    myresult = create_cursor.fetchall()
    return "{}".format(myresult)


@app.route('/user', methods=["POST"])
def post_user():
    mycursor = mariadb_connection.cursor()
    form_username = request.form.get['username', False]
    form_password = request.form.get['password', False]
    mycursor.execute("INSERT INTO Users (username, password) VALUES (%s, %s)",
                     (form_username, form_password))
    mariadb_connection.commit()
    return ("user inserted")


@app.route('/user/<id>', methods=['PUT'])
def update_user(id):
    mycursor = mariadb_connection.cursor()
    form_username = request.form['username']
    form_password = request.form['password']
    mycursor.execute("""UPDATE Users SET username = %s, password = %s WHERE id = %s
    """, (form_username, form_password, id))
    mariadb_connection.commit()
    return ("user " + id + " is updated")


@app.route('/user/<id>', methods=['DELETE'])
def delete_user(id):
    mycursor = mariadb_connection.cursor()
    mycursor.execute('DELETE FROM Users WHERE userid = {0}'.format(id))
    mariadb_connection.commit()
    return("user " + id + " is deleted")

# Game


@app.route('/game', methods=["GET"])
def get_games():
    create_cursor = mariadb_connection.cursor()
    create_cursor.execute('Select * From Games')
    myresult = create_cursor.fetchall()
    return "{}".format(myresult)


@app.route('/game', methods=["POST"])
def post_game():
    mycursor = mariadb_connection.cursor()
    form_score = request.form['score']
    form_userid = request.form['userid']
    mycursor.execute("INSERT INTO Games (score, userid) VALUES (%s, %s)",
                     (form_score, form_userid))
    mariadb_connection.commit()
    return ("game inserted")


@app.route('/game/<id>', methods=['DELETE'])
def delete_game(id):
    mycursor = mariadb_connection.cursor()
    mycursor.execute('DELETE FROM Games WHERE gameid = {0}'.format(id))
    mariadb_connection.commit()
    return("game " + id + " is deleted")

# Question


@app.route('/question', methods=["GET"])
def get_question():
    create_cursor = mariadb_connection.cursor()
    create_cursor.execute('Select * From Questions')
    myresult = create_cursor.fetchall()
    return "{}".format(myresult)


@app.route('/question', methods=["POST"])
def post_question():
    mycursor = mariadb_connection.cursor()
    form_text = request.form['text']
    form_correctanswer = request.form['correctanswer']
    form_wronganswer1 = request.form['wronganswer1']
    form_wronganswer2 = request.form['wronganswer2']
    form_wronganswer3 = request.form['wronganswer3']
    form_points = request.form['points']
    mycursor.execute("INSERT INTO Questions (text, correctanswer, wronganswer1, wronganswer2, wronganswer3, points) VALUES (%s, %s, %s, %s, %s, %s)",
                     (form_text, form_correctanswer, form_wronganswer1, form_wronganswer2, form_wronganswer3, form_points))
    mariadb_connection.commit()
    return ("question inserted")


@app.route('/question/<id>', methods=['PUT'])
def update_question(id):
    mycursor = mariadb_connection.cursor()
    form_text = request.form['text']
    form_correctanswer = request.form['correctanswer']
    form_wronganswer1 = request.form['wronganswer1']
    form_wronganswer2 = request.form['wronganswer2']
    form_wronganswer3 = request.form['wronganswer3']
    form_points = request.form['points']
    mycursor.execute("""UPDATE Questions SET text = %s, correctanswer = %s, wronganswer1 = %s, wronganswer2 = %s, wronganswer3 = %s, points = %s WHERE id = %s
    """, (form_text, form_correctanswer, form_wronganswer1, form_wronganswer2, form_wronganswer3, form_points, id))
    mariadb_connection.commit()
    return ("question " + id + " is updated")


@app.route('/question/<id>', methods=['DELETE'])
def delete_question(id):
    mycursor = mariadb_connection.cursor()
    mycursor.execute('DELETE FROM Questions WHERE id = {0}'.format(id))
    mariadb_connection.commit()
    return("question " + id + " is deleted")


if __name__ == "__main__":
    app.run(debug=True)
