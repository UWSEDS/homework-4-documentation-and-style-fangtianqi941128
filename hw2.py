"""hw2.py
by Tianqi Fang
11/06/2019

This module has a function that creates a dataframe from a URL which points to a CSV file.

Then, it has a function called test_create_dataframe with two inputs,
        a pandas DataFrame and a list of column names, that make three tests.
The function returns True if the following three tests all hold at the same time:
1. The DataFrame contains only the columns that you specified as the second argument.
2. The values in each column have the same python type
3. There are at least 10 rows in the DataFrame.
"""

import pandas as pd


def read_url(url):
    """Read a url to return a pandas data frame."""
    data_frame = pd.read_csv(url)
    return data_frame

def test_create_dataframe(data_frame, list_col_name):
    """Read a pandas data frame and a list of column names
        to do some tests and return true or false.
    """
    if data_frame.columns.tolist() != list_col_name: # test 1: same column names as provided.
        return False

    for i in range(len(list(data_frame.dtypes))): # test 2: same type in each column.
        for j in range(list(data_frame.count())[i]):
            if not isinstance(data_frame.iloc[j, i], type(data_frame.iloc[0, i])):
                return False

    if data_frame.shape[0] < 10: # test 3: at least 10 rows
        return False

    return True
