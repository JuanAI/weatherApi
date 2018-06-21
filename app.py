from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required, current_identity
from common.utils import Utils

from security import authenticate, identity

from resources.api_id import ApiId
from resources.gen_sum import GenSummary
from resources.gen_sum_def import GenSummaryDef
from resources.gen_sum_rest import GenSummaryRestr
from resources.huminfo import HumInfo
from resources.pressinfo import PressInfo
from resources.tempinfo import TempInfo


app = Flask(__name__)
app.secret_key = '1234'
api = Api(app)

@app.before_first_request
def deleteContent(fName='api_password.txt'):
    text_file = open(fName, "w")
    text_file.close()


jwt = JWT(app, authenticate, identity)

api.add_resource(ApiId, '/weather/london/<name>/<surname>') #OK
api.add_resource(GenSummary, '/weather/london/<name>/<surname>/<date>/<hour>') #OK
api.add_resource(GenSummaryDef, '/weather/london/<date>/<hour>') #OK
api.add_resource(GenSummaryRestr, '/weather/london/restricted/<date>/<hour>') #OK
api.add_resource(TempInfo, '/weather/london/<date>/<hour>/temperature') #OK
api.add_resource(HumInfo, '/weather/london/<date>/<hour>/humidity') #OK
api.add_resource(PressInfo, '/weather/london/<date>/<hour>/pressure') #OK


if __name__ == '__main__':
    app.run(debug=True)