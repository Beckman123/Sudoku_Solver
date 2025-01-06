import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import pickle

# Load the dataset
file_path = "sudoku.csv"
df = pd.read_csv(file_path)

# Preprocess data
def preprocess_data(df):
    feat = []
    label = []

    for i in df['quizzes']:
        x = np.array([int(j) for j in i]).reshape((9, 9, 1))
        feat.append(x)

    feat = np.array(feat)
    feat = feat / 9
    feat -= 0.5

    for i in df['solutions']:
        x = np.array([int(j) for j in i]).reshape((81, 1)) - 1
        label.append(x)

    label = np.array(label)
    return feat, label

# Split data into training, validation, and test sets
def split_data(X, y):
    X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.2, random_state=42)
    X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)
    return X_train, X_val, X_test, y_train, y_val, y_test

# Preprocess the data
X, y = preprocess_data(df)

# Split into train, validation, and test sets
X_train, X_val, X_test, y_train, y_val, y_test = split_data(X, y)

# Check the shapes
print("Training data shape:", X_train.shape, y_train.shape)
print("Validation data shape:", X_val.shape, y_val.shape)
print("Test data shape:", X_test.shape, y_test.shape)

# Save the processed dataset for later use
processed_file_path = "processed_sudoku.pkl"
with open(processed_file_path, 'wb') as f:
    pickle.dump((X_train, X_val, X_test, y_train, y_val, y_test), f)
print(f"\nProcessed dataset saved to {processed_file_path}")
