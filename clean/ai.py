import pandas as pd
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import json
from flask import Flask, request, jsonify

# Load the CSV file
data = pd.read_csv('materiallist.csv')

# Split the Token_list and Label_list columns
data['Token_list'] = data['Token_list'].apply(lambda x: eval(x))
data['Label_list'] = data['Label_list'].apply(lambda x: eval(x))

# Merge the Token_list and Label_list into a single list of tuples
data['tokens_and_labels'] = data.apply(lambda row: list(zip(row['Token_list'], row['Label_list'])), axis=1)

def preprocess_input(text):
    tokens = nltk.word_tokenize(text)
    return tokens

# Create a CountVectorizer object
vectorizer = CountVectorizer()

# Fit and transform the 'tokens_and_labels' column to create a token matrix
X = vectorizer.fit_transform(data['tokens_and_labels'].apply(lambda x: ' '.join([' '.join(token) for token in x])))

# Get the feature names (tokens)
token_names = vectorizer.get_feature_names_out()

# Convert the 'tokens_and_labels' column into a list of labels
y = data['tokens_and_labels'].apply(lambda x: [label for token, label in x]).tolist()

# Train a Naive Bayes classifier
model = MultinomialNB()
model.fit(X, y)

def sort_words_to_json(user_prompt):
    # Preprocess the user prompt
    tokens = preprocess_input(user_prompt)
    
    # Create a token matrix for the user prompt
    X_prompt = vectorizer.transform([' '.join([' '.join(token) for token in tokens])])
    
    # Get the predicted variables for the tokens
    predicted_variables = model.predict(X_prompt)[0]
    
    # Create a dictionary with tokens as keys and predicted variables as values
    word_variables = dict(zip(tokens, predicted_variables))
    
    # Convert the dictionary to JSON
    json_data = json.dumps(word_variables)
    
    return json_data

app = Flask(__name__)

@app.route('/sort_words', methods=['POST'])
def sort_words():
    user_prompt = request.json.get('user_prompt')
    if user_prompt:
        json_data = sort_words_to_json(user_prompt)
        return jsonify({'sorted_words': json_data})
    else:
        return jsonify({'error': 'User prompt is required'}), 400

if __name__ == '__main__':
    app.run(debug=True)