#!/usr/bin/env python3
"""Encode features for modeling with scikit-learn."""
import pandas as pd
from sklearn import preprocessing


def encode_features(df):
    """Encodes the target, binary, ordinal and nominal features.

    Args:
        df: pandas DataFrame

    Returns:
        tuple of (encoded DataFrame, fitted LabelEncoder for Churn,
        fitted OrdinalEncoder for binary columns,
        fitted OrdinalEncoder for TenureGroup)
    """
    df = df.copy()

    churn_le = preprocessing.LabelEncoder()
    df['Churn'] = churn_le.fit_transform(df['Churn'])

    binary_cols = ['Partner', 'Dependents', 'PaperlessBilling',
                   'SeniorCitizen']
    binary_oe = preprocessing.OrdinalEncoder(
        categories=[['No', 'Yes']] * len(binary_cols))
    df[binary_cols] = binary_oe.fit_transform(df[binary_cols]).astype(int)

    tenure_oe = preprocessing.OrdinalEncoder()
    df[['TenureGroup']] = tenure_oe.fit_transform(
        df[['TenureGroup']]).astype(int)

    df = pd.get_dummies(df, columns=['Contract', 'PaymentMethod'],
                        drop_first=True, dtype=int)

    return df, churn_le, binary_oe, tenure_oe
