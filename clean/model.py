from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from itertools import chain
from preprocessing import preprocess_input






def train_model(data):
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(data['tokens'].apply(' '.join))
    y = list(chain(*data['labels']))
    model = MultinomialNB()
    model.fit(X, y)
    return model, vectorizer

def predict_variables(model, vectorizer, user_prompt):
    tokens = preprocess_input(user_prompt)
    X_prompt = vectorizer.transform([' '.join([' '.join(token) for token in tokens])])
    predicted_variables = model.predict(X_prompt)[0]
    word_variables = dict(zip(tokens, predicted_variables))
    return word_variables