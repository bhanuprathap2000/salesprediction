import numpy as np
from flask import Flask, request, jsonify, render_template
from joblib import load

app = Flask(__name__)
model = load('salesofcompanypredict')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
   
    
    int_features = [float(x) for x in request.form.values()]
    
    final_features = [np.array(int_features)]
    print(type(final_features))
    prediction = model.predict(final_features)
    
    output = prediction[0]

    return render_template('index.html', prediction_text='Sales of the company  in units {}'.format(output))



if __name__ == "__main__":
    app.run()