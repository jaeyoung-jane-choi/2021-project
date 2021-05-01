# goal: 유저 클릭 히스토리를 바탕으로 광고 전환 (확률을 예측하는 모델)


import pandas as pd
import tarfile
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.preprocessing import MinMaxScaler



# unzip the datafile
# tar = tarfile.open("/Users/janechoi/PycharmProjects/LINEPLUS/Criteo_Conversion_Search_3.tar.gz", "r:gz")
# tar.extractall('./FILE')
# tar.close()

# Create train & test dataframe
path = '/Users/janechoi/PycharmProjects/LINEPLUS/FILE/Criteo_Conversion_Search/CriteoSearchData'

train = pd.read_table(path, header = None, nrows= 1000000)
test = pd.read_table(path, header = None, skiprows= (1, 1000000), nrows = 500000)

# Target label 은 데이터 세트의 첫번째 컬럼을 사용합니다.(0번째)
train = train.iloc[:,[0]+list(range(3,23)) ]
test = test.iloc[:,[0]+list(range(3,23)) ]

train.to_csv('/Users/janechoi/PycharmProjects/LINEPLUS/FINALDATA/train.csv', index= False )
test.to_csv('/Users/janechoi/PycharmProjects/LINEPLUS/FINALDATA/test.csv', index= False )
print(train.shape)
print(test.shape)

#Load Dataset
train = pd.read_csv('/Users/janechoi/PycharmProjects/LINEPLUS/FINALDATA/train.csv')
test = pd.read_csv('/Users/janechoi/PycharmProjects/LINEPLUS/FINALDATA/test.csv')
print(train.shape) #(1000000, 21) -> Feature :20
print(test.shape) #(500000, 21) -> Feature :20
print(train.describe())
print(train.info())
# total_df = pd.concat([train,test],axis= 0 )
# total_df.to_csv('total_df.csv', index=False )

#SALES : SUPER!!  UNBALANCED
print(train.iloc[:,0].value_counts()) # 0 : 889930 , 1: 110070
print(test.iloc[:,0].value_counts()) # 445679, 54321

for i in range(len(train.columns)) :
 if i not in [0,1,2,3]: #these columns are integers
  tr = len(train.iloc[:, i].value_counts())
  te = len(test.iloc[:, i].value_counts())
  print('TRAIN column',str(i), ' : ', str(tr))
  print('TEST column',str(i), ' : ', str(te))
  if tr == te :
   print('The Column ', str(i), 'has the same count for train&test')

print(train.iloc[:, 9].unique())
print(test.iloc[:, 9].unique())
print(sorted(test.iloc[:, 9].unique()) == sorted(train.iloc[:, 9].unique())) #SAME VALUES

#I will only use columns [0,1,2,3,9]

print(train.iloc[:, 1])
print(test.iloc[:, 1]) #time stamp - can't find pattern -> NOT USE


#I will only use columns [2,3,9] / [0] -> SALES

print(train.iloc[:, 2])
print(test.iloc[:, 2])


print(train.iloc[:, 3])
print(test.iloc[:, 3])

#CREATE NEW DATASET
train_df = train.iloc[:,[0,2,3,9]]
train_df.columns = ['Sales', 'A','B','C']

test_df = test.iloc[:,[0, 2,3,9]]
test_df.columns = ['Sales', 'A','B','C']


#-1 means it is missing value -> Lets look into the columns
print(train_df.describe())
print(test_df.describe())

target_1 = train_df[train_df.iloc[:,0] == 1]
target_0 = train_df[train_df.iloc[:,0] == 0]

print(target_0.describe())
print(target_1.describe())

#COLUMN 1 : look at distribution for each sales

sns.displot(train_df[train_df.iloc[:,0] == 0].iloc[:,1], color = 'red' ,label = 'target-0'  )
plt.xlim(-1, 100)
plt.legend(title="Sales")
plt.show()

sns.displot(train_df[train_df.iloc[:,0] == 1].iloc[:,1], color = 'blue',label = 'target-1' )
plt.xlim(-1, 100)
plt.legend(title="Sales")
plt.show()

#lets see the stats w/o -1
col01 = target_0[target_0.iloc[:,1] != -1 ]
col11 = target_1[target_1.iloc[:,1] != -1 ]

print(col01.describe())
print(col11.describe())

#can't use each target's mean for imputation due to target leak




#FINAL DATASET
#convert categorical into dummy vars

df = pd.concat([train_df, test_df], axis = 0 )
df.to_csv('/Users/janechoi/PycharmProjects/LINEPLUS/FINALDATA/df.csv', index=False )


df = pd.read_csv('/Users/janechoi/PycharmProjects/LINEPLUS/FINALDATA/df.csv')
df = pd.get_dummies(df, columns = ['C'])
df_x = df.iloc[:,1:]
x = pd.DataFrame(MinMaxScaler().fit_transform(df_x), index=df_x.index, columns=df_x.columns)
df_y = df[['Sales']]

df_final = pd.concat([df_x,df_y], axis= 1 )
df_final.to_csv('/Users/janechoi/PycharmProjects/LINEPLUS/FINALDATA/df_final.csv', index=False )

train_x = x.iloc[:100000,:]
train_y = df_y.iloc[:100000,0]
test_x = x.iloc[100000:,:]
test_y = df_y.iloc[100000:,0]

print(train_x.shape)
print(train_y.shape)
print(test_x.shape)
print(test_y.shape)


#MODELING :: LR
clf = LogisticRegression(max_iter=5000, random_state = 2021 )
clf.fit(train_x, train_y)

y_train_pred = clf.predict(train_x)
y_test_pred = clf.predict(test_x)


roc_auc_train = metrics.roc_auc_score(train_y, y_train_pred)
roc_auc_test = metrics.roc_auc_score(test_y, y_test_pred)

print('TRAIN ROC AUC SCORE :', str(roc_auc_train))
print('TEST ROC AUC SCORE :', str(roc_auc_test))

# TRAIN ROC AUC SCORE : 0.5024163568773234
# TEST ROC AUC SCORE : 0.502222858667847