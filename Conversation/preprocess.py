import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

# Load datasets
train_df = pd.read_csv('train.csv')
val_df = pd.read_csv('validation.csv')
test_df = pd.read_csv('test.csv')

# Data Preprocessing
def preprocess_data(train_df, val_df, test_df):
    # Extracting relevant columns for inputs and labels
    # Ensure we're correctly joining the messages and context from the respective columns
    train_texts = []
    train_labels = []
    for idx, row in train_df.iterrows():
        text = f"{row['previous_utterance']} {row['free_messages']} {row['suggestions']}"
        train_texts.append(text)
        train_labels.append(row['personas'])

    val_texts = []
    val_labels = []
    for idx, row in val_df.iterrows():
        text = f"{row['previous_utterance']} {row['free_messages']} {row['suggestions']}"
        val_texts.append(text)
        val_labels.append(row['personas'])

    test_texts = []
    test_labels = []
    for idx, row in test_df.iterrows():
        text = f"{row['previous_utterance']} {row['free_messages']} {row['suggestions']}"
        test_texts.append(text)
        test_labels.append(row['personas'])

    # Ensure texts and labels have the same length
    print(f"Train texts length: {len(train_texts)} | Train labels length: {len(train_labels)}")
    print(f"Validation texts length: {len(val_texts)} | Validation labels length: {len(val_labels)}")
    print(f"Test texts length: {len(test_texts)} | Test labels length: {len(test_labels)}")

    # Split data into train, validation, and test sets
    train_texts, val_texts, train_labels, val_labels = train_test_split(train_texts, train_labels, test_size=0.2, random_state=42)
    val_texts, test_texts, val_labels, test_labels = train_test_split(val_texts, val_labels, test_size=0.5, random_state=42)

    # Save the data as numpy arrays
    np.save('X_train.npy', np.array(train_texts))
    np.save('X_val.npy', np.array(val_texts))
    np.save('X_test.npy', np.array(test_texts))
    np.save('y_train.npy', np.array(train_labels))
    np.save('y_val.npy', np.array(val_labels))
    np.save('y_test.npy', np.array(test_labels))

    print("Data preprocessing completed and saved.")

# Call preprocessing function
preprocess_data(train_df, val_df, test_df)
