import pickle
from flask import Flask, request, jsonify
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS
import tpot
app = Flask(__name__)
api=Api(app)
cors=CORS(app)
model=pickle.load(open('tpot_model.pkl','rb'))

class predict(Resource):
    def get(self):
        return {'message':'This is an Iris Flower Prediction API'}
    def post(self):
        data = request.get_json()
        sepal_length = float(data['sepal_length'])
        sepal_width = float(data['sepal_width'])
        petal_length = float(data['petal_length'])
        petal_width = float(data['petal_width'])
        data = [[sepal_length, sepal_width, petal_length, petal_width]]
        try:
            prediction=model.predict(data)
            name=''
            if prediction[0]==0:
                name='setosa'
            elif prediction[0]==1:
                name='versicolor'
            else:
                name='virginica'
            return jsonify({'prediction':name})
        except:
            return jsonify({'message':'An error occured'}), 500


api.add_resource(predict,'/predict')

if __name__=='__main__':
    app.run(debug=True)

