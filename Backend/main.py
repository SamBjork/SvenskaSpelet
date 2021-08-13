from flask import Flask, render_template
from flask_restful import Api, Resource
from datetime import datetime
import mariadb

app = Flask(__name__)
api = Api(app)


@app.route('/')
def index():
    return 'Flask'


class HelloWorld(Resource):
    def get(self):
        return{'data': 'Hello World'}


api.add_resource(HelloWorld, "/hw")


@app.route('/db')
def database():
    config = {'host': '127.0.0.1', 'port': 3306, 'user': 'root',
              'password': 'secret', 'database': 'SvenskaSpelet'}
    conn = mariadb.connect(**config)
    cur = conn.cursor()
    sql = "SELECT * FROM user"
    cur.execute(sql)
    myresult = cur.fetchall()
    return "{}".format(myresult)


if __name__ == "__main__":
    app.run(debug=True)
