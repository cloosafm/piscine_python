from load_csv import load
from matplotlib import pyplot as plt, ticker


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


def plot_country_data(df, country1: str, country2: str) -> None:
    """
    Plot the data showing two specific countries.
    Args:
        df : The DataFrame containing the data.
        country1 (str): The name of the 1st country to plot.
        country2 (str): The name of the 2nd country to plot.
            """
    # Transpose the DataFrame
    df = df.T
    # Set the first row as the header using loc
    df.columns = df.loc[df.index[0]]
    df = df.loc[df.index[1:]]
    # Set index to years, convert to int
    df.index = df.index.astype(float)
    # Check if the specified countries exist in the DataFrame
    if country1 not in df.columns:
        print(f"Error: The country '{country1}' does not exist.")
        return
    if country2 not in df.columns:
        print(f"Error: The country '{country2}' does not exist.")
        return

    # keep only rows between 1800 and 2050
    df = df.loc[1800:2050]

    # Convert population values to floats
    convert = Convert()
    try:
        df[country1] = df[country1].apply(convert.convert_to_float)
        df[country2] = df[country2].apply(convert.convert_to_float)
    except ValueError as e:
        print(f"Error: {e}")
        return None

    # Plot the data for the specified countries
    fig, ax = plt.subplots()
    ax.plot(df.index, df[country1], label=country1,
            color='b')
    ax.plot(df.index, df[country2], label=country2,
            color='g')

    # Customize ticks on the x-axis
    min_year = int(df.index.min())
    max_year = int(df.index.max())
    ax.set_xticks(range(min_year, max_year, 40))

    # Customize ticks on the y-axis to be every 20 million
    min_pop = max(20_000_000, int(min(df[country1].min(),
                                      df[country2].min())))
    max_pop = int(max(df[country1].max(),
                      df[country2].max()))
    ax.set_yticks(range(min_pop, max_pop + 1, 20_000_000))

    # Apply the custom formatter to the y-axis
    formatter = ticker.EngFormatter(sep="")
    ax.yaxis.set_major_formatter(formatter)

    # Add labels, legend and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Population')
    ax.set_title("Population Projections")
    ax.legend(loc='lower right')

    plt.show()


def main():
    """
    Loads a csv file and displays its info about France and Belgium
    """
    df = load("population_total.csv")
    if df is not None:
        plot_country_data(df, "Belgium", "France")


if __name__ == "__main__":
    main()
