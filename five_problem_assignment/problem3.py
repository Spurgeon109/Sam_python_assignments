def my_map(func, itr):
    l = [func(i) for i in itr]
    return iter(l)

def my_filter(func, itr):
    l = []
    for i in itr:
        if func(i) == True: l.append(i)
    return iter(l)


f = lambda x: x > 2
l = lambda x: x*x
print(list(my_map(l, [1, 2, 3, 4 ])))
print(list(my_filter(f, [1, 1, 2, 3, 4, 5])))