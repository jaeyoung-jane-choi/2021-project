
from flask import Flask, render_template, request

import joblib
import pandas as pd
import os
import pickle
from LR import read_data, preprocess , predict_LR,submission


#FUNCTIONS NEEDED
#LOAD THE TRAINED MODEL


def load_model():
    global model
    model = joblib.load('/Users/janechoi/PycharmProjects/MODEL/model.pkl')



app = Flask(__name__)
#HOME URL
@app.route('/')
def home():
    # load_model()
    return '...Lets predict the Conversion Rate...'


#CVR UPLOAD
@app.route('/html')
def load():
    return render_template('cvr.html')


#CVR PREDICTION
@app.route('/get/cvr', methods = ['POST'] )
def getfile():
   if request.method == 'POST':

        #SAVE DATA FROM WEB
        PATH = "/Users/janechoi/PycharmProjects/FLASK/WEBDATA/"

        f = request.files['file']
        f.save(os.path.join(PATH,f.filename))

        NAME = str(f.filename).split('.txt')[0]

        #PREPROCESS INTO FFM TXT
        df= read_data(dir = PATH+NAME+'.txt', type='txt')
        df_x,y= preprocess(df)

        #MODEL PREDICTION
        pred_y, prob_y = predict_LR(df_x, y, clf=model)


        #SAVE SUB
        submission(pred_y, prob_y , subpath= PATH, task=NAME)

        #READ PREDICTIONS

        tx = pd.read_table(PATH+NAME+".txt")
        label = tx['Target Label']
        prob = tx['Predicted Probability']

        return render_template('result.html',label =label, prob = prob, zip=zip )



#RELOAD MODEL
@app.route('/update/model')
def reload():
    load_model()
    return '...reloaded the model..'

if __name__ == '__main__':
    load_model()
    app.run(debug= True)
