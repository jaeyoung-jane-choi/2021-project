

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
from top2vec import Top2Vec
from konlpy.tag import Okt, Kkma, Komoran, Mecab



def preprocess():
    data = pd.read_csv('./0913_tokenized_data.csv', converters={'question_reduced': eval})
    # print(data.shape) #(18204, 13)
    data['question_tokenized']= data['question_reduced'].apply(lambda x: ' '.join(x))
    print(data.head())

    return data

def TopicModeling(data):
    ll= data["question_tokenized"].to_numpy()
    np.random.seed(2021)
    # model = Top2Vec(documents=ll ,# embedding_model='universal-sentence-encoder-multilingual',
    #                 speed="deep-learn", workers= 4   ) #use_embedding_model_tokenizer=True
    # model.save('1004_tokenized_model.h5')
    model = Top2Vec.load('1003_tokenized_model.h5') #234 topic
    return model

def Inference(model):
    # Inference
    topic_sizes, topic_nums = model.get_topic_sizes()
    print(topic_sizes, topic_nums) #234 topic
    d= pd.DataFrame(columns=['Topic_num', 'Top_50_words', 'size'])


    #print out 5 documents per topic
    for i in range(len(topic_nums)):
        # documents, document_scores, document_ids = model.search_documents_by_topic(topic_num=i, num_docs=5)
        # print('Topic number: ', str(i))
        # print( )
        # for doc, score, doc_id in zip(documents, document_scores, document_ids):
            # print(f"Document: {doc_id}, Score: {score}")
            # print("-----------")
            # print(doc)
            # print("-----------")
            # print()

        #print out top 50 topic words for each topic
        topic_words, word_scores, t = model.get_topics()

        d= d.append({'Topic_num': i, 'Top_50_words': topic_words[i], 'size': len(t)},ignore_index=True)
    print(d)
    d.to_csv('N_234_topics_top2vec.csv', index=False,  encoding='utf-8-sig')

    #word cloud for topics
    # topic_words, word_scores, topic_nums = model.get_topics()
    # print(topic_words, word_scores, topic_nums)
    # for topic in topic_nums:
    #     print(topic)
    #     word_score_dict = dict(zip(topic_words[topic],  word_scores[topic]))
    #     print(word_score_dict)
    #     plt.figure(figsize=(16, 4),  dpi=200)
    #     plt.axis("off")
    #     plt.imshow( wordcloud.WordCloud(width=1600, height=400,
    #                   background_color='black').generate_from_frequencies(word_score_dict))
    #     plt.title("Topic " + str(topic), loc='left', fontsize=25, pad=20)

    # for topic in topic_nums :
    #     model.generate_topic_wordcloud(topic, background_color="black")


def keyword_split(model,data):
    data['topic'] = -1
    data['topic_prob'] = -1
    keywordlist = [['요양','보건', '종사자' ],
                   ['해외여행', '입국', '가다', '해외'],
                   ['변이', '바이러스'], ['화이자', '얀센', '아스트라제네카'],
                   ['문재인', '대통령', '승인'], ['복용', '먹다', '근육통', '수술', '미열'],
                   ['접종', '신청', '대상자'],
                   ['수능', '학교', '등교']]  # 추가 주제
    np.random.seed(2021)
    for r,k in enumerate(keywordlist):
        print(r, k)
        documents, document_scores, document_ids = model.search_documents_by_keywords(keywords=k, num_docs=18204)
        print(documents, document_scores, document_ids)
        for n, i in enumerate(document_ids):
            if data.loc[i,'topic'] == -1:
                # print('topic false but now is ', r)
                data.at[i,'topic'] = r
                data.at[i,'topic_prob'] = document_scores[n]
            else:
                if data.loc[i, 'topic_prob'] < document_scores[n] :
                    # if data.loc[i, 'topic'] == 0 : print('이전 확률보다 높기에,', data.loc[i, 'topic'],' 은 ' ,str(r), ' 로 주제 변경')
                    data.loc[i, 'topic'] = r
                    data.loc[i, 'topic_prob'] = document_scores[n]



    print(data.head())
    print(data[data['topic_prob'] <= 0 ].shape)
    data[data['topic_prob'] <= 0].to_csv('probability_under_zero.csv', index=False,  encoding='utf-8-sig')
    data = data[data['topic_prob'] > 0]
    print(data.shape)
    data.sort_values(by= ['date','page'], inplace=True)

    print(data['topic'].value_counts())
    data.to_csv('N_top2vec_classified_new.csv', index=False,  encoding='utf-8-sig')

if __name__ == "__main__":
    data =preprocess()
    model = TopicModeling(data)
    # Inference(model)
    keyword_split(model,data)
    # d= data.sample(n=300, replace =False, random_state = 2021)
    # d.to_csv('N_random_sample_300.csv', index=False,  encoding='utf-8-sig' )

