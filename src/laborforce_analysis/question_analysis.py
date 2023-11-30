#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class LaborForceParticipationVisualization:
    def __init__(self, df):
        """
        Initialize the LaborForceParticipationVisualization class with a DataFrame.

    
        df (pd.DataFrame): The DataFrame containing the data for visualization.
        """
        self.df = df

    def plot_lfp_by_k5(self):
        """
        Plot the Labor Force Participation Rate by the presence of children under 5.

        This method creates a binary column based on the 'k5' variable, groups the data by
        the new binary column, and calculates the mean of 'lfp_encoded'. It then plots a bar
        chart to visualize the labor force participation rate based on whether there are
        children under 5 in the household.

        """
        # Create a binary column based on 'k5' variable
        self.df['k5_binary'] = self.df['k5'].apply(lambda x: 1 if x > 0 else 0)

        # Group by the new binary column and calculate mean of 'lfp_encoded', reset index for easier plotting
        lfp_rate_by_k5 = self.df.groupby('k5_binary')['lfp_encoded'].mean().reset_index()

        # Plotting
        plt.figure(figsize=(8, 6))
        sns.barplot(x='k5_binary', y='lfp_encoded', data=lfp_rate_by_k5)

        plt.xlabel('Children under 5')
        plt.ylabel('Labor Force Participation Rate')
        plt.title('Labor Force Participation by Young Children')
        plt.xticks([0, 1], ['No Children under 5', 'At Least One Child under 5'])

        plt.show()

# In[ ]:


import matplotlib.pyplot as plt
import pandas as pd

class CouplesEducationLFPVisualization:
    """
    A class for analyzing and visualizing labor force participation rates based on the educational background of couples.

    Args:
        df (pd.DataFrame): The DataFrame containing the data for visualization.
    """

    def __init__(self, df):
        """
        Initialize the CouplesEducationLFPVisualization class.

        Args:
            df (pd.DataFrame): The DataFrame containing the data for visualization.
        """
        self.df = df

    def prepare_data(self):
        """

        This method creates several columns in the DataFrame to categorize couples based on their
        educational background, including 'BothCollege', 'WifeOnly', 'HusbandOnly', and 'Neither'.

        """
        self.df['BothCollege'] = (self.df['wc_encoded'] == 1) & (self.df['hc_encoded'] == 1)
        self.df['WifeOnly'] = (self.df['wc_encoded'] == 1) & (self.df['hc_encoded'] == 0)
        self.df['HusbandOnly'] = (self.df['wc_encoded'] == 0) & (self.df['hc_encoded'] == 1)
        self.df['Neither'] = (self.df['wc_encoded'] == 0) & (self.df['hc_encoded'] == 0)

    def plot_lfp_by_education(self):
        """
        Plot the labor force participation rate by the educational background of couples.

        This method groups the data by 'BothCollege', 'WifeOnly', 'HusbandOnly', 'Neither', 
        calculates the normalized value counts as a proportion of 'lfp_encoded' for each group, 
        and then plots a stacked bar chart to visualize the labor force participation rate
        based on the educational background of couples.

        """
        grouped = self.df.groupby(['BothCollege', 'WifeOnly', 'HusbandOnly', 'Neither'])['lfp_encoded'].value_counts(normalize=True).unstack().fillna(0)

        grouped.plot(kind='bar', stacked=True)
        plt.title('Labor Force Participation by Educational Background of Couples')
        plt.xlabel('Educational Background')
        plt.ylabel('Proportion in Labor Force')
        plt.xticks(ticks=[0, 1, 2, 3], labels=['Both College', 'Wife Only', 'Husband Only', 'Neither'], rotation=0)
        plt.legend(title='Labor Force Participation', labels=['Not Participating', 'Participating'])
        plt.show()  # Plot the chart


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

class AgeGroupLFPVisualization:
    """
    A class for analyzing and visualizing labor force participation rates based on age groups.

    Args:
        df (pd.DataFrame): The DataFrame containing the data for visualization.
    """

    def __init__(self, df):
        """
        Initialize the AgeGroupLFPVisualization class with a DataFrame.

        """
        self.df = df

    def create_age_group_variable(self):
        """
        Create an age group variable in the DataFrame.

        This method adds a new column 'age_group' to the DataFrame, categorizing individuals into
        age groups 'Before 45' and '45 and After' based on their age.

        """
        self.df['age_group'] = self.df['age'].apply(lambda x: 'Before 45' if x < 45 else '45 and After')

    def plot_lfp_by_age_group(self):
        """
        Plot the labor force participation rate by age group.

        This method groups the data by 'age_group', calculates the mean of 'lfp_encoded' for each group,
        and then plots a bar chart to visualize the average labor force participation rate by age group.

        """
        age_group_lfp = self.df.groupby('age_group')['lfp_encoded'].mean().reset_index()

        plt.figure(figsize=(8, 6))
        sns.barplot(x='age_group', y='lfp_encoded', data=age_group_lfp)

        plt.xlabel('Age Group')
        plt.ylabel('Average Labor Force Participation Rate')
        plt.title('Labor Force Participation by Age Group of Married Women')

        plt.show()  # Plot the chart


