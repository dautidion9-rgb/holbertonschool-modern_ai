# Data Preparation and Visualization

Python data preparation and visualization project for the Holberton School
Modern AI curriculum.

## Description

This project walks through a complete data preparation pipeline on the
[Telco Customer Churn dataset](https://www.kaggle.com/datasets/blastchar/telco-customer-churn):
exploring and cleaning the raw data, visualizing feature distributions,
testing features for statistical significance, and finally engineering,
encoding, scaling, and splitting the data so it is ready for machine
learning models that predict customer churn.

## Requirements

- Ubuntu 20.04 LTS, Python 3.11
- pandas, numpy, matplotlib, seaborn, scipy, scikit-learn
- Code follows `pycodestyle` 2.11.1
- All files are executable and start with `#!/usr/bin/env python3`

## Dataset

- `Telco-Customer-Churn.csv` — raw dataset (7,043 customers, 21 columns),
  used by tasks 0–5 (not committed; download it from the link above)
- `precleaned-Telco-Customer-Churn.csv` — output of tasks 2–5 (types
  converted, missing `TotalCharges` dropped, duplicates removed,
  `customerID` dropped); used by all tasks from 6 onward

## Tasks

### Exploration and cleaning

| File                                 | Description                                                                  |
| ------------------------------------ | ---------------------------------------------------------------------------- |
| `0-describe_data.py`                 | Print shape, dtypes, head, missing values and duplicate count of the dataset |
| `1-plot_missingness.py`              | Visualize the position of missing values across rows and columns             |
| `2-convert_columns.py`               | Convert `TotalCharges` to numeric and map `SeniorCitizen` to Yes/No          |
| `3-clean_total_charges.py`           | Handle missing `TotalCharges` by dropping, median fill, or imputation        |
| `4-remove_duplicates.py`             | Drop duplicate rows                                                          |
| `5-drop_customerID.py`               | Drop the `customerID` column and save the pre-cleaned dataset                |

### Visualization

| File                                 | Description                                                                  |
| ------------------------------------ | ---------------------------------------------------------------------------- |
| `6-plot_churn_distribution.py`       | Bar plot of the churn class distribution                                     |
| `7-plot_categorical_distributions.py`| Grid of bar plots for every categorical feature                              |
| `8-plot_continuous_distributions.py` | Plot distributions of continuous features with KDE and boxplots              |
| `9-plot_correlation_heatmap.py`      | Plot a correlation heatmap of numeric features                               |
| `10-plot_categorical_vs_churn.py`    | Bar plot of the churn rate per category of a feature                         |
| `11-plot_numeric_vs_churn.py`        | Grouped histograms of a numeric feature split by churn                       |

### Statistical testing

| File                                 | Description                                                                  |
| ------------------------------------ | ---------------------------------------------------------------------------- |
| `12-chi_square_tests.py`             | Chi-square p-values between each categorical feature and churn               |
| `13-ttest_numeric.py`                | Welch's t-test p-values comparing numeric features across churn groups       |

The tests show `gender` (p ≈ 0.49) and `PhoneService` (p ≈ 0.35) carry no
churn signal, so both are dropped before feature engineering.

### Feature engineering and preprocessing

| File                                 | Description                                                                  |
| ------------------------------------ | ---------------------------------------------------------------------------- |
| `14-create_features.py`              | Create `NumServices` (count of subscribed services) and `TenureGroup` (binned tenure) |
| `15-encode_features.py`              | Encode the target (label), binary features (ordinal), and nominal features (one-hot) |
| `16-scale_numeric.py`                | Standardize `MonthlyCharges` and `TotalCharges` with `StandardScaler`        |
| `17-split_data.py`                   | Stratified 80/20 train/test split preserving the churn class balance         |

## Usage

Each task has a matching `N-main.py` test file. Run one from this
directory, for example:

```bash
./17-main.py
```
