from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

import datetime

from common.utils import Utils

import json
import os


class GenSummary(Resource):
	parser = reqparse.RequestParser()

	def get(self, name, surname, date, hour):

		if os.stat("api_password.txt").st_size == 0:
			return {'status': 'error', 'message': 'you have not saved any api password'}

		else:

			with open('api_password.txt') as f:
				lines = f.readlines()

			api_user=json.loads(lines[0])

			if api_user['name'] == name and api_user['surname'] == surname:
				utils_aux=Utils(_id=api_user['id'])
				json_aux=utils_aux.get_json()

				if json_aux['cod'] != '200':
					return {'status': 'error', 'message': 'error api access'}

				else:

					filtered=next(filter(lambda x: x['date'] == date and x['hour'] == hour, json_aux['data']), None)
					date_ask=datetime.datetime.strptime(date+hour,'%Y%m%d%H%M').strftime('%Y-%m-%d %H:%M')
					string='No data for '+str(date_ask)

					print(filtered)

					if filtered == None:
						return {'status': 'error', 'message': string}

					return {'description':filtered['description'],
					'temperature':filtered['temp-C']+'C',
					'pressure':filtered['pressure'],
					'humidity':filtered['humidity']} 

			else:
				return {'status': 'error', 'message': 'your username do not match'}
