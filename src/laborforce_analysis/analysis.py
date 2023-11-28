#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

class LaborForceParticipationVisualization:
    """
    A class for visualizing labor force participation in relation to categorical variables.

    This class provides methods to create binary and grouped categorical variables
    and to plot the relationship of these variables with labor force participation.
    """

    def __init__(self, df):
        """
        Initializes the LaborForceParticipationVisualization with a DataFrame.

        Parameters:
        df (pd.DataFrame): A pandas DataFrame containing the data for visualization.
        """
        self.df = df

    def create_binary_variable(self, column, threshold, new_column_name):
        """
        Creates a binary variable based on a specified threshold.

        Parameters:
        column (str): The name of the column to be transformed into a binary variable.
        threshold (int or float): The threshold value for the binary conversion.
        new_column_name (str): The name for the new binary column.
        """
        self.df[new_column_name] = self.df[column].apply(lambda x: 1 if x > threshold else 0)

    def create_grouped_variable(self, column, groups, new_column_name):
        """
        Creates a grouped variable based on specified groupings.

        Parameters:
        column (str): The name of the column to be transformed into a grouped variable.
        groups (dict): A dictionary defining the grouping.
        new_column_name (str): The name for the new grouped column.
        """
        self.df[new_column_name] = self.df[column].apply(lambda x: groups[x] if x in groups else groups['default'])

    def plot_lfp_rate_by_group(self, group_column, target_column, title, labels, xlabel, ylabel):
        """
        Plots the labor force participation rate by different groups.

        Parameters:
        group_column (str): The name of the column representing the groups.
        target_column (str): The name of the column representing the target variable.
        title (str): The title of the plot.
        labels (list of str): Labels for the groups in the plot.
        xlabel (str): The label for the x-axis.
        ylabel (str): The label for the y-axis.
        """
        lfp_rate_by_group = self.df.groupby(group_column)[target_column].mean().reset_index()

        plt.figure(figsize=(8, 6))
        sns.barplot(x=group_column, y=target_column, data=lfp_rate_by_group, order=labels)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        plt.xticks(range(len(labels)), labels)
        plt.show()


# In[ ]:


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

class OlderChildrenLFPVisualization:
    """
    A class for analyzing and visualizing labor force participation rates based on the number of older children.

    Attributes:
        df (pd.DataFrame): A pandas DataFrame containing the data to be analyzed and visualized.
    """

    def __init__(self, df):
        """
        Initializes the OlderChildrenLFPVisualization with a DataFrame.

        Parameters:
            df (pd.DataFrame): A pandas DataFrame containing the data for analysis and visualization.
        """
        self.df = df

    def create_grouped_children_variable(self, children_column, grouped_column_name):
        """
        Creates a grouped variable for the number of older children.

        Parameters:
            children_column (str): The name of the column indicating the number of older children.
            grouped_column_name (str): The name for the new grouped column.
        """
        self.df[grouped_column_name] = self.df[children_column].apply(lambda x: '0' if x == 0 else ('1' if x == 1 else ('2' if x == 2 else '3+')))

    def plot_lfp_rate_by_children_number(self, grouped_column, target_column, xlabel, ylabel, title, xtick_labels, order):
        """
        Plots the labor force participation rate by the number of older children.

        Parameters:
            grouped_column (str): The name of the grouped column indicating the number of older children.
            target_column (str): The name of the column representing the target variable (labor force participation rate).
            xlabel (str): The label for the x-axis.
            ylabel (str): The label for the y-axis.
            title (str): The title of the plot.
            xtick_labels (list of str): Labels for the x-axis ticks.
            order (list): The order of groups to be plotted.
        """
        lfp_rate = self.df.groupby(grouped_column)[target_column].mean().reset_index()

        plt.figure(figsize=(8, 6))
        sns.barplot(x=grouped_column, y=target_column, data=lfp_rate, order=order)

        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        plt.xticks(range(len(xtick_labels)), xtick_labels)

        plt.show()


# In[ ]:


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

class OlderChildrenLFPVisualization:
    """
    A class for analyzing and visualizing labor force participation rates based on the number of older children.

    Attributes:
        df (pd.DataFrame): A pandas DataFrame containing the data to be analyzed and visualized.
    """

    def __init__(self, df):
        """
        Initializes the OlderChildrenLFPVisualization with a DataFrame.

        Parameters:
            df (pd.DataFrame): A pandas DataFrame containing the data for analysis and visualization.
        """
        self.df = df

    def create_grouped_children_variable(self, children_column, grouped_column_name):
        """
        Creates a grouped variable for the number of older children.

        Parameters:
            children_column (str): The name of the column indicating the number of older children.
            grouped_column_name (str): The name for the new grouped column.
        """
        self.df[grouped_column_name] = self.df[children_column].apply(lambda x: '0' if x == 0 else ('1' if x == 1 else ('2' if x == 2 else '3+')))

    def plot_lfp_rate_by_children_number(self, grouped_column, target_column, xlabel, ylabel, title, xtick_labels, order):
        """
        Plots the labor force participation rate by the number of older children.

        Parameters:
            grouped_column (str): The name of the grouped column indicating the number of older children.
            target_column (str): The name of the column representing the target variable (labor force participation rate).
            xlabel (str): The label for the x-axis.
            ylabel (str): The label for the y-axis.
            title (str): The title of the plot.
            xtick_labels (list of str): Labels for the x-axis ticks.
            order (list): The order of groups to be plotted.
        """
        lfp_rate = self.df.groupby(grouped_column)[target_column].mean().reset_index()

        plt.figure(figsize=(8, 6))
        sns.barplot(x=grouped_column, y=target_column, data=lfp_rate, order=order)

        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        plt.xticks(range(len(xtick_labels)), xtick_labels)

        plt.show()


# In[ ]:



import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

class AgeGroupParticipationVisualization:
    """
    A class for visualizing labor force participation by age group.

    This class provides methods to categorize individuals into age groups and to plot
    the labor force participation rates for these groups.

    Attributes:
    df (pd.DataFrame): A pandas DataFrame containing the data to be visualized.
    """

    def __init__(self, df):
        """
        Initializes the AgeGroupParticipationVisualization with a DataFrame.

        Parameters:
        df (pd.DataFrame): A pandas DataFrame containing the data for visualization.
        """
        self.df = df

    def categorize_age_groups(self, age_column, new_column_name, threshold):
        """
        Categorizes ages into groups based on a specified threshold.

        Parameters:
        age_column (str): The name of the column containing age data.
        new_column_name (str): The name for the new age group column.
        threshold (int): The age threshold to split the groups.
        """
        self.df[new_column_name] = self.df[age_column].apply(lambda x: 'Before ' + str(threshold) if x < threshold else str(threshold) + ' and After')

    def plot_lfp_by_age_group(self, age_group_column, target_column, title, xlabel, ylabel):
        """
        Plots the labor force participation rate by age group.

        """
        age_group_lfp = self.df.groupby(age_group_column)[target_column].mean().reset_index()

        plt.figure(figsize=(8, 6))
        sns.barplot(x=age_group_column, y=target_column, data=age_group_lfp)

        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        plt.show()

