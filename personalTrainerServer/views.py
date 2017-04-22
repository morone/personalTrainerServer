from personalTrainerServer import app

from flask import request, jsonify, g

from confef import Confef

import sqlite3


DATABASE = 'personalTrainerServer/db/user.db'


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


def insert(table, fields=(), values=()):
    # g.db is the database connection
    try:
        cur = get_db()
        query = 'INSERT INTO %s (%s) VALUES (%s)' % (
            table,
            ', '.join(fields),
            ', '.join(['?'] * len(values))
        )
        cur.execute(query, values)
        cur.commit()
        cur.close()
        return '{"message": "Ok", "code": 200}'
    except Exception as e:
        print('Database error [{0}]'.format(e.message))
        return '{"message": "Error", "code": 404}'


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route("/", methods=['GET'])
def main():
    return "Hello World"


@app.route("/validate_user", methods=['POST'])
def validate_user():
    confef = Confef()
    response = None
    if request.form.get('username') and request.form.get('cref'):
        response = confef.validate_user(
            username=request.form.get('username'),
            cref=request.form.get('cref')
        )
    else:
        response = {"message": "You should provide username and cref", "code": 400}
    return jsonify(response)


@app.route("/create_user", methods=['POST'])
def create_user():
    if request.form.get('username') and request.form.get('cref'):
        response = insert('user', ['name', 'cref', 'uf'], [request.form.get('username'), request.form.get('cref'), request.form.get('uf')])

    return jsonify(response)

if __name__ == "__main__":
    app.run()