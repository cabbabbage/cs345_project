import nltk
from nltk import pos_tag
from nltk.tokenize import word_tokenize, sent_tokenize

class Passivevoice:
    def __init__(self, name="Passivevoice"):
        self.name = name

    def _is_passive(self, sentence):
        tagged = pos_tag(word_tokenize(sentence))
        to_be_verbs = ['is', 'was', 'were', 'are', 'been']
        passive_pattern = [(('VBD', 'VBN'), 'NNP'), (('VBD', 'VBN'), 'NN'), (('VBZ', 'VBN'), 'NNP'), (('VBZ', 'VBN'), 'NN')]

        for i in range(len(tagged) - 1):
            if tagged[i][0].lower() in to_be_verbs and tagged[i+1][1] == 'VBN':
                return True
        return False

    def get(self, text):
        sentences = sent_tokenize(text)
        if not sentences:
            return 0.0
        
        passive_sentences = sum(1 for sentence in sentences if self._is_passive(sentence))
        return passive_sentences / len(sentences)
