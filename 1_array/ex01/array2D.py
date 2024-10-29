import numpy


def check_args(family: list, start: int, end: int):
    """Check the args given for the slice_me fct"""
    if not isinstance(family, list):
        raise AssertionError("need a list as 1st arg")
    if not isinstance(start | end, int):
        raise AssertionError("need an int for start | end")

    # Adjust for negative indices
    if start < 0:
        start += len(family)
    if end < 0:
        end += len(family)
    if start < 0 or start >= len(family):
        raise AssertionError("start position is outside list size")
    if end < 0 or end > len(family):
        raise AssertionError("end position is outside list size")
    if start >= end:
        raise AssertionError("end position is lower than start position")


def slice_me(family: list, start: int, end: int) -> list:
    """Take a list, a start and end position in this list
    Return the list sliced according to given positions"""
    try:
        check_args(family, start, end)
    except AssertionError as e:
        print(f"AssertionError: {e}")
        return None
    fam_array = numpy.array(family)
    print(f"My shape is : {fam_array.shape}")
    sliced_fam = fam_array[start:end]
    print(f"My new shape is : {sliced_fam.shape}")
    # need to revert to a list because of output format of arrays
    family = sliced_fam.tolist()
    return family
