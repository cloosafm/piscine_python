from load_csv import load
from matplotlib import pyplot as plt, ticker, widgets
import numpy as np
from pint import UnitRegistry


class Convert:
    """Class for converting strs with units to actual numbers"""
    def __init__(self):
        """Constructor for the Convert class"""
        self.ureg = UnitRegistry()
        self.ureg.define("thousand = 1e3 = k")
        self.ureg.define("million = 1e6 = M")
        self.ureg.define("billion = 1e9 = B")

    def convert_to_float(self, value: str) -> float:
        """
        Convert a string with units to a float.
        Args:
            value (str): The string with units (e.g., '3.28M').
        Returns:
            float: The value as a float.
        """
        try:
            return float(value)
        except ValueError:
            return self.ureg(value).to_base_units().magnitude



def plot_projection_life(df_gdp, df_life, year: int):
    """
    Plots the projection of life expectancy in relation to the GDP.
    Args:
        df_gdp : The DataFrame containing the GDP data.
        df_life : The DataFrame containing the life expectancy data.
        year (int): The year for the projection.
    """
    # what if a country appears in only on csv file?
        # remove it from the other csv file?
        # print a warning message?

    # Transpose the DataFrames
    df_gdp = df_gdp.T
    df_life = df_life.T

    # Set the first row of each Dataframe as the header using loc
    df_gdp.columns = df_gdp.loc[df_gdp.index[0]]
    df_gdp = df_gdp.loc[df_gdp.index[1:]]
    df_life.columns = df_life.loc[df_life.index[0]]
    df_life = df_life.loc[df_life.index[1:]]

    # Convert GDP values to float
    convert = Convert()
    df_gdp = df_gdp.map(convert.convert_to_float)

    # Align the DataFrames based on their common columns and indexes
    common_countries = df_gdp.columns.intersection(df_life.columns)
    df_gdp = df_gdp[common_countries]
    df_life = df_life[common_countries]

    common_years = df_gdp.index.intersection(df_life.index)
    df_gdp = df_gdp.loc[common_years]
    df_life = df_life.loc[common_years]


    # Set indexes to years, convert to float
    df_gdp.index = df_gdp.index.astype(float)
    df_life.index = df_life.index.astype(float)




    # plot type : scatter
    fig, ax = plt.subplots()
    ax.scatter(df_gdp.loc[year], df_life.loc[year])

    # Set the x-axis limits, to ensure plotting shows necessary values only
    # Calculate the minimum and maximum values in the x-axis data
    min_gdp = df_gdp.loc[year].min()
    max_gdp = df_gdp.loc[year].max()
    # Determine the lowest and highest hundred values for x-axis
    start_value = (min_gdp // 100) * 100
    end_value = 10 ** np.floor(np.log10(max_gdp))
    ax.set_xlim(left=start_value, right=end_value)

    # Customize the x-axis to be logarithmic
    ax.set_xscale('log')


   # Set custom ticks to include 300
    xticks = [300] + [tick for tick in ax.get_xticks() if tick > 300]
    ax.set_xticks(xticks)
    # Apply the custom formatter to the x-axis
    formatter = ticker.EngFormatter(sep="")
    ax.xaxis.set_major_formatter(formatter)



    # Add labels, legend and title
    ax.set_xlabel('Gross domestic product')
    ax.set_ylabel('Life Expectancy')
    ax.set_title(f"{year}")


    # cursor = mplcursors.cursor(
    #     plt.scatter(df_gdp.astype(float), df_life.astype(float))
    # )
    # cursor = widgets.Cursor(ax, useblit=True, color='red', linewidth=2)
    # cursor.connect(
    #     "add",
    #     lambda sel: sel.annotation.set_text(
    #         "Country: {}\nGDP: {}\nLife expectancy: {}".format(
    #             df_gdp["country"][sel.index], sel.target[0], sel.target[1]
    #         )
    #     ),
    # )

    cursor = widgets.Cursor(ax, useblit=True, color='red', linewidth=2)
    plt.show()



def main():
    """
    Loads csv files for gross domestic product and life expectancy.
    Plots the projection for the given year.
    """
    df_gdp = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    df_life = load("life_expectancy_years.csv")

    if df_gdp is not None and df_life is not None:
        year = 1900
        # Ensure same number of rows (countries) in both DataFrames
        if df_gdp.shape[0] != df_life.shape[0]:
            print("Warning: The DataFrames have a different number of rows.")
            return
        # Check if the specified year exists in the DataFrames
        if str(year) not in df_gdp.columns and str(year) not in df_life.columns:
            print(f"Error: The year {year} is inexistent in both DataFrames.")
            return
        elif str(year) not in df_gdp.columns:
            print(f"Error: The year {year} is inexistent in the GDP DataFrame.")
            return
        elif str(year) not in df_life.columns:
            print(f"Error: The year {year} is inexistent in the Life Expectancy DataFrame.")
            return
        plot_projection_life(df_gdp, df_life, year)


if __name__ == "__main__":
    main()