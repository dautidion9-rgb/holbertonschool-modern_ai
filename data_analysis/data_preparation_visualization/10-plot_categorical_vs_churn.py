#!/usr/bin/env python3
"""
Count plots of categorical features split by the Churn target.
"""
import math
import matplotlib.pyplot as plt
import seaborn as sns


def plot_categorical_vs_churn(df, columns_to_plot=None):
    """
    Plots a count plot for each categorical column, colored by Churn.

    Args:
        df: pandas DataFrame
        columns_to_plot: optional list of categorical columns to plot;
            if None, all non-numeric columns except Churn are used

    Returns:
        None
    """
    if columns_to_plot is None:
        columns_to_plot = df.select_dtypes(
            exclude="number").columns.drop("Churn").tolist()

    n_cols = 3
    n_rows = math.ceil(len(columns_to_plot) / n_cols)
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(5*n_cols, 4*n_rows))
    axes = axes.flatten()

    for i, col in enumerate(columns_to_plot):
        sns.countplot(data=df, x=col, hue="Churn", ax=axes[i])
        axes[i].set_title(f"{col} vs Churn")
        axes[i].tick_params(axis="x", rotation=45)

    for ax in axes[len(columns_to_plot):]:
        ax.set_visible(False)

    plt.tight_layout()
    plt.show()
