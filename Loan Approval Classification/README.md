
# Loan Status Classification

This project implements a machine learning model to predict loan approval status using various classification algorithms and ensemble methods.

## Project Overview

- **Objective**: Predict whether a loan application will be approved or denied.
- **Models Used**: Logistic Regression, Support Vector Classifier (SVC), Random Forest
- **Ensemble Methods**: Voting Classifier, Bagging Classifier, Stacking Classifier
- **Best Performing Model**: Bagging Classifier (85% accuracy on validation set, 81% on test set)

## Dataset

- **Size**: 614 rows, 13 columns
- **Features**: Loan_ID, Married, Education, Self_Employed, ApplicantIncome, CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History, Property_Area
- **Target Variable**: Loan_Status (Yes/No)

## Data Preprocessing

- Handled null values using dropna
- Encoded categorical variables with OneHotEncoder
- Encoded target variable with LabelEncoder
- Handled outliers using Z-score
- Scaled features using StandardScaler

## Exploratory Data Analysis

- Plotted histograms and scatter plots
- Created correlation matrix

## Model Development

1. Split data into train, validation, and test sets
2. Implemented Logistic Regression, SVC, and Random Forest models
3. Performed hyperparameter tuning for all models
4. Applied ensemble methods: hard voting, soft voting, stacking classifier, and bagging
5. Evaluated models using accuracy, precision, recall, and F1-score

## Results

The Bagging Classifier achieved the best performance:
- Validation Set Accuracy: 85%
- Test Set Accuracy: 81%
- Precision: 88%
- Recall: 78%

## Conclusion

The model demonstrates strong performance in classifying loan approval statuses, with high precision in identifying approved loans. There is room for improvement in capturing all instances of loan approvals.

## Future Work

- Experiment with feature engineering to improve model performance
- Try other advanced ensemble methods or deep learning approaches
- Collect more data to potentially improve model generalization

## Requirements

- scikit-learn
- pandas
- numpy
- matplotlib
- seaborn

## Author

**Khushi Kala**
