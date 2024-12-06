# Logistic Regression: Overview

Logistic Regression is a statistical method used for **binary classification** problems. Unlike Linear Regression, which predicts a continuous value, Logistic Regression predicts the probability of an observation belonging to a specific class.

---

## Key Concepts

1. **Purpose**:
   - Logistic Regression is used to model the relationship between one or more independent variables and a binary dependent variable (e.g., "Yes" or "No," "Spam" or "Not Spam").

2. **Sigmoid Function**:
   - Logistic Regression uses the sigmoid function to map predicted values to probabilities:
     \[
     \sigma(z) = \frac{1}{1 + e^{-z}}
     \]
     Where:
     - \( z \) is the linear combination of the input features: \( z = m_1X_1 + m_2X_2 + \dots + b \).
     - \( \sigma(z) \) outputs a probability between 0 and 1.

3. **Decision Boundary**:
   - Predictions are made by applying a threshold (e.g., 0.5). If \( \sigma(z) > 0.5 \), the model predicts one class; otherwise, it predicts the other.

4. **Loss Function**:
   - Logistic Regression minimizes the **log-loss** function, which measures how well the predicted probabilities match the actual labels:
     \[
     \text{Log Loss} = -\frac{1}{n} \sum_{i=1}^n \left[ y_i \log(\hat{y}_i) + (1 - y_i) \log(1 - \hat{y}_i) \right]
     \]
     Where:
     - \( y_i \): Actual label (0 or 1).
     - \( \hat{y}_i \): Predicted probability.

---

## Key Advantages of Logistic Regression
- Simple and easy to interpret.
- Outputs probabilities, making it useful for decision-making.
- Computationally efficient for small to medium-sized datasets.

## Disadvantages of Logistic Regression
1. - **Linear Decision Boundary**:

Logistic Regression assumes the data can be separated linearly. It performs poorly if the relationship between features and the target is non-linear.

2. - **Sensitive to Outliers**:

Outliers in the dataset can affect the model's performance and decision boundary.

3. - **Binary Classification Only**:

While it can be extended to multi-class problems (using techniques like One-vs-Rest or Softmax), it is inherently designed for binary classification.

4. - **Assumption of Independence**:

Logistic Regression assumes that the independent variables are not highly correlated (no multicollinearity).