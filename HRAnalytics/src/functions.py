import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def plot_hist(df): 
    """Generating histogram for the complete numerical columns present in the dataset
    Args:
        df (pandas dataframe): This parameter takes the dataframe object

    Returns:
        This shows a hist plot and does not return any value
    """
    numerical_cols = df.select_dtypes(include=['float64', 'int64']).columns
    plt.figure(figsize=(15,10))

    for idx, col in enumerate(numerical_cols, 1):
        plt.subplot(3, 3, idx)
        sns.histplot(data=df, x=col, kde=True)
        plt.title(f'Distribution of {col}')
        plt.xlabel(col)
        plt.ylabel('Count')

    plt.tight_layout()
    plt.show()