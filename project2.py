from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

iris = load_iris()

X = iris.data
y = iris.target

print("Dataset Shape:", X.shape)
print("Features:", iris.feature_names)
print("Classes:", iris.target_names)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = DecisionTreeClassifier(random_state=42)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("\nTraining Data:", len(X_train))
print("Testing Data:", len(X_test))
print("Accuracy:", accuracy)
print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=iris.target_names))

sample = [[5.1, 3.5, 1.4, 0.2]]
prediction = model.predict(sample)

print("New Data:", sample)
print("Predicted Class:", iris.target_names[prediction[0]])