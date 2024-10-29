import numpy as np


def give_bmi(height: list[int | float], weight: list[int | float]) \
            -> list[int | float]:
    """
    Calculate the BMI for each person in the list.
    BMI = weight / (height * height)
    Units are kilograms and meters
    """
    height_len = len(height)
    weight_len = len(weight)
    try:
        if weight_len != height_len:
            raise AssertionError("lists have different lengths")
        for h, w in zip(height, weight):
            if not isinstance(h, (int, float)) or h <= 0:
                raise AssertionError("must be int or floats, and positive.")
            if not isinstance(w, (int, float)) or w <= 0:
                raise AssertionError("must be int or floats, and positive.")
    except AssertionError as e:
        print(f"AssertionError: {e}")
    return [w / (h * h) for h, w in zip(height, weight)]


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Check whether given BMI is above the limit ("True") or not ("False").
    """
    bmi_array = np.array(bmi)
    result = []

    for value in np.nditer(bmi_array):
        if value < limit:
            result.append(False)
        else:
            result.append(True)
    return result
