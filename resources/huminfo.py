from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
import datetime

from common.utils import Utils


class HumInfo(Resource):
	parser = reqparse.RequestParser()

	def get(self, date, hour):
		utils=Utils()
		json=utils.get_json()        

		if json['cod'] != '200':
			return {'status': 'error', 'message': 'error api access'}

		else:

			filtered=next(filter(lambda x: x['date'] == date and x['hour'] == hour, json['data']), None)
			date_ask=datetime.datetime.strptime(date+hour,'%Y%m%d%H%M').strftime('%Y-%m-%d %H:%M')
			string='No data for '+str(date_ask)
		if filtered == None:
			return {'status': 'error', 'message': string}

		return {'humidity':str(filtered['humidity'])+"%"}