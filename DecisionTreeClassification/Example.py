# Load libraries
import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn import metrics
import matplotlib.pyplot as plt

# Column names for the dataset
col_names = ['pregnant', 'glucose', 'bp', 'skin', 'insulin', 'bmi', 'pedigree', 'age', 'label']

# Load dataset
pima = pd.read_csv("diabetes.csv", skiprows=1, header=None, names=col_names)

# Display dataset information
print("Dataset dimensions:", pima.shape)
print(pima.head())

# Split dataset into features and target variable
feature_cols = ['pregnant', 'insulin', 'bmi', 'age', 'glucose', 'bp', 'pedigree']
X = pima[feature_cols]   # Features
y = pima.label           # Target variable

# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=1
)  # 70% training and 30% test

# Create Decision Tree classifier object
clf = DecisionTreeClassifier()

# Train Decision Tree Classifier
clf = clf.fit(X_train, y_train)

# Predict the response for test dataset
y_pred = clf.predict(X_test)

# Model Accuracy
print("Accuracy:", metrics.accuracy_score(y_test, y_pred))

# Plot the decision tree
plt.figure(figsize=(20,10))  # Set the figure size
plot_tree(clf, 
          feature_names=feature_cols, 
          class_names=['No Diabetes','Diabetes'], 
          filled=True,  # Color nodes by class
          rounded=True)
plt.show()  # Display the tree
