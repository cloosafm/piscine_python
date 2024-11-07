from load_csv import load
from matplotlib import pyplot as plt, ticker



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


    # Check if the specified year exists in the DataFrames
    # if year not in df_gdp.index:
    #     print(f"Error: The year {year} does not exist in gdp.")
    #     return
    # if year not in df_life.index:
    #     print(f"Error: The year {year} does not exist in life.")
    #     return


    # Set the first row of each Dataframe as the header using loc
    df_gdp.columns = df_gdp.loc[df_gdp.index[0]]
    df_gdp = df_gdp.loc[df_gdp.index[1:]]
    df_life.columns = df_life.loc[df_life.index[0]]
    df_life = df_life.loc[df_life.index[1:]]
    # Set indexes to years, convert to int
    df_gdp.index = df_gdp.index.astype(int)
    df_life.index = df_life.index.astype(int)

    # plot type : scatter
    fig, ax = plt.subplots()
    ax.scatter(df_gdp.loc[year], df_life.loc[year])

    # Customize the x-axis to be logarithmic
    ax.set_xscale('log')

    # Apply the custom formatter to the x-axis
    formatter = ticker.EngFormatter(sep="")
    ax.xaxis.set_major_formatter(formatter)

    logfmt = ticker.LogFormatterSciNotation()
    ax.xaxis.set_minor_formatter(logfmt, minor_thresholds=)

    # Calculate the minimum value in the x-axis data
    min_gdp = df_gdp.loc[year].min()

    # Determine the lowest hundred value less than or equal to the minimum value
    start_value = (min_gdp // 100) * 100

    # Set x-axis limits to start at the calculated value
    ax.set_xlim(left=start_value)


    # Add labels, legend and title
    ax.set_xlabel('Gross domestic product')
    ax.set_ylabel('Life Expectancy')
    ax.set_title(f"{year}")

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