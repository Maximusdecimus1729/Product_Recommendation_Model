from flask import Flask, render_template, request
import pickle
import os

app = Flask(__name__)

model_path = os.path.join('model', 'svd_model.pkl')
with open(model_path, 'rb') as model_file:
    model = pickle.load(model_file)
    
# Dummy data for user and product IDs
users = list(range(1, 1001))
products = list(range(1, 501))

@app.route('/')
def index():
    return render_template('index.html', users=users, products=products)

@app.route('/recommend', methods = ['POST'])
def recommend():
    uder_id = int(request.form['user_id'])
    product_id = int(request.form['product_id'])
    
    prediction = model.predict(uder_id, product_id)
    return render_template('result.html', user_id=uder_id, product_id=product_id, predicted_rating=prediction.est)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7860, debug=False)
