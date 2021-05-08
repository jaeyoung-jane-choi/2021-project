

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from collections import defaultdict
from sklearn.preprocessing import LabelEncoder
import joblib
import pickle
from sklearn import metrics
import numpy as np

def read_data(dir,type='csv'):
    colnames = ['SALE'] + [chr(c) for c in range(ord('A'), ord('T') + 1)]
    if type == 'txt': df= pd.read_table(dir,names=colnames , sep ='\t')
    else:
        df = pd.read_csv(dir, header= 0)
        df.columns = colnames

    # numerical [1,2,3] -> [2,3] (1: doesn't have pattern: timestamp)
    # categorical : only use features where train& test both have
    #iloc 4, 9,15,16 -> 4,9,16
    #final : 2,3,4,9,16

    # print(sorted(test.iloc[:, 4].unique()) == sorted(train.iloc[:, 4].unique()))
    # print(sorted(test.iloc[:, 9].unique()) == sorted(train.iloc[:, 9].unique()))
    # print(sorted(test.iloc[:, 16].unique()) == sorted(train.iloc[:, 16].unique()))

    df = df.iloc[:,[0,2,3,4,9,16]]

    return df


def preprocess(df, task='test'):

    if task == 'test':
        with open('/Users/janechoi/PycharmProjects/LINEPLUS/MODEL/encoder.pickle', 'rb') as fr:
            encoder = pickle.load(fr)
    else: encoder = defaultdict(LabelEncoder)

    #Encode categorical features

    cat = ['D','I','P']
    df_cat = df[cat].apply(lambda x: encoder[x.name].fit_transform(x))

    df_x = df[['B','C']]
    df_x = pd.concat([df_x,df_cat], axis = 1 )

    #scale the variables
    scaler = StandardScaler()
    df_x = pd.DataFrame(scaler.fit_transform(df_x), index=df_x.index, columns=df_x.columns)

    y = df.iloc[:,0]

    #save encoder
    if task == 'train':
        with open('/Users/janechoi/PycharmProjects/LINEPLUS/MODEL/encoder.pickle', 'wb') as fw:
            pickle.dump(encoder, fw)

    return df_x,y

def train_LR(train_x, train_y):

    clf = LogisticRegression(max_iter=5000, random_state=2021, verbose=True)
    clf.fit(train_x, train_y)

    #save model
    joblib.dump(clf, '/Users/janechoi/PycharmProjects/LINEPLUS/MODEL/model.pkl')


def predict_LR(test_x,test_y, clf):

    pred_y= clf.predict(test_x)
    prob_y= clf.predict_proba(test_x)

    return pred_y, prob_y


def submission(pred_y,prob_y,subpath,task):
    df = pd.DataFrame(columns =['Target Label', 'Predicted Probability'])
    df['Target Label'] = pred_y
    df['Predicted Probability'] = np.max(prob_y, axis=1)
    if task == 'test_result' :
        df.index = df.index+1000001
    if task == 'train_result' :
        df.index =df.index+1

    df.to_csv(subpath+task+'.txt', sep ='\t')
    return df



if __name__ == '__main__':
    # loc to save models, txt files
    savepath = "/Users/janechoi/PycharmProjects/LINEPLUS/FINALDATA/"

    # loc to save final txt file
    subpath = '/Users/janechoi/PycharmProjects/LINEPLUS/SUB/'

    #read data
    train = read_data(savepath+'train.csv')
    test = read_data(savepath + 'test.csv')


    #Preprocess data
    train_x, train_y = preprocess(df= train, task = 'train')
    test_x, test_y = preprocess(df= test)

    #Train model
    train_LR(train_x, train_y)

    #Predict
    clf = joblib.load('/Users/janechoi/PycharmProjects/LINEPLUS/MODEL/model.pkl')
    test_pred_y, test_prob_y= predict_LR(test_x, test_y, clf)
    train_pred_y, train_prob_y= predict_LR(train_x, train_y,clf)

    #SUBMISSION
    submission(test_pred_y, test_prob_y, subpath= subpath, task='test_result')
    submission(train_pred_y, train_prob_y, subpath= subpath, task='train_result')




