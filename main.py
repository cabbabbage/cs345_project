import os
import importlib.util
from tqdm import tqdm
import tkinter as tk
from tkinter import filedialog
from add_feature import AddFeature 
import string
import pandas as pd
import numpy as np
from sklearn import feature_extraction, pipeline, metrics
from sklearn.ensemble import RandomForestClassifier
import pickle
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

def select_csv_file():

    return "/s/bach/g/under/rollo/cs345/semester_project/final_train.csv"


def get_features():
    features = []
    feature_dir = 'feature_extraction'
    pos_tags = {
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

    for filename in os.listdir(feature_dir):
        if filename.endswith('.py') and filename != '__init__.py':
            module_name = filename[:-3]
            spec = importlib.util.spec_from_file_location(module_name, os.path.join(feature_dir, filename))
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            if filename == 'POS.py':
                for pos_tag in pos_tags.keys():
                    pos_counter_instance = module.POS(pos_tag)
                    features.append(pos_counter_instance)
            else:
                feature_class = getattr(module, module_name.capitalize())
                features.append(feature_class())

    return features

def main():
    csv_path = select_csv_file()
    features = get_features()
    add_feature = AddFeature(csv_path)
    with open(csv_path, 'r', encoding='utf-8') as file:
        total_lines = sum(1 for line in file) - 1  

    total_progress = len(features) * total_lines

    with tqdm(total=total_progress, desc="Total Progress", unit="line") as progress_bar:
        for feature in features:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"Processing feature: {feature.name}")
            add_feature.add(feature, feature.name)
            progress_bar.update(total_lines)  
    


if __name__ == "__main__":
    main()
