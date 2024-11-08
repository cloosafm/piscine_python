import numpy as np


def give_bmi(height: list[int | float], weight: list[int | float]) \
            -> list[int | float]:
    """
    Calculate the BMI for each person in the list.
    BMI = weight / (height * height).
    Units are kilograms and meters.
    Args:
        height (list): The list of heights.
        weight (list): The list of weights.
    Returns:
        list: The list of BMIs.
    """
    height_len = len(height)
    weight_len = len(weight)
    try:
        if height_len == 0 or weight_len == 0:
            raise AssertionError("lists cannot be empty")
        if not isinstance(height, (list)) or not isinstance(weight, (list)):
            raise AssertionError("must be lists")
        if weight_len != height_len:
            raise AssertionError("lists have different lengths")
        for h, w in zip(height, weight):
            if isinstance(h, bool) or \
                    not isinstance(h, (int, float)) or h <= 0:
                raise AssertionError("height must be greater than 0, \
                                     int or floats.")
            if isinstance(w, bool) or \
                    not isinstance(w, (int, float)) or w <= 0:
                raise AssertionError("weight must be greater than 0, \
                                     int or floats.")
    except AssertionError as e:
        print(f"AssertionError: {e}")
        return None
    else:
        return [w / (h * h) for h, w in zip(height, weight)]


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Check whether given BMI is above the limit ("True") or not ("False").
    Args:
        bmi (list): The list of BMIs.
        limit (int): The limit to check against.
    Returns:
        list: The list of booleans checking BMIs against given limit.
    """
    try:
        if not isinstance(bmi, (list)):
            raise AssertionError("BMI must be a list")
        if len(bmi) == 0:
            raise AssertionError("BMI list cannot be empty")
        for value in bmi:
            if isinstance(value, bool) or not isinstance(value, (int, float)) \
                         or value <= 0:
                raise AssertionError("BMI must be greater than 0, \
                                    int or float")
        if isinstance(limit, bool) or not isinstance(limit, int) or limit <= 0:
            raise AssertionError("limit must be an integer greater than 0")
    except AssertionError as e:
        print(f"AssertionError: {e}")
        return None
    else:
        bmi_array = np.array(bmi)
        result = []

        for value in np.nditer(bmi_array):
            if value < limit:
                result.append(False)
            else:
                result.append(True)
        return result
