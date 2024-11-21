from load_csv import load
from matplotlib import pyplot as plt, ticker
from math import log10, floor
# import mplcursors


class Convert:
    """Class for converting strs with units to actual numbers"""

    def __init__(self):
        """Constructor for the Convert class"""
        # Define a dictionary for unit conversions
        self.unit_map = {
            'k': 1e3,      # Thousand
            'M': 1e6,      # Million
            'B': 1e9       # Billion
        }

    def convert_to_float(self, value: str) -> float:
        """
        Convert a string with units to a float.
        Args:
            value (str): The string with units (e.g., '3.28M').
        Returns:
            float: The value as a float.
        """
        try:
            # If the value is already a number, return it as float
            return float(value)
        except ValueError:
            pass

        # Check for units in the value string
        for unit, multiplier in self.unit_map.items():
            if value.endswith(unit):
                # Extract number and multiply by the corresponding unit
                number = float(value[:-len(unit)])
                return number * multiplier

        # If no unit is found, raise an exception
        raise ValueError(f"Unknown unit in value: {value}")


def plot_projection_life(df_gdp, df_life, year: int):
    """
    Plots the projection of life expectancy in relation to the GDP.
    Args:
        df_gdp : The DataFrame containing the GDP data.
        df_life : The DataFrame containing the life expectancy data.
        year (int): The year for the projection.
    """
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
    try:
        df_gdp = df_gdp.map(convert.convert_to_float)
    except ValueError as e:
        print(f"Error: {e}")
        return None

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
    # scatter = ax.scatter(df_gdp.loc[year], df_life.loc[year])

    # Set the x-axis limits, to ensure plotting shows necessary values only
    # Calculate the minimum and maximum values in the x-axis data
    min_gdp = df_gdp.loc[year].min()
    max_gdp = df_gdp.loc[year].max()
    # Determine the lowest and highest hundred values for x-axis
    start_value = (min_gdp // 100) * 100
    end_value = 10 ** floor(log10(max_gdp))
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

    # Add a cursor to display the country, GDP and life expectancy
    # cursor = mplcursors.cursor(scatter)
    # cursor.connect(
    #     "add",
    #     lambda sel: sel.annotation.set_text(
    #         "Country: {}\nGDP: {}\nLife expectancy: {}".format(
    #             df_gdp.columns[sel.index], sel.target[0], sel.target[1]
    #         )
    #     ),
    # )

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
        # Check both DataFrames have same countries
        if not all((df_gdp.iloc[i, 0] == df_life.iloc[i, 0]
                    for i in range(df_gdp.shape[0]))):
            print("Error: DataFrames have different countries.")
            return
        # Check if the specified year exists in the DataFrames
        if (str(year) not in df_gdp.columns and
                str(year) not in df_life.columns):
            print(f"Error: The year {year} is inexistent in both DataFrames.")
            return
        elif str(year) not in df_gdp.columns:
            print(f"Error: Year {year} is inexistent in the GDP DataFrame.")
            return
        elif str(year) not in df_life.columns:
            print(f"Error: Year {year} is inexistent in the LE DataFrame.")
            return
        plot_projection_life(df_gdp, df_life, year)


if __name__ == "__main__":
    main()
