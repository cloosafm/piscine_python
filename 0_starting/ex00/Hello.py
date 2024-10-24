ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

"""main characteristics of data structures:

 ordered : elements have a defined order, and that order will not change.
    unordered : order of use/apparition of elements is not guaranteed.
    mutable : can be modified after creation.
    immutable : cannot be modified after creation
       if modif needed, you have to declare a new one
"""


# lists are ordered, mutable. They can contain duplicates
# defined with		[]
ft_list.pop(1)
ft_list.append("World!")

# tuples are ordered, immutable. They can contain duplicates
# defined with		()
ft_tuple = ("Hello", "France!")

# sets are unordered, mutable. They CANNOT contain duplicates
# defined with		{}
ft_set.discard("tutu!")
ft_set.add("Paris!")

# dictionaries are unordered, mutable (both keys and values).
# The keys must be unique, the values can be duplicated
# defined with		{}		key-value pairs are separated by a colon :
ft_dict["Hello"] = "42Paris!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
