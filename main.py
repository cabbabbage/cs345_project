import os
import importlib.util
import tkinter as tk
from tkinter import filedialog

from tqdm import tqdm

from add_feature import AddFeature

def select_csv_file():
    root = tk.Tk()
    root.withdraw() 
    try:
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if not file_path:   
            file_path = "test.csv"
    except Exception as ex:
        file_path = "test.csv"
    return file_path

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
    add_feature = AddFeature(csv_path, True)
    features = get_features()
    
     
    progress_bar = tqdm(features, desc="Adding features", unit="feature")

    for feature in progress_bar:
        add_feature.add(feature, feature.name)
    os.system(csv_path)

if __name__ == "__main__":
    main()



