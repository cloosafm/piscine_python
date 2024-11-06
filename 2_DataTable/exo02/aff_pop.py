from load_csv import load
from matplotlib import pyplot as plt, ticker


def pop_to_float(pop_str: str) -> float:
    """
    Convert a population string with suffix to a float.
    Args:
        pop_str (str): The population string (e.g., '3.28M').
    Returns:
        float: The population as a float.
    """
    if pop_str.endswith('M'):
        return float(pop_str[:-1]) * 1e6
    elif pop_str.endswith('k'):
        return float(pop_str[:-1]) * 1e3
    else:
        return float(pop_str)


def plot_country_data(df, country1: str, country2: str) -> None:
    """
    Plot the data showing two specific countries.
    Args:
        df : The DataFrame containing the data.
        country1 (str): The name of the 1st country to plot.
        country2 (str): The name of the 2nd country to plot.
            """
    if df is not None:
        # Transpose the DataFrame
        df_transposed = df.T
        # Set the first row as the header using loc
        df_transposed.columns = df_transposed.loc[df_transposed.index[0]]
        df_transposed = df_transposed.loc[df_transposed.index[1:]]
        # Set index to years, convert to int
        df_transposed.index = df_transposed.index.astype(int)
        # Check if the specified countries exist in the DataFrame
        if country1 not in df_transposed.columns:
            print(f"Error: The country '{country1}' does not exist.")
            return
        if country2 not in df_transposed.columns:
            print(f"Error: The country '{country2}' does not exist.")
            return

        # keep only rows between 1800 and 2050
        df_transposed = df_transposed.loc[1800:2050]

        # Convert population values to floats
        df_transposed[country1] = df_transposed[country1].apply(pop_to_float)
        df_transposed[country2] = df_transposed[country2].apply(pop_to_float)

        # Plot the data for the specified countries
        fig, ax = plt.subplots()
        ax.plot(df_transposed.index, df_transposed[country1], label=country1,
                color='b')
        ax.plot(df_transposed.index, df_transposed[country2], label=country2,
                color='g')

        # Customize ticks on the x-axis
        min_year = df_transposed.index.min()
        max_year = df_transposed.index.max()
        # min_year = 1800
        # max_year = 2050
        ax.set_xticks(range(min_year, max_year, 40))

        # Customize ticks on the y-axis to be every 20 million
        min_pop = max(20_000_000, int(min(df_transposed[country1].min(),
                                          df_transposed[country2].min())))
        max_pop = int(max(df_transposed[country1].max(),
                          df_transposed[country2].max()))
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
