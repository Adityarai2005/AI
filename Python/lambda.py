""" Important for NLP """
#text preprocessing 
# a common use case is to preprocess text data by transforming it to suitable text
texts=["Hello World!","This is a special text.","python is good for DS!"]
cleaned_text=list(map(lambda x:x.lower().replace('!','').replace('.',''),texts))
print(cleaned_text)
