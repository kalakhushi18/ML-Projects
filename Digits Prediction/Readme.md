**Handwritten Digits Classification using Logistic Regression**

This project implements a machine learning model to classify handwritten digits (0-9) using the popular Scikit-learn digits dataset. The model achieves a robust accuracy of 95% using Logistic Regression.

**Dataset Overview**

The project uses the built-in digits dataset from scikit-learn, which includes:

1,797 samples of handwritten digits (0-9)
Each image is 8x8 pixels in grayscale
Each pixel has a value from 0-16, representing intensity
Target values are the actual digits (0-9)

**Requirements**

numpy
pandas
scikit-learn
matplotlib
seaborn


**Data Preprocessing**

Loading the digits dataset using sklearn.datasets.load_digits()
Visualization of sample digits using matplotlib's imshow()
Feature scaling: Data is already scaled (0-16 pixel values)
Train-test split: 80-20 ratio (standard split for sufficient training while maintaining a good test set)

**Training Process**

Split data into training and testing sets
Initialize Logistic Regression model
Train model on training data
Make predictions on test data

**Results Visualization**

The project includes:

Sample digit images from the dataset

Confusion matrix heatmap

**Author**

Khushi Kala
