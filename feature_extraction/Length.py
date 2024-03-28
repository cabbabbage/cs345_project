class Length:
    def __init__(self):
        self.name = "Length"
        pass

    def get(self, text):
        length = len(text.split())
        print(str(length) + " " + text)
        return length 