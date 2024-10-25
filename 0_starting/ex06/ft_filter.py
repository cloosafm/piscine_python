# from sys import argv




# def isanumber(item):
#     return isinstance(item, int)

def ft_filter(function, iterable) -> iter:
    """
    ft_filter(function or None, iterable) --> filter object
    
    Return an iterator yielding those items of iterable for which function(item)
    is true. If function is None, return the items that are true.
    
    """
    if function is None:
        return [item for item in iterable if item]
    for item in iterable:
        return [item for item in iterable if function(item)]


# def main():
#     ft_list = ["Hello", "tata!", 5]
#     ft_tuple = ("Hello", "toto!", 6)
#     ft_set = {"Hello", "tutu!", 7}

#     truthy_values = ft_filter(isanumber, ft_list)
#     print(list(truthy_values))

#     truthy_values = ft_filter(isanumber, ft_tuple)
#     print(tuple(truthy_values))
    
#     truthy_values = ft_filter(isanumber, ft_set)
#     print(set(truthy_values))




# if __name__ == "__main__":
#     main()

