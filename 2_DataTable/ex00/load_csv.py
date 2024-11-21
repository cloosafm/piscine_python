from pandas import DataFrame as Dataset, read_csv, errors


def load(path: str) -> Dataset:
    """
    Returns dataset from file given in path
    Args:
        path (str): The path to the file.
    Returns:
        Dataset: The dataset as a pandas DataFrame.
    """
    try:
        data_set = read_csv(path)
    except FileNotFoundError:
        print(f"Error: The file at path '{path}' does not exist.")
        return None
    except errors.EmptyDataError:
        print(f"Error: The file at path '{path}' is empty.")
        return None
    except errors.ParserError:
        print(f"Error: The file at path '{path}' could not be parsed.")
        return None
    else:
        print(f"Loading dataset of dimensions {data_set.shape}")
        return data_set
