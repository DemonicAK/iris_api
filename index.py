from flask import Flask, request
from flask_cors import CORS
import pickle as pkl


app = Flask(__name__)
CORS(app)


model = pkl.load(open('iris.pkl', 'rb'))


@app.route('/')
def hello():
    return 'Hello World!'


@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the data from the POST request.
        # Make prediction using model loaded from disk as per the data.
        data = request.get_json(force=True)
        # Take the first value of prediction
        input_data = [data['p1'], data['p2'],
                      data['p3'], data['p4']]
        for i in range(len(input_data)):
            if input_data[i] == "":
                result = {
                    "error": "Pls enter all the values",
                    "TaskSuccess": False,
                }
                return result, 400

            input_data[i] = float(input_data[i])

            if input_data[i] <= 0:
                result = {
                    "error": "only positive integers are allowed",
                    "TaskSuccess": False,
                }
                return result, 400

        prediction = model.predict([input_data])
        # print("prediction",prediction)
        output = prediction[0]
        # print("output",output)
        target_names = ['setosa', 'versicolor', 'virginica']
        name = target_names[output]
        # print(name)
        result = {
            "name": f"{name}",
            "TaskSuccess": True,
        }
        return result, 200
    except ValueError as e:
        # print(e)
        result = {
            "error": "only integers are allowed",
            "TaskSuccess": False,
        }
        return result, 400
    except:
        result = {
            "error": "something went wrong",
            "TaskSuccess": False,
        }
        return result, 400
