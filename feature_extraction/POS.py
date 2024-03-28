import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
nltk.download('punkt')

class POS:
    def __init__(self, pos_filter):
        pos_names = {
            'NN': 'Noun',
            'VB': 'Verb',
            'JJ': 'Adjective',
            'RB': 'Adverb',
            'PRP': 'Pronoun',
            'DT': 'Determiner',
            'IN': 'Preposition',
            'CD': 'Number',
            'CC': 'Conjunction',
            'UH': 'Interjection'
        }
        
         
        self.name = pos_names.get(pos_filter, "Unknown POS")
        nltk.download('averaged_perceptron_tagger')
        self.pos_filter = pos_filter   

    def get(self, text):
        """
        Counts the occurrences of the specified part of speech in the text.

        Parameters:
        - text (str): The text to analyze.

        Returns:
        - int: The count of the specified part of speech in the text.
        """
         
        words = word_tokenize(text)
         
        pos_tags = pos_tag(words)
         
        pos_count = sum(1 for word, tag in pos_tags if tag.startswith(self.pos_filter))
        return pos_count/len(text)
