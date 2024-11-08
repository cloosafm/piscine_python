from load_csv import load
from matplotlib import pyplot as plt


def plot_country_data(df, country: str):
    """
    Plot the data for a specific country.

    Args:
        df : The DataFrame containing the data.
        country (str): The name of the country to plot.
    """
    # Transpose the DataFrame
    df_transposed = df.T
    # Set the first row as the header using loc
    df_transposed.columns = df_transposed.loc[df_transposed.index[0]]
    df_transposed = df_transposed.loc[df_transposed.index[1:]]
    # Set index to years, convert to int
    df_transposed.index = df_transposed.index.astype(float)
    # Check if the specified country exists in the DataFrame
    if country not in df_transposed.columns:
        print(f"Error: The country '{country}' does not exist.")
        return

    # Plot the data for the specified country
    plt.plot(df_transposed.index, df_transposed[country])
    # Customize ticks on the x-axis
    min_year = int(df_transposed.index.min())
    max_year = int(df_transposed.index.max())
    plt.xticks(range(min_year, max_year, 40))
    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Life expectancy')
    plt.title(f"{country} Life expectancy Projections")

    plt.show()


def main():
    """
    Loads a csv file and displays its info about France
    """
    df = load("life_expectancy_years.csv")
    if df is not None:
        plot_country_data(df, "France")


if __name__ == "__main__":
    main()
