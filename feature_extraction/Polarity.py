 
from textblob import TextBlob


class Polarity:
    def __init__(self):
        self.name = "Polarity"
         
    def get(self, text):
        testimonial = TextBlob(text)
        return testimonial.polarity
