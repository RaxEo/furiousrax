import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
docs=['why hello there', 'omg hello pony', 'she went there? omg']
v= CountVectorizer()
x= v.fit_transform (docs) #transform in columnformat

df=pd.DataFrame (x. toarray (),columns=v.get_feature_names ())

#array rowformat and display in matrix

print (df)
