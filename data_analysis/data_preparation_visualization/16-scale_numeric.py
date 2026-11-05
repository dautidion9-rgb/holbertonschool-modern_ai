#!/usr/bin/env python3
"""Standardize the numeric charge columns."""
from sklearn import preprocessing


def scale_numeric(df):
    """Scales MonthlyCharges and TotalCharges to mean 0 and std 1.

    Args:
        df: pandas DataFrame

    Returns:
        the modified DataFrame
    """
    df = df.copy()
    cols = ['MonthlyCharges', 'TotalCharges']
    scaler = preprocessing.StandardScaler()
    df[cols] = scaler.fit_transform(df[cols])
    return df
