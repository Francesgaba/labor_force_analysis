#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np

class LaborForceDataAnalysis:
    """
    A class for loading and exploring labor force data.

    Methods:
        load_data(): Load the dataset from the provided URL.
        explore_data(): Display basic exploratory information about the dataset.
    """

    def __init__(self, data_url):
        """
        Initializes a LaborForceDataAnalysis object.

        Args:
            data_url (str): The URL of the dataset to be loaded.
        """
        self.data_url = data_url
        self.df = None

    def load_data(self):
        """
        Load the dataset from the provided URL.

        Returns:
             True if data is loaded successfully, False otherwise.
        """
        try:
            self.df = pd.read_csv(self.data_url, sep=",")
            return True
        except Exception as e:
            print(f"Error loading data: {str(e)}")
            return False

    def explore_data(self):
        """
        Display basic exploratory information about the dataset.
        """
        if self.df is not None:
            print(self.df.head())
            print(self.df.info())
            print(self.df.describe())
        else:
            print("Data not loaded. Use 'load_data()' to load the dataset.")
            

