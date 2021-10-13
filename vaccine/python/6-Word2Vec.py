import pickle
import numpy as np
import pandas as pd
from gensim.models import Word2Vec
import matplotlib.pyplot as plt
import re
from tqdm import tqdm
from konlpy.tag import Komoran
tqdm.pandas()
pd.set_option('display.max_columns', None )
pd.set_option('display.max_rows', 50)
pd.set_option('display.width', None )
import warnings
warnings.filterwarnings('ignore')


def tokenize(data):
    """

    (1) best_answers_reduced : 단어의 길이가 2이상인 명사, 형용사, 외국어, 감탄사, 부사, 관형사, 동사 만 수집
    """
    tokenizer = Komoran()
    data= data.drop_duplicates('best_answers')
    print(data.shape)
    def is_not_blank(s):   return bool(s and not s.isspace())
    def reduce(x):
        # print(x)
        x= x.replace(r'https://\w+','').replace('\t','').replace('\n','').replace('.', '').replace(',','').replace("'","").replace('·', ' ').replace('=','').replace('[','').replace(']','')
        x = x.replace('newstistorycom', '').replace('msitenavercom', '').replace('dingdotistorycom', '')
        if is_not_blank(x) == False:  return False
        tagged = tokenizer.pos(x)
        nouns=[]
        l =  ['NN', 'NNG' , 'NNP', # 명사, 보통명사, 고유 명사
               'VA', 'VV', 'VX' #형용사, 동사
                'XR', 'SL','NA' #어근/ 외국어,  감정 / 분리안된 단어들
            ]
        # print(tagged)
        for s,t in tagged:
            if t in l:
                if t in ['VA','VV','VX']:  s+='다'
                if t in ['XR'] : s+= '하다'
                if s == '아스트라' : s+='제네카'
                if (s=='모') and (t == 'NNG') : s+='더나'
                if (s != '카') and (s!= '안녕하세요')\
                        and (s!= '하다')and (s!= '있다')\
                        and (s!= '없다') and (s!= '되다'): nouns.append(s)
        # print(nouns)
        return nouns

    data['best_answers_reduced']= data['best_answers'].progress_apply(lambda x: reduce(x))

    print(data[['best_answers', 'best_answers_reduced']].head(50))
    data =data[data['best_answers_reduced']!=False]
    data.to_csv('1014_tokenized_best_answers.csv', index=False,  encoding='utf-8-sig')

    return data

def w2v(data,i) :
    # print(data['best_answers_reduced'].tolist())
    model = Word2Vec(data['best_answers_reduced'].tolist(), size = 300, window = 5, min_count = 100, workers = 3 , sg=1, iter = 5, negative = 5)
    print(model.wv.most_similar("백신"))
    print('saving ', str(i),'th model ')
    model.save("./word2vec_naver_"+str(i)+"_th.model")


def get_filtered_df():
    for i in range(1,8):
        '''
        load model - get 300 similar word  
        output : data frame for 50 similar words with "vaccine" by each topic 
        '''

        with open("./word2vec_naver_"+str(i)+"_th.model", 'rb') as f: model = pickle.load(f)

        def get_simlist(sim_list, name):
            df = pd.DataFrame(sim_list.items(), columns=['Word', 'Similarity'])
            df.to_csv('./word2vec_naver' + name + '.csv', index=False)

            return df

        def similar_words(model, keyword, topn, name):
            sim_list = model.wv.similar_by_vector(keyword, topn=topn, restrict_vocab=None)
            sim_list_dict = {word: sim for word, sim in sim_list}
            df = get_simlist(sim_list_dict, name)

            return df

        df = similar_words(model, '백신', 300, str(i) + "th df")
        print('similar words for ', str(i), 'data ')
        print(df)

        final_list = df

        with open('./word2vec_naver' + str(i) + 'f_list.pkl', 'wb') as f: pickle.dump(final_list, f)

def create_final_words_df():
    total_f_list = []
    for idx in range(1, 8):
        with open('./word2vec_naver' + str(idx) + 'f_list.pkl', 'rb') as f: f_list = pickle.load(f)
        print('topic_num : ',idx)
        print(f_list)
        if len(f_list) < 50:
            for _ in range(len(f_list), 50): f_list.append("-")
        else:  f_list = f_list[:50]

        total_f_list.append(f_list)
    dic = {1: 'side effects', 2: 'visiting overseas', 3: 'variant', 4: 'different vaccines', 5: 'government policy',
           6: 'vaccine appointment', 7: 'school/education'}
    df = pd.DataFrame(columns=dic.values(), index=range(50))
    for idx in range(1, 8):   df[dic[idx]] = total_f_list[idx-1]['Word']
    df.to_csv('N_top_50_words_2.csv', index=False, encoding='utf-8-sig')

    return df

if __name__ == "__main__" :
    # data = pd.read_csv('N_sentimental_final_result.csv')
    # print(data.head())
    # tokenize(data)
    data = pd.read_csv('1014_tokenized_best_answers.csv', converters={'best_answers_reduced': eval})
    print(data.head())
    print(data.shape) # (17078, 20)
    # for i in range(1,8):   w2v(data[data['topic']==i],i)
    # get_filtered_df()
    # df = create_final_words_df()
    # print(df)
    # print(data['topic'].value_counts(normalize=True))
    dd = pd.DataFrame(columns=['topic', 'answer'])
    for i, t in zip(range(1,8),['부작용', '면역', '개발','모더나','국민', '잔여', '청소년']):
        d= data.loc[data['topic'] ==i]
        for k in d[d['best_answers'].str.contains(t, regex=True, na=False)]['best_answers'].values:
            dd = dd.append({'topic': i , 'answer': k}, ignore_index=True)
    dd.to_csv('main-word-include.csv', index=False, encoding='utf-8-sig' )
