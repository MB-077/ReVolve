import json
from flask import Flask, request, jsonify
from preprocessing import preprocess_dataset
from model import train_model, predict_variables

app = Flask(__name__)

# Load and preprocess the dataset
data = preprocess_dataset('materiallist.csv')
# Train the model
model, vectorizer = train_model(data)

@app.route('/sort_words', methods=['POST'])
def sort_words():
    user_prompt = request.json.get('user_prompt')
    if user_prompt:
        word_variables = predict_variables(model, vectorizer, user_prompt)
        json_data = json.dumps(word_variables)
        return jsonify({'sorted_words': json_data})
    else:
        return jsonify({'error': 'User prompt is required'}), 400

if __name__ == '__main__':
    app.run(debug=True)