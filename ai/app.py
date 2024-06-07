from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Load the model, vectorizer, and label encoder
model = joblib.load('model.pkl')
vectorizer = joblib.load('vectorizer.pkl')
label_encoder = joblib.load('label_encoder.pkl')

@app.route('/tag', methods=['POST'])
def tag():
    prompt = request.json.get('prompt', '')
    tokens = prompt.split()  # Simple tokenization by splitting on whitespace
    X = vectorizer.transform(tokens)
    y_pred = model.predict(X)
    labels = label_encoder.inverse_transform(y_pred)
    
    # result = {token: label for token, label in zip(tokens, labels)}
    result = {label: token for token, label in zip(tokens, labels)}
    
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
