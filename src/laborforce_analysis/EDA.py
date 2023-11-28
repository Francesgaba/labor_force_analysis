#!/usr/bin/env python
# coding: utf-8

# In[3]:


import matplotlib.pyplot as plt
import seaborn as sns

class ContinuousVariableVisualization:
    def __init__(self, df):
        self.df = df
        self.continuous_variables = ["lwg", "inc"]

    def plot_histograms_and_boxplots(self):
        for col in self.continuous_variables:
            fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(15, 6))  # creating a 2x2 subplot structure for each variable

            # Matplotlib histogram
            axes[0, 0].hist(self.df[col], bins=20, edgecolor='black', alpha=0.7)
            axes[0, 0].set_title(f'Matplotlib - Distribution of {col}')

            # Seaborn histogram
            sns.histplot(self.df[col], kde=True, ax=axes[0, 1])
            axes[0, 1].set_title(f'Seaborn - Distribution of {col}')

            # Matplotlib boxplot
            axes[1, 0].boxplot(self.df[col], patch_artist=True)
            axes[1, 0].set_title(f'Matplotlib - Boxplot of {col}')

            # Seaborn boxplot
            sns.boxplot(x=self.df[col], ax=axes[1, 1])
            axes[1, 1].set_title(f'Seaborn - Boxplot of {col}')

            plt.tight_layout()
            plt.show()


# In[ ]:


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


class CategoricalDataVisualization:
    """
    A class to visualize categorical and discrete data in a DataFrame.

    This class provides methods to create bar plots using both Matplotlib and Seaborn
    to visualize the distribution of categorical and discrete attributes.

    Attributes:
    df (pd.DataFrame): A pandas DataFrame containing the data to be visualized.
    """

    def __init__(self, df):
        """
        Initializes the CategoricalDataVisualization with a DataFrame.

        Parameters:
        df (pd.DataFrame): A pandas DataFrame containing the data for visualization.
        """
        self.df = df

    def plot_distributions(self, attributes):
        """
        Plots the distributions of the specified categorical and discrete attributes
        using both Matplotlib and Seaborn.

        For each attribute, this method creates a figure with two subplots: one for
        the Matplotlib bar plot and the other for the Seaborn count plot.

        Parameters:
        attributes (list of str): A list of column names from the DataFrame representing 
                                  the categorical and discrete attributes to be visualized.
        """
        for col in attributes:
            fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(20, 3)) 

            # Matplotlib bar plot
            axes[0].bar(self.df[col].value_counts().index, self.df[col].value_counts())
            axes[0].set_title(f'Matplotlib - Distribution of {col}')
            axes[0].tick_params(axis='x', rotation=90)

            # Seaborn count plot
            sns.countplot(data=self.df, x=col, ax=axes[1])
            axes[1].set_title(f'Seaborn - Distribution of {col}')
            axes[1].tick_params(axis='x', rotation=90)

            plt.tight_layout()
            plt.show()


# In[5]:


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

class CorrelationMatrixVisualization:
    """
    A class for encoding categorical variables and visualizing correlation matrices.

    This class provides methods to encode specified categorical variables in a DataFrame
    and to plot the resulting correlation matrix using both Matplotlib and Seaborn.

    Attributes:
    df (pd.DataFrame): A pandas DataFrame containing the data to be visualized and encoded.
    """

    def __init__(self, df):
        """
        Initializes the CorrelationMatrixVisualization with a DataFrame.

        Parameters:
        df (pd.DataFrame): A pandas DataFrame containing the data for visualization and encoding.
        """
        self.df = df

    def encode_categorical_variables(self, columns, mapping):
        """
        Encodes specified categorical variables in the DataFrame.

        Parameters:
        columns (list of str): A list of column names to be encoded.
        mapping (dict): A dictionary defining the mapping for encoding.
        """
        for col in columns:
            if col in self.df.columns:
                self.df[f'{col}_encoded'] = self.df[col].map(mapping)

    def plot_correlation_matrix(self, exclude_columns=None):
        """
        Plots the correlation matrix of the DataFrame using both Matplotlib and Seaborn.

        Parameters:
        exclude_columns (list of str, optional): A list of column names to be excluded from the correlation matrix.
        """
        if exclude_columns is not None:
            selected_columns = self.df.columns[~self.df.columns.isin(exclude_columns)]
        else:
            selected_columns = self.df.columns

        correlation_matrix = self.df[selected_columns].corr()

    
        plt.figure(figsize=(5, 4))
        plt.matshow(correlation_matrix, fignum=1)
        plt.colorbar()
        plt.xticks(range(len(correlation_matrix.columns)), correlation_matrix.columns, rotation=90)
        plt.yticks(range(len(correlation_matrix.columns)), correlation_matrix.columns)
        plt.title('Matplotlib - Correlation Matrix', pad=20)
        plt.show()

        # Seaborn heatmap
        plt.figure(figsize=(5, 4))
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
        plt.title('Seaborn - Correlation Matrix')
        plt.show()

