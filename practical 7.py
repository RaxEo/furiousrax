from nltk.tokenize import word_tokenize
import numpy as np
import nltk

def process(file):
    raw=open (file).read()
    tokens=word_tokenize(raw)
    #count words
    count=nltk.defaultdict(int)
    for word in tokens:
        count[word]+=1
    print('file: ', file , count)
    return count;

def cos_sim(a,b):
    dot_product=np.dot(a,b)
    norm_a=np.linalg.norm(a)
    print('norm_a: ',norm_a)
    norm_b=np.linalg.norm(b)
    print('norm_b: ',norm_b)
    return dot_product/(norm_a * norm_b)

def getSimilarity(dict1,dict2):
    all_words_list=[]
    for key in dict1:
        all_words_list.append(key)
    for key in dict2:
        all_words_list.append(key)
    print('all_wors_list: ',all_words_list)
    all_words_list_size=len(all_words_list)

    v1=np.zeros(all_words_list_size,dtype=np.int)
    v2=np.zeros(all_words_list_size,dtype=np.int)
    i=0
    for  (key) in all_words_list:
        v1[i]=dict1.get(key,0)
        print('v1',v1)
        v2[i]=dict2.get(key,0)
        print('v2',v2)
        i=i+1
    return cos_sim(v1,v2)

if __name__ == '__main__':
    dict1=process("C:/Users/ITCS/Downloads/t1.txt")
    dict2=process("C:/Users/ITCS/Downloads/t2.txt")
    print("Similarity between two text documents",getSimilarity(dict1,dict2))
