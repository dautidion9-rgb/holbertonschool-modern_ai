#!/usr/bin/env python3
"""
Histogram + KDE and boxplot for continuous numeric features.
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats


def plot_continuous_distributions(df, columns_to_plot=None):
    """
    Plots a histogram with KDE and a boxplot for each continuous column.

    Args:
        df: pandas DataFrame
        columns_to_plot: optional list of numeric columns to plot;
            if None, all numeric columns are used

    Returns:
        None
    """
    if columns_to_plot is None:
        columns_to_plot = df.select_dtypes(
            include=[np.number]).columns.tolist()

    n_cols = len(columns_to_plot)
    fig, axes = plt.subplots(n_cols, 2, figsize=(10, 3*n_cols))

    if n_cols == 1:
        axes = axes.reshape(1, -1)

    for i, col in enumerate(columns_to_plot):
        data = df[col].dropna()

        axes[i, 0].hist(data, bins=30, density=True, alpha=0.7,
                        edgecolor='black')
        kde = stats.gaussian_kde(data)
        x = np.linspace(data.min(), data.max(), 200)
        axes[i, 0].plot(x, kde(x), 'r--')
        axes[i, 0].set_title(f"{col} Histogram + KDE")

        axes[i, 1].boxplot(data, vert=False)
        axes[i, 1].set_title(f"{col} Boxplot")

    plt.tight_layout()
    plt.savefig("Task_8.png")
    plt.show()