class Quotations:
    def __init__(self):
        self.name = "Quotations"
    
    def get(self, text):
         

         
        in_quotes_count = 0
         
        in_single_quotes = False
        in_double_quotes = False

        for char in text:
             
            if char == "\"" and not in_double_quotes:   
                in_single_quotes = not in_single_quotes
            elif char == '\"' and not in_single_quotes:   
                in_double_quotes = not in_double_quotes
            
             
            if in_single_quotes or in_double_quotes:
                in_quotes_count += 1

        total_chars = len(text)

         
        if total_chars > 0:
            percentage_in_quotes = in_quotes_count / total_chars
        else:
            percentage_in_quotes = 0   

        return percentage_in_quotes
