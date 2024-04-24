 
from textblob import TextBlob


class Subjectivity:
    def __init__(self):
        self.name = "Subjectivity"
         
    
    def get(self, text):
        testimonial = TextBlob(text)
        return testimonial.subjectivity
