import csv
from pathos.multiprocessing import ProcessingPool as Pool
import language_tool_python
import os
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor

# Set Java options for LanguageTool
os.environ['JAVA_TOOL_OPTIONS'] = '-Xmx1024m -Xms512m'


def process_line(line, feature):
    text = line[0]
    new_column_value = feature.get(text)
    line.insert(-1, new_column_value)
    return line


class AddFeature:
    def __init__(self, csv_path, reanalyze=True):
        self.csv_path = csv_path
        self.reanalyze = reanalyze
        self._validate_csv_format()
        self.tool = language_tool_python.LanguageTool('en-US')


    def get_text_correctness(self, line):
        text = line[0]
        matches = self.tool.check(text)
        errors = len(matches)
        words = text.split()
        total_words = len(words)
        if total_words == 0:
            return line
        correctness = 1 - errors / total_words
        line.insert(-1, max(0.0, min(correctness, 1.0)))
        return line

    def _validate_csv_format(self):
        with open(self.csv_path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            first_line = next(reader)
            if first_line[0] != "text" or first_line[-1] != "label":
                raise ValueError("CSV invalid format. First entry should be 'text' and last entry should be 'label'.")

    def add(self, feature, title):
        with open(self.csv_path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            lines = list(reader)

        if title in lines[0] and not self.reanalyze:
            return

        # Reanalyze existing data
        if title in lines[0]:
            title_index = lines[0].index(title)
            lines = [lines[0]] + [line[:title_index] + line[title_index+1:] for line in lines[1:]]

        lines[0].insert(-1, title)
        total_lines = len(lines) - 1
        if total_lines == 0:
            print("No data to process.")
            return

        processed_lines = [lines[0]]  # Start with the header

        if feature.name == "TextCorrectness":
            # Using threading for text correctness
            with ThreadPoolExecutor() as executor:
                results = list(tqdm(executor.map(self.get_text_correctness, lines[1:]), total=total_lines, desc="Correcting Text"))
                processed_lines += results
        else:
            # Parallel processing for other features
            with Pool() as pool:
                results = list(tqdm(pool.map(lambda line: process_line(line, feature), lines[1:]), total=total_lines, desc="Processing Features"))
                processed_lines += results

        with open(self.csv_path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(processed_lines)

        print(f'Total lines processed: {total_lines}')


