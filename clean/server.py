import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
import json
from flask import Flask, request, jsonify

# Load the dataset
file_path = 'materiallist.csv'
data = pd.read_csv(file_path)

# Preprocess the data to ensure the correct format
data['Token_list'] = data['Token_list'].astype(str)
data['Label_list'] = data['Label_list'].astype(str)

# Use the correct column names
X = data['Token_list']
y = data['Label_list']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a pipeline with a text vectorizer and a classifier
pipeline = make_pipeline(CountVectorizer(), LogisticRegression())

# Train the model
pipeline.fit(X_train, y_train)

# Evaluate the model
print(f"Model accuracy: {pipeline.score(X_test, y_test)}")

# Define functions to parse prompts and convert to JSON
def parse_prompt(prompt):
    # Predict the label list from the prompt
    predicted_label = pipeline.predict([prompt])[0]
    return predicted_label

def convert_to_json(label):
    # Split the label string into a list
    labels_list = label.strip("()").replace("'", "").split(", ")
    json_data = json.dumps({"objects": labels_list}, indent=4)
    return json_data

# Set up the Flask server
app = Flask(__name__)

@app.route('/parse', methods=['POST'])
def parse():
    data = request.get_json()
    prompt = data['prompt']
    predicted_label = parse_prompt(prompt)
    json_result = convert_to_json(predicted_label)
    return jsonify(json.loads(json_result))

if __name__ == '__main__':
    app.run(debug=True)
