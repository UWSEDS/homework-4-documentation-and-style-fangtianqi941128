"""test_dataframe.py
by Tianqi Fang
11/06/2019

This module uses unittest to determine if a data frame
        imported from a csv file through an url is in a proper style.

The module first imports three tests done in hw2.py.
Then it checks that all columns have values of the correct type.
Next it checks if NAN values exist in data frame.
Finally, it verifies that the dataframe has at least one row.

The module returns ok or Fail to show if four tests are passed or not.
"""

import unittest

import pandas as pd

from hw2 import read_url, test_create_dataframe


URL = 'https://data.ct.gov/api/views/kbxi-4ia7/rows.csv'
LIST_COL_NAME = ['District Number', 'District', 'School', 'Test-takers: 2012',\
                'Test-takers: 2013', 'Test-takers: Change%',\
                'Participation Rate (estimate): 2012',\
                'Participation Rate (estimate): 2013',\
                'Participation Rate (estimate): Change%',\
                'Percent Meeting Benchmark: 2012', 'Percent Meeting Benchmark: 2013',\
                'Percent Meeting Benchmark: Change%']
DATA_FRAME = read_url(URL)

class TestModule(unittest.TestCase):
    """Using unittest to determine if data frame in proper style."""

    def test_dataframe(self):
        """Import test case in hw2.py, return ok or FAIL."""
        self.assertTrue(test_create_dataframe(DATA_FRAME, LIST_COL_NAME))

    def test_same_type(self):
        """Check that all columns have values of the same type, return ok or FAIL."""
        for i in range(len(list(DATA_FRAME.dtypes))):
            for j in range(list(DATA_FRAME.count())[i]):
                self.assertTrue(isinstance(DATA_FRAME.iloc[j, i], type(DATA_FRAME.iloc[0, i])))

    def test_nan(self):
        """Make sure that no NAN values in data frame, return ok or FAIL."""
        for i in list(DATA_FRAME.columns):
            self.assertTrue(not pd.isna(DATA_FRAME[i]).any())

    def test_at_least_one_row(self):
        """Verify that the dataframe has at least one row, return ok or FAIL."""
        for i in DATA_FRAME.count(axis='rows'):
            self.assertTrue(int(i) > 0)

if __name__ == '__main__':
    unittest.main(verbosity=2)
