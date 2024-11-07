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
    # Set the first row of each Dataframe as the header using loc
    df_gdp.columns = df_gdp.loc[df_gdp.index[0]]
    df_gdp = df_gdp.loc[df_gdp.index[1:]]
    df_life.columns = df_life.loc[df_life.index[0]]
    df_life = df_life.loc[df_life.index[1:]]
    # Set indexes to years, convert to int
    df_gdp.index = df_gdp.index.astype(int)
    df_life.index = df_life.index.astype(int)

# plot type : scatter

def main():
    """
    Loads csv files for gross domestic product and life expectancy.
    Plots the projection for the given year.
    """
    df_gdp = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    df_life = load("life_expectancy_years.csv")

    if df_gdp is not None and df_life is not None:
        year = 1900
        plot_projection_life(df_gdp, df_life, year)


if __name__ == "__main__":
    main()