#!/usr/bin/env python3
"""Compare a numeric feature's distribution by churn."""
import matplotlib.pyplot as plt


def plot_numeric_vs_churn(df, col):
    """Plots overlapping histograms of col for Churn=No and Churn=Yes.

    Args:
        df: pandas DataFrame with a Churn column
        col: numeric column name

    Returns:
        None
    """
    plt.figure(figsize=(12, 8))

    plt.hist([df[df['Churn'] == 'No'][col],
              df[df['Churn'] == 'Yes'][col]],
             bins=30, label=['No', 'Yes'])
    plt.title(f"{col} Distribution by Churn")
    plt.xlabel(col)
    plt.legend(title='Churn')
    plt.show()
