from personalTrainerServer import app

from flask import request, jsonify

from confef import Confef

from user import User


def _run_validation(username, cref):
    confef = Confef()
    return confef.validate_user(
        username=username,
        cref=cref
    )


@app.route("/", methods=['GET'])
def main():
    return "Hello World"


@app.route("/validate_user", methods=['POST'])
def validate_user():
    response = []
    if request.form.get('username') and request.form.get('cref'):
        response = _run_validation(
            username=request.form.get('username'),
            cref=request.form.get('cref')
        )
    else:
        response.append({"message": "You should provide username and cref", "code": 400})
    return jsonify(response)


@app.route("/create_user", methods=['POST'])
def create_user():
    # TODO create user class
    response = []
    if request.form.get('username') and request.form.get('cref'):
        validation = _run_validation(
            username=request.form.get('username'),
            cref=request.form.get('cref')
        )
        if validation[0].get('code') == 200:
            user = User()
            response = user.create_new_user(
                request.form.get('username'),
                request.form.get('cref'),
                request.form.get('uf')
            )
        else:
            response.append({"message": "User has no registered CREF", "code": 400})

    return jsonify(response)


@app.route("/list_users", methods=['GET'])
def list_users():
    user = User()
    return jsonify(user.get_user_list())

if __name__ == "__main__":
    app.run()