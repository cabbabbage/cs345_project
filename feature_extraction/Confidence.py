import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

class Confidence:
    def __init__(self):
        self.name = "Confidence"
         
        self.insecure_words = [
            "maybe", "possibly", "could", "might", "perhaps", "suggests",
            "probably", "may", "suppose", "assume", "presume", "can", "believe", "think", "ought"
  
        ]

    def get(self, text):
        sentences = sent_tokenize(text)
        total_sentences = len(sentences)
        confident_sentences = 0

        for sentence in sentences:
             
            words = word_tokenize(sentence.lower())
             
            if not any(word in self.insecure_words for word in words):
                confident_sentences += 1

         
        confident_percentage = confident_sentences / total_sentences if total_sentences > 0 else 0

        return confident_percentage

