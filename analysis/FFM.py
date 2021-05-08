

import pandas as pd
import xlearn as xl
from tqdm import tqdm
import pickle


def create_ffm(savepath, datapath, task, type ='csv' , catecodes = {}):
    """
    FORMAT >  label field1:feat1:val1 field2:feat2:val2

    :param savepath: loc to save the ffm txt file
    :param datapath: loc of org data
    :param task: train, test ...
    :param catecodes: dict
    :return: catecodes
    """

    def convert_to_ffm(path, df, name, numerics, categories, features, catcodes={}):
        currentcode = len(numerics)
        catdict = {}

        # Flagging categorical and numerical fields
        for x in numerics:
            catdict[x] = 0
        for x in categories:
            catdict[x] = 1

        nrows = df.shape[0]
        ncolumns = len(features)
        with open(path + str(name) + "_ffm.txt", "w") as text_file:

            # Looping over rows to convert each row to libffm format
            for n, r in tqdm(enumerate(range(nrows))):
                datastring = ""
                datarow = df.iloc[r].to_dict()
                datastring += str(int(datarow['SALE']))

                # For numerical fields, we are creating a dummy field here
                for i, x in enumerate(catdict.keys()):
                    if (catdict[x] == 0):
                        datastring = datastring + " " + str(i) + ":" + str(i) + ":" + str(datarow[x])
                    else:

                        # For a new field appearing in a training example
                        if (x not in catcodes):
                            catcodes[x] = {}
                            currentcode += 1
                            catcodes[x][datarow[x]] = currentcode  # encoding the feature

                        # For already encoded fields
                        elif (datarow[x] not in catcodes[x]):
                            currentcode += 1
                            catcodes[x][datarow[x]] = currentcode  # encoding the feature

                        code = catcodes[x][datarow[x]]
                        datastring = datastring + " " + str(i) + ":" + str(int(code)) + ":1"

                datastring += '\n'
                text_file.write(datastring)

                if n % 1000000 == 0:
                    print(n)
                    with open(path + 'catcodes.pickle', 'wb') as fw:
                        pickle.dump(catcodes, fw)

            text_file.close()
            return catcodes

    colnames = ['SALE'] + [chr(c) for c in range(ord('A'), ord('V')+1)]
    if type == 'txt': df= pd.read_table(datapath,names=colnames )
    else: df = pd.read_csv(datapath,names=colnames )

    #variables
    num = ['D','E']
    cat = [chr(c) for c in range(ord('F') ,ord('V')+1)]
    fet = [chr(c) for c in range(ord('D'), ord('V')+1)]

    try:
        catcodes = convert_to_ffm(path=savepath, df=df, name=task, numerics=num, categories=cat,
                                  features=fet, catcodes=catcodes)
    except:
        catcodes = convert_to_ffm(path=savepath, df=df, name=task, numerics=num, categories=cat,
                                  features=fet, catcodes={})

    return catcodes


def ffm_train(savepath, datapath):
    """
    :param savepath:  path to save the TRAINED MODEL
    :param datapath: train_ffm.txt file location
    :return: TRAINED MODEL
    """
    #CREATE MODEL
    model = xl.create_ffm()

    #TRAIN MODEL WITH DATASET
    model.setTrain(datapath)

    param = {'task': 'binary', 'lr': 0.2, 'lambda': 0.002,
         'k': 3, 'epoch': 100, 'metric': 'auc', 'opt': 'adagrad'}
    #k : latent factor size


    model.fit(param=param, model_path= "/Users/janechoi/PycharmProjects/LINEPLUS/MODEL/model.out") #SAVE the MODEL

    # model.cv(param)# Cross-Validation으로도 학습 가능

    return model


def ffm_predict(task, model , datapath, savepath):
    """
    :param task : train or test
    :param model:  TRAINED MODEL
    :param datapath: path of ffm txt
    :param savepath : loc to save
    :return:
    """
    # Prediction 1: PROBABILITY
    model.setSigmoid()
    model.setTest(datapath)
    model.predict("/Users/janechoi/PycharmProjects/LINEPLUS/MODEL/model.out",
                  savepath+ str(task)+"_predictions_sigmoid.txt") #predictions 으로 예측 파일


    #PREDICTION 2 : LABELS
    ffm = xl.create_ffm()
    ffm.setPreModel("/Users/janechoi/PycharmProjects/LINEPLUS/MODEL/model.out")
    ffm.setSign()
    ffm.setTest(datapath)
    ffm.predict("/Users/janechoi/PycharmProjects/LINEPLUS/MODEL/model.out",
                  savepath+ str(task)+"_predictions_binary.txt")


def submission(path1,path2, savepath, task):
    """

    :param path1: binary label prediction file
    :param path2: probability prediction file
    :param savepath: path to save final dataset
    :param task: name to save  i.e train/test
    :return: None
    """

    # <Line Number>, <Target Label>, <Predicted Probability>
    b = pd.read_table(path1)
    s = pd.read_table(path2)
    df = pd.concat([b,s], axis= 1 )
    df.columns = [ 'Target Label', 'Predicted Probability']
    if name == 'train' : df['Line Number'] = [i for i in range(1,1000000)]
    else: df['Line Number'] = [i for i in range(1000001,1500000)]

    #save as
    df.to_csv(str(savepath)+str(task)+'.csv', index=False)
    df.to_csv(str(savepath) + str(task) + '_result.txt', index=False, sep= '\t')


if __name__ == '__main__':
    #loc to save models, txt files
    savepath = "/Users/janechoi/PycharmProjects/LINEPLUS/FINALDATA/"

    #loc to save final txt file
    subpath = '/Users/janechoi/PycharmProjects/LINEPLUS/SUB/'


    # 1. CREATE TXT FILES FOR BOTH TRAIN & TEST
    print('CREATING TXT FILES FOR FFM')
    catcodes = create_ffm(savepath=savepath, datapath=savepath+'train.csv', task = 'train')
    catcodes = create_ffm(savepath=savepath, datapath=savepath+'test.csv',catecodes=catecodes, task='test')

    with open(savepath + 'catcodes.pickle', 'wb') as fw:
        pickle.dump(catcodes, fw)

    # 2 START MODEL TRAINING FOR THESE DATASET : FFM MODEL
    # 2.1 TRAIN
    print("TRAINING FFM MODEL ON TRAIN DATA")
    ffm = ffm_train(savepath=savepath, datapath=savepath+"train_ffm.txt")

    # 2.2 PREDICTION
    print("PREDICTION FFM ON TRAIN & TEST ")
    ffm_predict(task = 'train' , model=ffm,datapath=savepath+"train_ffm.txt",savepath=savepath)
    ffm_predict(task='test', model = ffm, datapath =savepath+"test_ffm.txt", savepath=savepath)


    # CLEANING PREDICTIONS FOR SUBMISSION
    print("CREATING SUB FILES FOR TRAIN & TEST ")
    #TRAIN SUB TXT
    submission(path1= savepath+ 'train_predictions_binary.txt',
                path2= savepath+ 'train_predictions_sigmoid.txt',
                savepath = subpath,
                task ='train')
    #TEST SUB TXT
    submission(path1= savepath+'test_predictions_binary.txt',
                path2=savepath+'test_predictions_sigmoid.txt',
                savepath = subpath,
                task = 'test')

    print('END OF PROCESS')

