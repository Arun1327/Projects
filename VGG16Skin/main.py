#importing libraries
import numpy as np
import os

#import flask
from flask import Flask,app,request,render_template
from flask import Flask, request,render_template

#tensorflow  models importing
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.inception_v3 import preprocess_input
    
#loading the trained model
modeln=load_model(r'vgg16final.h5')

app = Flask(__name__)
#default home page or route

#flask routes redirecting to pages on request
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/Dermatalogist')
def teahome():
    return render_template('Dermatalogist.html')

@app.route('/Predict')
def teapred():
    return render_template('predict.html')


#using GETPOST methods to get requestand give a response
@app.route('/Predict',methods=['GET','POST'])


# code to detect the type of disease found in the leaf image uploaded
@app.route('/Predict', methods=['GET', 'POST'])
def nres():
    if request.method == 'POST':
        try:
            f = request.files['image']
            
            # Check if an image was uploaded
            if not f:
                raise Exception("No image uploaded")
            
            basepath = os.path.dirname(__file__)
            filepath = os.path.join(basepath, 'uploads', f.filename)
            f.save(filepath)
            
            img = image.load_img(filepath, target_size=(224, 224))
            x = image.img_to_array(img)
            x = np.expand_dims(x, axis=0)
            img_data = preprocess_input(x)
            prediction = np.argmax(modeln.predict(img_data))
            
            index = ['Cellulitis', 'Impetigo', 'Athlete Foot', 'Nail Fungus', 'Ringworm', 'Cutaneous Larva Migrans', 'ChickenPox', 'Shingles']
            nresult = str(index[prediction])
            
            return render_template('predict.html', prediction=nresult)
        
        except Exception as e:
            error_message = str(e)
            return render_template('predict.html', prediction="Error: " + error_message)
    
    # Handle GET request or any other methods
    return render_template('predict.html')

    
#running the app
if __name__=="__main__":
    app.run(debug=True,port=8080)
    