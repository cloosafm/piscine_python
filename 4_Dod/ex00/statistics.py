def arg_ok(*args: any) -> bool:
    """Check if all arguments are numbers
        Args:
            *args: list of numbers
        Returns:
            True if all arguments are numbers, False and "ERROR" otherwise
    """
    if not args:
        print("ERROR")
        return False
    for value in args:
        if not isinstance(value, (int, float)):
            print("ERROR")
            return False
    return True


def ft_statistics(*args: any, **kwargs: any) -> None:
    """Compute statistics on a list of numbers
        Stats are: mean, median, quartile, variance, standard deviation
        Args:
            *args: list of numbers
            **kwargs: list of statistics to compute
    """
    for value in kwargs.values():
        match value:
            case 'mean':
                if arg_ok(*args):
                    print("mean :", sum(args) / len(args))
            case 'median':
                if arg_ok(*args):
                    print("median :", sorted(args)[len(args) // 2])
            case 'quartile':
                if arg_ok(*args):
                    first_quart = sorted(args)[len(args) // 4]
                    third_quart = sorted(args)[3 * len(args) // 4]
                    print_quart = [float(first_quart), float(third_quart)]
                    print("quarter :", print_quart)
            case 'var':
                if arg_ok(*args):
                    mean_value = sum(args) / len(args)
                    var = sum((i - mean_value) ** 2 for i in args) / len(args)
                    print("var :", var)
            case 'std':
                if arg_ok(*args):
                    mean_value = sum(args) / len(args)
                    var = sum((i - mean_value) ** 2 for i in args) / len(args)
                    std_dev = var ** 0.5
                    print("std :", std_dev)
