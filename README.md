# IA-STUDY

This repository contains projects and examples related to the study of Artificial Intelligence (AI) and Machine Learning (ML).

---

📌 **Purpose**

The IA-STUDY repository was created to learn and practice the basics of AI and ML through hands-on examples.  
Each folder focuses on a specific topic, with code implementations and documentation.

---

📂 **Repository Structure**

- **LinearRegression/**  
  `Example.py`: A simple linear regression example using dummy data.

- **DecisionTreeClassification/** (in progress)  
  `Example.py`: Example of classification using Decision Trees.  
  Includes visualization of the decision tree using `matplotlib`.  

(more examples will be added as the learning process continues)

---

📊 **Implemented Examples**

🔹 **Linear Regression** (`LinearRegression/Example.py`)  
This example demonstrates how to apply linear regression on a dummy dataset, predicting scores based on study hours.

**Libraries used:**  
- `numpy` → numerical operations  
- `pandas` → data handling  
- `matplotlib` → visualization  
- `scikit-learn` → linear regression model

**Steps:**  
1. Create dummy data (study hours × scores).  
2. Train a linear regression model.  
3. Plot real data points and the fitted regression line.  
4. Display the coefficient (slope) and intercept.  

---

🔹 **Decision Tree Classification** (`DecisionTreeClassification/Example.py`)  
This example demonstrates how to classify data using a **Decision Tree** and visualize the tree using `matplotlib`.  

**Libraries used:**  
- `pandas` → data handling  
- `scikit-learn` → decision tree classifier and data splitting  
- `matplotlib` → tree visualization

**Steps:**  
1. Load the Pima Indians Diabetes dataset.  
2. Split the dataset into training and test sets.  
3. Train a Decision Tree Classifier.  
4. Evaluate the model accuracy.  
5. Visualize the decision tree structure.  

---

▶️ **How to Run**

1. Make sure you have Python 3.x installed.  
2. Install the required dependencies:

```bash
    pip install numpy pandas matplotlib scikit-learn
```


```bash
    python Example.py
```