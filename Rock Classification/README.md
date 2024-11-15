
# Rock Classification Project

This project implements machine learning models to classify rock types based on various features. The goal is to compare the performance of different algorithms and ensemble methods against human accuracy in rock classification.

## Dataset

The project uses the following data files:

- **aggregateRockData.xlsx**: Main target for modeling, containing categorized and recognized data from the test phase, aggregated by rock token.

- **feature_presence540.txt**: Contains mean feature presence ratings for 540 rock stimuli.

- **trialData.csv**: Complete individual trial data from the main experiment.

## Models

The following classifiers are implemented:

1. Softmax Regression
2. Support Vector Machine
3. Random Forest Classifier
4. Ensemble Methods (Hard Voting, Soft Voting, Stacking)

## Data Preprocessing and Exploration

- Outlier detection using Z-score
- Visualization with histograms, scatter plots, and box plots
- Correlation analysis using a correlation matrix

## Model Evaluation

Metrics used for performance assessment:

1. Accuracy
2. Precision
3. Recall
4. F1 Score

Additional evaluation tools:
- Confusion matrix
- Randomized search cross-validation

## Data Splitting

- Training data: Token numbers 1-10
- Validation data: Token numbers 11-13
- Test data: Token numbers 14-16

(Each of the 30 rock subtypes has 16 token numbers)

## Results

The best performing model was the Stacking Classifier:

- Test set accuracy: 59.32%
- Correctly classified:
  - Igneous Rocks: 21
  - Metamorphic Rocks: 8
  - Sedimentary Rocks: 6
- Precision: 59%
- Recall: 55%

## Comparison with Human Accuracy

- Model accuracy on test dataset: 59.32%
- Human accuracy on test dataset: 59.84%
- Model accuracy on train dataset: 73%
- Human accuracy on train dataset: 55.99%

## Observations

1. The model's test accuracy (59.32%) is slightly lower than human test accuracy (59.84%).
2. The model's training accuracy (73%) is higher than human training accuracy (55.99%).
3. The model performed well on training and validation sets compared to human accuracy but couldn't outperform human accuracy on the test dataset.
4. The validation set accuracy was around 80% with a precision of about 84%.
5. Limited data points may have affected the model's training accuracy.

## Future Work

- Collect more data to improve model training and generalization
- Experiment with feature engineering and selection
- Try advanced deep learning approaches for potentially better performance

## Requirements

- scikit-learn
- pandas
- numpy
- matplotlib
- seaborn
- openpyxl


## Author

Khushi Kala
