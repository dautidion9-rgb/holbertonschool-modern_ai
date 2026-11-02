#!/usr/bin/env python3
"""
Correlation heatmap of continuous numeric features.
"""
import seaborn as sns
import matplotlib.pyplot as plt


def plot_correlation_heatmap(df):
    """
    Plots an annotated correlation heatmap of the numeric columns in df.

    Args:
        df: pandas DataFrame

    Returns:
        None
    """
    plt.figure(figsize=(6, 5))

    corr = df.select_dtypes(include="number").corr()

    sns.heatmap(corr, annot=True, cmap="coolwarm", vmin=-1, vmax=1)

    plt.title("Correlation Heatmap")
    plt.tight_layout()
    plt.show()
