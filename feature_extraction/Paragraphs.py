class Paragraphs:
    def __init__(self):
        self.name = "Paragraphs"
    
    def get(self, text):
         
        paragraphs = text.split('\n')
         
        paragraphs = [p for p in paragraphs if p.strip() != '']
        return len(paragraphs)
