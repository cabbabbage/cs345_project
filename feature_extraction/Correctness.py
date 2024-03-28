 
 

import language_tool_python

class Correctness:
    def __init__(self):
        self.name = "TextCorrectness"
         
        self.tool = language_tool_python.LanguageTool('en-US')
    
    def get(self, text):
         
        matches = self.tool.check(text)
        errors = len(matches)
        
         
        words = text.split()
        total_words = len(words)
        
        if total_words == 0:   
            return 1.0
        
         
         
         
        correctness = 1 - errors / total_words
        
         
        correctness = max(0.0, min(correctness, 1.0))
        
        return correctness
