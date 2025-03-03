import pickle
from flask import Flask, request, jsonify
from flask_restful import Api, Resource, reqparse
import tpot
app = Flask(__name__)
api=Api(app)
model=pickle.load(open('tpot_model.pkl','rb'))

class predict(Resource):
    def get(self):
        return {'message':'This is an Iris Flower Prediction API'}
    def post(self):
        sepal_length = float(request.form['sepal_length'])
        sepal_width = float(request.form['sepal_width'])
        petal_length = float(request.form['petal_length'])
        petal_width = float(request.form['petal_width'])
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

