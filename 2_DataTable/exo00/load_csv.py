from pandas import DataFrame as Dataset, read_csv


def load(path: str) -> Dataset:
    data_set = read_csv(path)
    return data_set