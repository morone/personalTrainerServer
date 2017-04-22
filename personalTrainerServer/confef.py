import requests


class Confef:

	def __init__(self):
		self.url = 'http://www.confef.org.br/extra/registrados/mostra_nome.asp'

	def validate_user(self, username, uf="00", cref=None):
		msg = []
		payload = [('nome', username), ('uf', uf)]
		# POST with form-encoded data
		r = requests.post(self.url, data=payload)
		if cref in r.text and username in r.text:
			message = "Ok"
			code = 200
		else:
			message = "User not found"
			code = 404

		msg.append({'message': message, 'code': code})
		# Response, status etc
		return msg