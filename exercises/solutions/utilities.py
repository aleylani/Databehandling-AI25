# Välkommen till din .py-fil med nyttiga funktioer
# genom att spara användbara funktioner här kan du enkelt importera och återanvända dem

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def find_columns_with_nulls_and_plot(df: pd.DataFrame) -> None:

    '''Identifies all columns in a DataFrame containing any null values, and plots a histogram for each of them.'''

    for column in df.columns:         # iterera över alla kolumner i vår dataframe

        if df[column].isnull().sum() > 0:
        
            sns.histplot(df, x=column)
            plt.title(f'Column: {column}')
            plt.show()

def find_and_plot_missing_value_counts(df: pd.DataFrame) -> None:

    missing_counts = df.isnull().sum()

    missing_more_than_zero = missing_counts[missing_counts > 0]

    x_values = missing_more_than_zero.index
    y_values = missing_more_than_zero.values

    sns.barplot(x=x_values, y=y_values)
    plt.title('Missing value counts per column')
    plt.show()