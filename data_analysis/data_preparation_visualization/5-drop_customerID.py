#!/usr/bin/env python3
"""Drop the customerID column from a DataFrame."""


def drop_customerID(df):
    """Remove the customerID column and return the modified DataFrame."""
    return df.drop(columns=['customerID'])
