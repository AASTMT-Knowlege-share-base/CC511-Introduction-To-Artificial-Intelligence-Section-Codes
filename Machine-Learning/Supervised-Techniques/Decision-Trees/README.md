# Decision Trees: Overview

Decision Trees are a supervised machine learning technique used for both **classification** and **regression** tasks. They predict outcomes by splitting data into branches based on feature thresholds, forming a tree-like structure.

---

## Key Concepts

1. **Tree Structure**:
   - **Root Node**: Represents the entire dataset.
   - **Decision Nodes**: Intermediate nodes where data is split based on feature values.
   - **Leaf Nodes**: Terminal nodes that contain the predictions.

2. **Splitting Criteria**:
   - Decision Trees use metrics like:
     - **Gini Index**: Measures impurity in a node.
     - **Entropy**: Used in information gain to evaluate splits.
     - **Mean Squared Error (MSE)**: Used in regression trees to minimize variance.

3. **Prediction**:
   - For a given input, the tree is traversed from the root to a leaf based on feature values, where the prediction is made.

---

## Objective Function

The objective of a Decision Tree is to find splits that maximize information gain or minimize impurity/variance. For example:

1. **Gini Index** (Classification):
   $\
   Gini = 1 - \sum_{i=1}^n (p_i)^2
   $
   Where \(p_i\) is the proportion of class \(i\) in a node.

2. **Entropy and Information Gain**:
   - **Entropy**:
     $\
     Entropy = -\sum_{i=1}^n p_i \log_2(p_i)
     $
   - **Information Gain**:
     $\
     Information Gain = $Entropy_{parent} - \sum_{i=1}^n $\($\frac{|child_i|}{|parent|} Entropy_{child_i})
     $

3. **MSE (Regression)**:
   $\
   MSE = \frac{1}{n} \sum_{i=1}^n y_i - \hat{y}^2
   $

---

## Advantages of Decision Trees

1. **Interpretability**:
   - Simple to understand and interpret, even for non-technical stakeholders.

2. **No Assumptions**:
   - Does not require assumptions about the distribution of data.

3. **Handles Categorical and Numerical Data**:
   - Works well with both types of features.

4. **Feature Importance**:
   - Provides insights into which features are most important for predictions.

---

## Disadvantages of Decision Trees

1. **Overfitting**:
   - Deep trees can overfit the training data, reducing generalization.

2. **Instability**:
   - Small changes in data can result in a completely different tree structure.

3. **Bias Toward Features with Many Levels**:
   - Features with many unique values may dominate splits, even if they are not the most predictive.

---