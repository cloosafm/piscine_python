import numpy


def slice_me(family: list, start: int, end: int) -> list:
    fam_array = numpy.array(family)
    print(f"My shape is : {fam_array.shape}")
    sliced_fam = fam_array[start:end]
    print(f"My new shape is : {sliced_fam.shape}")
    # need to revert to a list because of output format of arrays
    family = sliced_fam.tolist()
    return family