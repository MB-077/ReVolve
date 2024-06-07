import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
import joblib

# Load the dataset from a CSV file
df = pd.read_csv('clean_tagged_data.csv')

# Flatten the Token_list and Label_list
tokens = []
labels = []

for i in range(len(df)):
    token_list = eval(df.iloc[i]['Token_list'])  # Use eval to convert string to tuple
    label_list = eval(df.iloc[i]['Label_list'])  # Use eval to convert string to tuple
    tokens.extend(token_list)
    labels.extend(label_list)

# Encode labels
le = LabelEncoder()
y = le.fit_transform(labels)

# Vectorize the tokens
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(tokens)

# Train a simple logistic regression model
model = LogisticRegression(max_iter=1000)
model.fit(X, y)

# Save the model and vectorizer
joblib.dump(model, 'model.pkl')
joblib.dump(vectorizer, 'vectorizer.pkl')
joblib.dump(le, 'label_encoder.pkl')
