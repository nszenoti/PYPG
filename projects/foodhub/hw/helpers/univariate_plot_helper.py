# write a clas that helps to draw plots for univariate analysis (ie plotter helper class)
from matplotlib import pyplot as plt
import pandas as pd

import primitve_helpers as ph


class UnivariatePlotHelper:
    def __init__(self, df: pd.DataFrame):
        self.df = df
    # NOTE: these are generated methods by copilot
    def plot_univariate(self, column: str, kind: str = 'hist', bins: int = 10, **kwargs):
        '''
        Plot univariate analysis for a given column
        Args:
            column (str): column name
            kind (str): type of plot, default is 'hist'
            bins (int): number of bins, default is 10
            kwargs: additional arguments to be passed to the plot function
        '''
        # Get the column data
        data = self.df[column]

        # Plot the data
        if kind == 'hist':
            data.plot(kind=kind, bins=bins, **kwargs)
        else:
            data.plot(kind=kind, **kwargs)

        # Set the title
        plt.title(ph.snake_to_pascal(column))

        # Show the plot
        plt.show()

    def plot_univariate_categorical(self, column: str, kind: str = 'bar', **kwargs):
        '''
        Plot univariate analysis for a given column
        Args:
            column (str): column name
            kind (str): type of plot, default is 'bar'
            kwargs: additional arguments to be passed to the plot function
        '''
        # Get the column data
        data = self.df[column]

        # Plot the data
        data.value_counts().plot(kind=kind, **kwargs)

        # Set the title
        plt.title(ph.snake_to_pascal(column))

        # Show the plot
        plt.show()