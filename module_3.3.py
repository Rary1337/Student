def print_params(a = 1, b = "строка", c = True):
    print(a,b,c)


print_params(b = 25, c = [1,2,3])

value_list = [35, 'Boom', True]
value_dict = {'a' : 1, 'b' : 'строка', 'c' : True}

print_params(*value_list)
print_params(**value_dict)

value_list2 = (1,'Zorg')
print_params(*value_list2, 42)