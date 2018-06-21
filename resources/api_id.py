import json
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

class ApiId(Resource):
	parser = reqparse.RequestParser()
	parser.add_argument('id',
	    type=str,
	    required=True,
	    help="This field cannot be left blank!"
	)

	def post(self, name, surname):
		data = ApiId.parser.parse_args()

		api_acc = {'name': name, 'surname': surname, 'id': data['id']}

		with open('api_password.txt', 'w') as file:
			file.write(json.dumps(api_acc))


		return {'message': 'Your Api id has been saved'}