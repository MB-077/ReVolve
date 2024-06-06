import pandas as pd
import ast
import nltk


def preprocess_dataset(csv_file):
    data = pd.read_csv(csv_file)
    data['tokens'] = data['Token_list'].apply(lambda x: ast.literal_eval(x))
    data['labels'] = data['Label_list'].apply(lambda x: ast.literal_eval(x))
    return data

def preprocess_input(text):
    tokens = nltk.word_tokenize(text)
    return tokens