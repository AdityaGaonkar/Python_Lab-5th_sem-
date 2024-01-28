def check_divisiblity(test_list, k):
    res = []
    for test in test_list:
        if all(elem % k == 0 for elem in test):
            res.append(test)
    return res


test_list = [(6, 24, 2), (60, 12, 6), (12, 18, 21)]
K = 6
print(check_divisiblity(test_list, K))
