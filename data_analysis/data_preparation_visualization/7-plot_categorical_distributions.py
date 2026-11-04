#!/usr/bin/env python3
"""Bar plots for the categorical feature distributions."""
import matplotlib.pyplot as plt


def plot_categorical_distributions(df, columns_to_plot=None):
    """Plots the value counts of each categorical column as bar plots.

    Args:
        df: pandas DataFrame
        columns_to_plot: optional list of categorical columns to plot;
            if None, all object columns except Churn are used

    Returns:
        None
    """
    if columns_to_plot is None:
        columns_to_plot = [col for col in
                           df.select_dtypes(include='object').columns
                           if col != 'Churn']
    else:
        columns_to_plot = list(columns_to_plot)
    n_cols, n_rows = 3, (len(columns_to_plot) + 2) // 3
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(15, 5*n_rows))

    axes = axes.flatten()
    for i, col in enumerate(columns_to_plot):
        counts = df[col].value_counts()
        axes[i].bar(counts.index, counts.values)
        axes[i].set_title(col)
        axes[i].tick_params(axis='x', rotation=45)

    for ax in axes[len(columns_to_plot):]:
        ax.set_visible(False)

    plt.tight_layout()
    plt.savefig("Task_7.png")
    plt.show()
