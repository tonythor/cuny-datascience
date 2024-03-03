'''
Assignment #6
1. Add / modify code ONLY between the marked areas (i.e. "Place code below") 
2. Run the associated test harness for a basic check on completeness. A successful run of the test cases does not guarantee accuracy or fulfillment of the requirements. Please do not submit your work if test cases fail.
3. Unless explicitly stated, please do not import any additional libraries but feel free to use built-in Python packages
4. Submissions must be a Python file and not a notebook file (i.e *.ipynb)
5. Do not use global variables
'''

import pandas as pd
import unittest

def exercise01():
    '''
    Create a DataFrame 'df1' with 5 rows and 2 columns with columns named 'Name' and 'Age'. 
    Fill the DataFrame with arbitrary data.
    '''
    # ------ Place code below here \/ \/ \/ ------
    
    # ------ Place code above here /\ /\ /\ ------
    return df1

def exercise02():
    '''
    Load the dataset from the CSV file 'data.csv' into a DataFrame 'df2'. Assume 'data.csv' is in the same directory as this script.
    The dataset contains columns 'id', 'name', 'value'. Print the first 5 rows as part of the exercise.
    '''
    # ------ Place code below here \/ \/ \/ ------
   
    # ------ Place code above here /\ /\ /\ ------
    return df2

def exercise03(df):
    '''
    Given a DataFrame 'df', filter out and return a new DataFrame containing only the rows where 'value' is greater than 50.
    '''
    # ------ Place code below here \/ \/ \/ ------
    
    # ------ Place code above here /\ /\ /\ ------
    return filtered_df


def exercise04():
    '''
    Create a DataFrame 'df4' directly using a list of dictionaries.
    Each dictionary represents a row, with 'city' and 'data' as keys.
    '''
    # ------ Place code below here \/ \/ \/ ------

    # ------ Place code above here /\ /\ /\ ------
    return df4


def exercise05(df):
    '''
    Given a DataFrame 'df', add a new column 'data_squared' that contains the square of the 'data' column values.
    '''
    # ------ Place code below here \/ \/ \/ ------
    df['data_squared'] = df['data'] ** 2
    # ------ Place code above here /\ /\ /\ ------
    return df

def exercise06():
    '''
    Load data from an Excel file 'data.xlsx' into a DataFrame 'df6'. The file 'data.xlsx' has the data in the first sheet.
    Assume the Excel file has columns 'A', 'B', 'C'. Return the DataFrame.
    '''
    # ------ Place code below here \/ \/ \/ ------
    
    # ------ Place code above here /\ /\ /\ ------
    return df6

def exercise07(df):
    '''
    Given a DataFrame 'df', drop any rows that have missing values and return the cleaned DataFrame.
    '''
    # ------ Place code below here \/ \/ \/ ------
    
    # ------ Place code above here /\ /\ /\ ------
    return cleaned_df

def exercise08(df, column_name):
    '''
    Given a DataFrame 'df' and a 'column_name' as a string, return the average value of that column.
    '''
    # ------ Place code below here \/ \/ \/ ------
    
    # ------ Place code above here /\ /\ /\ ------
    return avg_value

class TestAssignment(unittest.TestCase):
    def test_exercise01(self):
        df = exercise01()
        self.assertEqual(df.shape, (5, 2))
        self.assertTrue('Name' in df.columns and 'Age' in df.columns)

    def test_exercise02(self):
        df = exercise02()
        self.assertTrue('id' in df.columns and 'name' in df.columns and 'value' in df.columns)

    def test_exercise03(self):
        df = pd.DataFrame({'id': [1, 2, 3], 'name': ['A', 'B', 'C'], 'value': [45, 55, 65]})
        df = exercise03(df)
        self.assertEqual(df.shape[0], 2)  

    def test_exercise04(self):
        df4 = exercise04()
        self.assertTrue(set(df4.columns) == {"city", "data"})
        self.assertEqual(len(df4), 3)

    def test_exercise05(self):
       df = pd.DataFrame({'city': ['A', 'B', 'C'], 'data': [1, 2, 3]})
       df = exercise05(df)
       self.assertTrue('data_squared' in df.columns)
       self.assertEqual(list(df['data_squared']), [1, 4, 9])

    def test_exercise06(self):
       df = exercise06()
       self.assertTrue('A' in df.columns and 'B' in df.columns and 'C' in df.columns)

    def test_exercise07(self):
       df = pd.DataFrame({'A': [1, 2, None, 4], 'B': [None, 2, 3, 4]})
       df = exercise07(df)
       self.assertEqual(df.shape[0], 2)  

    def test_exercise08(self):
       df = pd.DataFrame({'A': [10, 20, 30], 'B': [20, 30, 40]})
       avg_A = exercise08(df, 'A')
       avg_B = exercise08(df, 'B')
       self.assertEqual(avg_A, 20)
       self.assertEqual(avg_B, 30)

if __name__ == '__main__':
   unittest.main()

