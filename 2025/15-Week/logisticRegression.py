from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = {
    "HoursStudied": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "ExamScore": [12, 25, 32, 40, 50, 55, 66, 72, 80, 90]
}

df = pd.DataFrame(data)
# Convert ExamScore to binary outcome: 1 if score >= 50, else 0
df["Passed"] = (df["ExamScore"] >= 50).astype(int)
X = df[["HoursStudied"]]
y = df["Passed"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LogisticRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)
print(f"Accuracy: {accuracy:.2f}")
print("Classification Report:")
print(classification_report(y_test, predictions))
print("Confusion Matrix:")
print(confusion_matrix(y_test, predictions))

x_sorted = np.linspace(0, 12, 100).reshape(-1, 1)
y_proba = model.predict_proba(x_sorted)[:, 1]

plt.scatter(X, y, color='blue', label='Actual Data')
plt.plot(x_sorted, y_proba, color='red', label='Logistic Regression Curve')
plt.xlabel('Hours Studied')
plt.ylabel('Passed (1) / Failed (0)')
plt.title('Hours Studied vs Exam Outcome')
plt.legend()
plt.show()
