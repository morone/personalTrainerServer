from personalTrainerServer import app

from flask import request, jsonify

from confef import Confef


@app.route("/", methods=['GET'])
def main():
	return "Hello World"


@app.route("/user", methods=['POST'])
def get_user_information():
	confef = Confef()
	response = None
	if request.form.get('username') and request.form.get('cref'):
		response = confef.get_user_data(
			username=request.form.get('username'),
			cref=request.form.get('cref')
		)
	else:
		response = {"message": "You should provide username and cref", "code": 400}
	return jsonify(response)

if __name__ == "__main__":
	app.run()