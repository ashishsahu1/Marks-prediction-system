from flask import Flask, render_template
from os import name
import pickle

from flask.globals import request 

app = Flask(__name__)
app.config['SESSION_COOKIE_SECURE'] = False

model = pickle.load(open('model.pkl', 'rb'))

preds = model.predict([[9.25]])

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/predict')
def predict():
    hr = request.form('')
    return render_template('after.html', pred = preds )

if __name__ == "__main__":
    app.run(debug = True)