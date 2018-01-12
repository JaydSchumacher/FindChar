word_list = ['hello','world','my','name','is','Anna']
letters = set('m')

for words in word_list :
    if letters & set(words):
        print words