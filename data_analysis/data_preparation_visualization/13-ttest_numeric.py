#!/usr/bin/env python3
"""Welch's t-tests between numeric features and Churn."""
from scipy import stats


def ttest_numeric(df):
    """Compares each numeric feature's means for Churn=Yes vs Churn=No.

    Args:
        df: pandas DataFrame with a Churn column

    Returns:
        dict mapping each numeric feature name to its t-test p-value
    """
    p_values = {}
    for col in df.select_dtypes(include='number').columns:
        yes = df[df['Churn'] == 'Yes'][col]
        no = df[df['Churn'] == 'No'][col]
        p_values[col] = stats.ttest_ind(yes, no, equal_var=False)[1]
    return p_values
