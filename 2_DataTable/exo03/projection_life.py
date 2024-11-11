from load_csv import load
from matplotlib import pyplot as plt, ticker
import mplcursors
import numpy as np


def str_to_float(value):
    """
    Convert a string to a float.
    
    Args:
        value (str): The string to convert.
    
    Returns:
        float: The converted float value.
    """
    if isinstance(value, str):
        if value.endswith('M'):
            return float(value[:-1]) * 1e6
        elif value.endswith('K'):
            return float(value[:-1]) * 1e3
    return float(value)

def handleEvent(event, df_gdp, df_life, year, countries):
    """
    Handle the event when a point in the scatter plot is clicked.
    
    Args:
        event: The event object.
        df_gdp (pd.DataFrame): The GDP DataFrame.
        df_life (pd.DataFrame): The life expectancy DataFrame.
        year (int): The year for the projection.
        countries (list): The list of country names.
    """
    if event.inaxes:
        # Get the x and y data from the event
        xdata = event.xdata
        ydata = event.ydata
        print(f"Clicked on point: ({xdata}, {ydata})")
        
        # Find the closest point in the scatter plot
        gdp_values = np.array(df_gdp.loc[year].values)
        life_values = np.array(df_life.loc[year].values)
        distances = np.sqrt((gdp_values - xdata)**2 + (life_values - ydata)**2)
        min_index = np.argmin(distances)
        
        # Print the country name, GDP, and life expectancy
        country = countries[min_index]
        gdp = gdp_values[min_index]
        life_expectancy = life_values[min_index]
        print(f"Country: {country}, GDP: {gdp}, Life Expectancy: {life_expectancy}")

def plot_projection_life(df_init_gdp, df_init_life, year: int):
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


    # Apply the str_to_float function to all columns except the first column
    df_gdp = df_init_gdp.copy()
    df_life = df_init_life.copy()
    df_gdp.iloc[:, 1:] = df_gdp.iloc[:, 1:].applymap(str_to_float)
    df_life.iloc[:, 1:] = df_life.iloc[:, 1:].applymap(str_to_float)

    # Transpose the DataFrames
    df_gdp = df_gdp.T
    df_life = df_life.T


    # Set the first row of each Dataframe as the header using loc
    df_gdp.columns = df_gdp.loc[df_gdp.index[0]]
    df_gdp = df_gdp.loc[df_gdp.index[1:]]
    df_life.columns = df_life.loc[df_life.index[0]]
    df_life = df_life.loc[df_life.index[1:]]





    # Set indexes to years, convert to float
    df_gdp.index = df_gdp.index.astype(float)
    df_life.index = df_life.index.astype(float)

    # Get the list of countries
    countries = df_gdp.columns.tolist()


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


    # fig.canvas.mpl_connect('button_press_event', lambda event: handleEvent(event, df_gdp, df_life, year, countries))


    cursor = mplcursors.cursor(
        plt.scatter(df_gdp.astype(float), df_life.astype(float))
    )
    cursor.connect(
        "add",
        lambda sel: sel.annotation.set_text(
            "Country: {}\nGDP: {}\nLife expectancy: {}".format(
                df_gdp["country"][sel.index], sel.target[0], sel.target[1]
            )
        ),
    )




    # Add labels, legend and title
    ax.set_xlabel('Gross domestic product')
    ax.set_ylabel('Life Expectancy')
    ax.set_title(f"{year}")

    plt.show()
    # plt.ion()


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