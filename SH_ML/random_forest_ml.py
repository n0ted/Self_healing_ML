import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

# Load the data
df = pd.read_csv('c:/Users/Lenovo/Downloads/SelfHealingScript/DATASET/elements.csv')
test = pd.read_csv('c:/Users/Lenovo/Downloads/SelfHealingScript/DATASET/test.csv')

# Fill NaN values. Instead of 'None', use a neutral value like -1 for numerical columns or a specific string for categorical columns.
# This part might need customization based on your data's actual structure.
for column in df.columns:
    if df[column].dtype == 'object':
        # For object columns
        df[column] = df[column].fillna('None')
        test[column] = test[column].fillna('None')
    else:
        # For non-object columns
        df[column] = df[column].fillna(-1)
        test[column] = test[column].fillna(-1)

# Convert categorical variables into dummy/indicator variables for both training and test sets
X = pd.get_dummies(df.drop(['element'], axis=1), drop_first=True)
test_processed = pd.get_dummies(test, drop_first=True)

# Align test data columns with training data
test_processed = test_processed.reindex(columns=X.columns, fill_value=0)

# Encode the target variable
le = LabelEncoder()
y = le.fit_transform(df['element'])

# Split the training data for validation
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the Random Forest model
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)

# Predict on the test data
predictions = rf.predict(test_processed)

# Decode the predictions back to original labels
decoded_predictions = le.inverse_transform(predictions)

# Optionally, validate the model
val_predictions = rf.predict(X_val)
print(f'Validation Accuracy: {accuracy_score(y_val, val_predictions)}')

# Display predictions
for i, pred in enumerate(decoded_predictions):
    print(f'Predicted element for record {i}: {pred}')

joblib.dump(rf, 'random_forest_model.pkl')
