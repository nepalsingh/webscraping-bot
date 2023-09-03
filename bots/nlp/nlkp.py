from nltk.stem import WordNetLemmatizer, word_tokenize
import nltk

nltk.download('punkt')
nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()

def tokenize(text):
    return word_tokenize(text)

def lemmatize(text):
    return [lemmatizer.lemmatize(word) for word in tokenize(text)]

def preprocess(text):
    return lemmatize(text.lower())

if __name__ == '__main__':
    text = 'This is a test'
    print(preprocess(text))
