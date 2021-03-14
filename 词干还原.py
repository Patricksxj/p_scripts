import re
def stem(phrase):
    return ''.join([re.findall('^(.*ss|.*?)(s)?$',word)[0][0].strip("'") for word in phrase.lower().split()])
result=stem('houses')
print(result,'\n')
print(re.findall('^(.*ss|.*?)(s)?$','houses'))



from nltk.stem.porter import PorterStemmer
stemmer=PorterStemmer()
words="dish washer's washed dishes"
result2=' '.join([stemmer.stem(w).strip("'") for w in words.split()])
print(result2,'\n')