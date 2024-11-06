from load_csv import load
from matplotlib import pyplot as plt, ticker



def plot_projection_life(df_gdp, df_life):
    """
    Plots the projection of life expectancy for France and Belgium
    """



def main():
    """
    Loads a csv file and displays its info about France and Belgium
    """
    df_gdp = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    df_life = load("life_expectancy_years.csv")

    if df_gdp is not None and df_life is not None:
        plot_projection_life(df_gdp, df_life)


if __name__ == "__main__":
    main()