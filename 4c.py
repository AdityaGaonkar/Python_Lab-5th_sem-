def item_in_list(tuplee, listt):
    count = 0
    for item in listt:
        if item in tuplee:
            count += tuplee.count(item)
    return count


tuplee = ('a', 'a', 'a', 'bl', 'd')
listt = ['a', 'b']
print(item_in_list(tuplee, listt))
