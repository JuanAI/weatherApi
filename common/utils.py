import json
import requests
import datetime

class Utils(object):

	def __init__(self, file_path='data.txt', _id=None):
		self.file_path=file_path
		self._id=_id


	@staticmethod
	def convert_data(raw_data):

		data = []
		if raw_data['cod'] == '200':

			for i in raw_data['list']:

				date=i['dt_txt']
				date=datetime.datetime.strptime(date,'%Y-%m-%d %H:%M:%S')
				new_date=date.strftime('%Y%m%d')
				new_hour=date.strftime('%H%M')

				d={ 
				'date': new_date,
				'hour': new_hour,
				'description': i['weather'][0]['description'],
				'temp-K': i['main']['temp'],
				'temp-C': str(round(float(i['main']['temp'])-273.15)),
				'humidity': i['main']['humidity'],
				'pressure': i['main']['pressure']
				}

				data.append(d)

		final_data={'cod':raw_data['cod'],'data':data}

		return final_data


	def get_json(self):
		if self._id == None:			
			with open('data.txt') as json_file:  
				raw_data = json.load(json_file)

			json_data=self.convert_data(raw_data)			

		else:
			url ="http://api.openweathermap.org/data/2.5/forecast?q=London,uk&appid="+self._id
			response = requests.get(url)
			json_data = json.loads(response.text)
			json_data=self.convert_data(json_data)

		return json_data
