#!/usr/bin/env python3
"""Engineer NumServices and TenureGroup features."""
import pandas as pd


def create_features(df):
    """Creates NumServices and TenureGroup, dropping the source columns.

    Args:
        df: pandas DataFrame

    Returns:
        the modified DataFrame
    """
    df = df.copy()
    service_cols = ['MultipleLines', 'InternetService', 'OnlineSecurity',
                    'OnlineBackup', 'DeviceProtection', 'TechSupport',
                    'StreamingTV', 'StreamingMovies']

    df['NumServices'] = (
        (df[service_cols] == 'Yes').sum(axis=1)
        + df['InternetService'].isin(['DSL', 'Fiber optic']).astype(int))

    df['TenureGroup'] = pd.cut(
        df['tenure'],
        bins=[0, 12, 24, 48, 60, float('inf')],
        labels=['0-12', '13-24', '25-48', '49-60', '60+'])

    return df.drop(columns=service_cols + ['tenure'])
