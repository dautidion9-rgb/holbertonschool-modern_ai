#!/usr/bin/env python3
"""Visualize missing data in a DataFrame."""
import matplotlib.pyplot as plt
import numpy as np


def plot_missingness(df):
    """Plot each missing value as a vertical bar per row and column."""
    plt.figure(figsize=(12, 8))

    rows, cols = np.where(df.isnull().to_numpy())
    plt.scatter(rows, cols, marker='|')
    plt.yticks(np.arange(len(df.columns)), df.columns)
    plt.title('Missingness Plot')

    plt.tight_layout()
    plt.show()
