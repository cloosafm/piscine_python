from sys import argv
import ft_filter




def isanumber(item):
    return isinstance(item, int)


def main():
    ft_list = ["Hello", "tata!", 5]
    ft_tuple = ("Hello", "toto!", 6)
    ft_set = {"Hello", "tutu!", 7}

    truthy_values = ft_filter(isanumber, ft_list)
    print(list(truthy_values))

    truthy_values = ft_filter(isanumber, ft_tuple)
    print(tuple(truthy_values))
    
    truthy_values = ft_filter(isanumber, ft_set)
    print(set(truthy_values))




if __name__ == "__main__":
    main()

