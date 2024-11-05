from load_csv import load
from matplotlib import pyplot as plt


def main():
    """
    Loads a csv file and displays its info about France
    """
    life_data = load("life_expectancy_years.csv")
    if life_data is not None:
        life_data = life_data.T
        life_data.columns = life_data.loc['France']
        # life_data = life_data[1:]
        print(life_data)
        plt.plot(life_data.loc["France"])

        # plt.xlabel('Category')
        # plt.ylabel('Values')
        # plt.title('Bar Chart from CSV')
        # plt.show()


if __name__ == "__main__":
    main()
