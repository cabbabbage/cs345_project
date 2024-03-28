import csv
from tqdm import tqdm
import os

class AddFeature:
    def __init__(self, csv_path, reanalyze=False):
        self.csv_path = csv_path
        self.reanalyze = reanalyze
        self._validate_csv_format()

    def _validate_csv_format(self):
        with open(self.csv_path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            first_line = next(reader)
            if first_line[0] != "text" or first_line[-1] != "label":
                raise ValueError("CSV invalid format. First entry should be 'text' and last entry should be 'label'.")

    # Inside AddFeature class in add_feature.py
    def add(self, feature, title, progress_bar):
        
        with open(self.csv_path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            lines = list(reader)

        new_header = lines[0]
        f_prog = tqdm(total=len(lines) - 1, desc="Extracting line " + title, unit="line")
        if title in new_header:
            if self.reanalyze:
                title_index = new_header.index(title)
                for line in lines[1:]:  # Start from 1 to skip header
                    del line[title_index]
                new_header = lines[0]
            else:
                return

        new_header.insert(-1, title)

        with open(self.csv_path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(new_header)

            for line in lines[1:]:  # Skip header
                text = line[0]
                new_column_value = feature.get(text)
                line.insert(-1, new_column_value)
                writer.writerow(line)
                progress_bar.update(10)  
                f_prog.update(1)
            f_prog.close

