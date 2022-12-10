from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse

import pandas as pd
import numpy as np
import pickle

app = Flask(__name__)
api = Api(app)

model = pickle.load(open('Regression_pipeline.pickle', 'rb'))

class Prediction(Resource):
    def post(self):
        json_data = request.get_json()
        
        df = pd.DataFrame(json_data.values(), index = json_data.keys()).transpose()
        
        res = model.predict(df)
        
        if res == 'Y':
            answer = 'You are likely to get a loan'
            return answer
        elif res == 'N':
            answer = 'You are not likely to get a loan'
            return answer
        else:
            answer = 'There has been an error'
            return answer
        
api.add_resource(Prediction, '/prediction')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)