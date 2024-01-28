def uppercasefilter(test_list):
    res = []
    for tup in test_list:
        if all(char.isupper() for char in tup):
            res.append(tup)
    return res


test_list = [("GFG", "IS", "BEST"), ("GFG", "AVERAGE"), ("gFG", "CS")]
print(uppercasefilter(test_list))
