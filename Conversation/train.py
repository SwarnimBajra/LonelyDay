import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# Load preprocessed data
X_train = np.load('X_train.npy', allow_pickle=True)
X_val = np.load('X_val.npy', allow_pickle=True)
X_test = np.load('X_test.npy', allow_pickle=True)

y_train = np.load('y_train.npy', allow_pickle=True)
y_val = np.load('y_val.npy', allow_pickle=True)
y_test = np.load('y_test.npy', allow_pickle=True)

# Convert texts to features using CountVectorizer
vectorizer = CountVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_val_vec = vectorizer.transform(X_val)
X_test_vec = vectorizer.transform(X_test)

# Train a Multinomial Naive Bayes classifier
classifier = MultinomialNB()
classifier.fit(X_train_vec, y_train)

# Predict on validation and test sets
val_predictions = classifier.predict(X_val_vec)
test_predictions = classifier.predict(X_test_vec)

# Evaluate the model
print("Validation Accuracy: ", accuracy_score(y_val, val_predictions))
print("Test Accuracy: ", accuracy_score(y_test, test_predictions))

# Print classification reports
print("Validation Classification Report: ")
print(classification_report(y_val, val_predictions))

print("Test Classification Report: ")
print(classification_report(y_test, test_predictions))
