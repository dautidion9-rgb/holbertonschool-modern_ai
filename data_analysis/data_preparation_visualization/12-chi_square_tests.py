#!/usr/bin/env python3
"""Chi-square tests between categorical features and Churn."""
import pandas as pd
from scipy import stats


def chi_square_tests(df):
    """Tests independence between each categorical feature and Churn.

    Args:
        df: pandas DataFrame with a Churn column

    Returns:
        dict mapping each feature name to its chi-square p-value
    """
    p_values = {}
    for col in df.select_dtypes(include='object').columns:
        if col == 'Churn':
            continue
        contingency = pd.crosstab(df[col], df['Churn'])
        p_values[col] = stats.chi2_contingency(contingency)[1]
    return p_values
