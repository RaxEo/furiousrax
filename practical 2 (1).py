from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')
nltk.download('punkt')

data="This is a sample sentence, showing off the stop words filteration"

print("My text is....")
print(data)
stopwords1=set(stopwords.words('English'))
print("list of stopwords are.....")
print(stopwords1)
words=word_tokenize(data)
wordsfiltered=[]
for w in words:
           if w not in stopwords1:
                      wordsfiltered.append(w)
print("List of filtered words which are not stopwords \n")
print(wordsfiltered)

