data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

data_structure = list(data_structure)

summ = 0


def unpack_(list_):
    global summ
    for i in list_:
        if isinstance(i, list) or isinstance(i, tuple) or isinstance(i, set):
            unpack_(i)
        else:
            if isinstance(i, dict):
                for key, value in i.items():
                    if isinstance(key, int) or isinstance(key, float):
                        summ = summ + key
                    if isinstance(key, str):
                        summ = summ + len(key)
                    if isinstance(value, int) or isinstance(value, float):
                        summ = summ + value
                    if isinstance(value, str):
                        summ = summ + len(value)


            else:
                if (isinstance(i, int) or isinstance(i, float)):
                    summ = summ + i
                if isinstance(i, str):
                    summ = summ + len(i)
    return summ


print(unpack_(data_structure))
