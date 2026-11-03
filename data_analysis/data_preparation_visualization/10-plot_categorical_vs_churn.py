#!/usr/bin/env python3
"""Churn rate per category of a categorical feature."""
import matplotlib.pyplot as plt


def plot_categorical_vs_churn(df, col):
    """Plots the churn rate per category of col as a bar plot.

    Args:
        df: pandas DataFrame with a Churn column
        col: categorical column name

    Returns:
        None
    """
    churn_rate = df.groupby(col)["Churn"].apply(
        lambda s: (s == "Yes").mean())

    plt.figure(figsize=(12, 6))
    plt.bar(churn_rate.index, churn_rate.values)
    plt.title(f"Churn Rate by {col}")
    plt.ylabel("Churn Rate")
    plt.xticks(rotation=45)
    plt.show()
