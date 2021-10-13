

import pandas as pd
import time
import pickle
import matplotlib.pyplot as plt
import re
from tqdm import tqdm
import numpy as np
import seaborn as sns
tqdm.pandas()
pd.set_option('display.max_columns', None )
pd.set_option('display.max_rows', 50)
pd.set_option('display.width', None )
import warnings
warnings.filterwarnings('ignore')


from wordcloud import WordCloud
from collections import Counter
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification, TextClassificationPipeline
import dexplot as dxp

def load_data():
    data = pd.read_csv('./N_top2vec_classified_new.csv') #, converters={'best_answers': eval}

    tokenizer = AutoTokenizer.from_pretrained("jaehyeong/koelectra-base-v3-finetuned-generalized-sentiment-analysis")
    model = AutoModelForSequenceClassification.from_pretrained(  "jaehyeong/koelectra-base-v3-finetuned-generalized-sentiment-analysis")
    sentiment_classifier = TextClassificationPipeline(tokenizer=tokenizer, model=model)
    print(data.head())
    return data, sentiment_classifier, tokenizer



def senti_test(data, sentiment_classifier):
    d = data[data['topic'] == 7 ]
    print(d.head())
    answers = d["best_answers"].to_numpy()

    for idx, review in enumerate(answers[:10]):
        pred = sentiment_classifier(review)
        print(f'{review}\n>> {pred[0]}')
        # label 0 : negative review
        # label 1 : positive review
        #ex {'label': '1', 'score': 0.688380241394043}


def pos_neg_classify(data, sentiment_classifier, tokenizer):
    data['sentiment'] = -1
    data['score'] = -1
    cnt = 0
    for i in tqdm(range(1,8)): #1-7
        d = data[data['topic'] == i]['best_answers'].values
        ind = data[data['topic'] == i]['best_answers'].index
        for t, n in zip(d, ind):
            print(n,t)
            length = len(tokenizer.tokenize(t))
            print('tokenizer length is... ',length)
            if length > 510 :#max length is 512 so if text over 512 split text -- we need to add CLS/SEP so needs to be 2 less
                cnt +=1
                print('current text is...',tokenizer.tokenize(t) )
                l = (length - 510)//2
                tokens = tokenizer.tokenize(t)[l+1:length-l-1]
                print('the tokenized text should be..', tokens)
                print('now the length is..', len(tokens))

                sent = '' #rebuild text
                for tok in tokens:
                    if tok.startswith("##"):  sent += tok[2:]
                    else:  sent += " " + tok
                print('now the text is..', sent)
                t= sent
            else : pass

            pred= sentiment_classifier(t)
            # print(pred)
            data.loc[n, 'sentiment'] = pred[0]['label']
            data.loc[n, 'score'] = pred[0]['score']
            # print('org-text')
            # print(data.loc[n,'best_answers'])
            # print('sentiment-result')
            # print(data.loc[n, 'sentiment'])
        print(data[data['topic'] == i].head())
    return data ,cnt


def visualize_pos_neg(data):
    sns.set_theme(style="whitegrid")
    dic = {1:'side effects', 2: 'visiting overseas', 3: 'variant', 4: 'different vaccines', 5:'government policy', 6: 'vaccine appointment', 7:'school/education'}

    data['topic-label'] = data['topic'].apply(lambda x: dic[x])
    print(data.head())
    # sns.countplot(hue= 'sentiment', data=data, y='topic-label', palette=sns.diverging_palette(250, 15, s=75, l=40,  n=2, center="dark"))
    # plt.tight_layout()
    # plt.legend(loc='upper right',labels=['Negative', 'Positive'])
    # plt.xlabel("Count")
    # plt.ylabel("Topic")
    # plt.show()

    df1 = data.groupby('topic-label')['sentiment'].value_counts(normalize=True)
    df1 = df1.mul(100)
    df1 = df1.rename('percent').reset_index()
    print(df1)
    sns.catplot(y='topic-label', x='percent', hue='sentiment', kind='bar', legend =False, data=df1, palette=sns.diverging_palette(250, 15, s=75, l=40,  n=2, center="dark"))
    plt.tight_layout()
    # plt.legend(loc='upper right', labels=['Negative', 'Positive'])
    plt.xlabel("Percentage")
    plt.ylabel("Topic")
    plt.show()

    data.to_csv('N_sentimental_final_result.csv', index=False,  encoding='utf-8-sig')

    return data



if __name__ == "__main__":
    # data, sentiment_classifier ,tokenizer= load_data()
    # senti_test(data, sentiment_classifier)
    # data, cnt =pos_neg_classify(data, sentiment_classifier,tokenizer)
    # print('count of text which is longer than 512: ' , cnt )
    # print(data.head())
    # data.to_csv('N_sentimental_result.csv', index=False,  encoding='utf-8-sig')
    data = pd.read_csv('N_sentimental_result.csv')
    data = visualize_pos_neg(data)