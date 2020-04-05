import os
# import sys
import pandas as pd

COL_COUNTRY = "Country/Region"
COL_PROVINCE = "Province/State"
FILE_CASES = "data/time_series_covid19_confirmed_global.csv"


def get_file_cases_path():
    return get_file_path(FILE_CASES)


def get_file_path(filename):
    path_to_here = os.path.dirname(__file__)
    filepath = os.path.join(path_to_here, filename)
    return filepath


def read_data():
    filepath = get_file_cases_path()
    return pd.read_csv(filepath)


def get_cases(df, country, province=None):
    df = get_country_cases(df, country)
    df = get_province_cases(df, province=province)
    return df


def get_country_cases(df, country):
    df = df[df[COL_COUNTRY] == country]
    return df


def get_province_cases(df, province=None):
    if province is None:
        # If one state is NaN use only this, otherwise sum all
        if df[COL_PROVINCE].isnull().any():
            df = df[df[COL_PROVINCE].isnull()]
    else:
        df = df[df[COL_PROVINCE] == province]
    return df.iloc[:, 4:].sum()
