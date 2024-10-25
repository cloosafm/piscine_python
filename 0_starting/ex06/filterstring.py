from sys import argv
from ft_filter import ft_filter




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

	# aquarium_tanks = [11, False, 18, 21, "", 12, 34, 0, [], {}]
	# lambda word : len word > N, iterator
	# print(test)
    # print(official)



if __name__ == "__main__":
    main()

