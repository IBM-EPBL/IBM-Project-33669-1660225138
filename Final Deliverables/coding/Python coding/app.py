# -*- coding: utf-8 -*-
"""Build.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FuXQZLQKX6O3vp1z-iNvO4S1ESBU-JIK

**Bild Python code**

**Import Libraries**
"""


import requests



from flask import Flask,request, render_template
app=Flask(__name__,template_folder='templates')

@app.route('/',methods=['GET'])
def index():
    return render_template('Templetes/home.html')
@app.route('/home',methods=['GET'])
def about():
    return render_template('Templetes/home.html')
@app.route('/pred',methods=['GET'])
def page():
    return render_template('Templetes/upload.html')
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    print("[INFO] loading model...")
    input_features = [float(x) for x in request.form.values()]
    features_value = [input_features]
    print(features_value)
    
    features_name = ['homepage_featured', 'emailer_for_promotion', 'op_area', 'cuisine',
       'city_code', 'region_code', 'category']
    # NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
    API_KEY = "JoLEM-uzJudR-GHMBmljsuL3whjuctQTFJGib0hQKvuD" 
    token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey": 
    API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'}) 
    mltoken = token_response.json()["access_token"] 
    header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken} 
    # NOTE: manually define and pass the array(s) of values to be scored in the next line 
    payload_scoring = {"input_data": [{"values": features_value}]} 
    response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/c571791a-86a1-4ddf-94a6-904df13736e0/predictions?version=2022-11-19', json=payload_scoring, 
    headers={'Authorization': 'Bearer ' + mltoken}) 
    print("Scoring Endpoint") 
    print(response_scoring.json())
    pred = response_scoring.json()

    output=pred['predictions'][0]['values'][0][0]
    print(output)
    return render_template('upload.html', prediction_text=output)
    
if __name__ == '__main__':
      app.run()