import pandas as pd

# Load the dataset
df = pd.read_csv('/content/WA_Fn-UseC_-HR-Employee-Attrition.csv')

# Preview the data
df.head()

# A. Drop irrelevant or constant columns
df.drop(columns=[
    'EmployeeCount',    # Constant = 1
    'EmployeeNumber',   # Just an ID
    'Over18',           # Constant = 'Y'
    'StandardHours'     # Constant = 80
], inplace=True)

# B. Encode binary fields for modeling
df['Attrition_Flag'] = df['Attrition'].map({'Yes': 1, 'No': 0})
df['Overtime_Flag'] = df['OverTime'].map({'Yes': 1, 'No': 0})

# C. Create tenure bands
def tenure_band(years):
    if years <= 2:
        return '0–2 yrs'
    elif years <= 6:
        return '3–6 yrs'
    else:
        return '7+ yrs'

df['Tenure_Band'] = df['YearsAtCompany'].apply(tenure_band)

# D. Preview the updates
df[['Attrition', 'Attrition_Flag', 'OverTime', 'Overtime_Flag', 'YearsAtCompany', 'Tenure_Band']].head()

# Save cleaned version to CSV
df.to_csv("employee_attrition_cleaned.csv", index=False)

# Optional: download it locally
from google.colab import files
files.download("employee_attrition_cleaned.csv")

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix

# Select features and target
features = ['Age', 'DailyRate', 'DistanceFromHome', 'Overtime_Flag', 'YearsAtCompany']
X = df[features]
y = df['Attrition_Flag']

# Split the data (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LogisticRegression()
model.fit(X_train, y_train)

# Predict on test set
y_pred = model.predict(X_test)

# Evaluate performance
print("✅ Model Evaluation:\n")
print(confusion_matrix(y_test, y_pred))
print("\n", classification_report(y_test, y_pred))

# Save cleaned dataset to CSV
df.to_csv('employee_attrition_cleaned.csv', index=False)

# Download it from Colab to your local machine
from google.colab import files
files.download('employee_attrition_cleaned.csv')
