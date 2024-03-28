import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize

class Sentences:
    def __init__(self):
        self.name = "Sentences"
    
    def get(self, text):
         
        sentences = sent_tokenize(text)
        return len(sentences)
