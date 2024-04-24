import language_tool_python
import os
os.environ['JAVA_TOOL_OPTIONS'] = '-Xmx1024m -Xms512m'
class Correctness:
    def __init__(self, name="TextCorrectness"):
        self.name = name

    def get(self, text):
        tool = language_tool_python.LanguageTool('en-US')
        matches = tool.check(text)
        tool.close()
        errors = len(matches)
        words = text.split()
        total_words = len(words)

        if total_words == 0:
            return 1.0

        correctness = 1 - errors / total_words
        correctness = max(0.0, min(correctness, 1.0))
        return correctness
