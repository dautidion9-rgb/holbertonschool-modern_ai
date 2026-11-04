#!/usr/bin/env python3
"""Visualize the churn class distribution."""
import matplotlib.pyplot as plt


def plot_churn_distribution(df):
    """Plot the Churn value counts as a bar plot.

    Args:
        df: pandas DataFrame with a Churn column

    Returns:
        None
    """
    plt.figure(figsize=(12, 8))

    counts = df['Churn'].value_counts()
    plt.bar(counts.index, counts.values, color=['skyblue', 'salmon'])
    plt.title('Churn Distribution')
    plt.ylabel('Count')
    plt.show()
