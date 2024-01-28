listt = []
n = int(input("enter the number of elements\n"))
for i in range(0, n):
    ele = int(input("enter the number\n"))
    listt.append(ele)
    if ele % 4 == 0 and ele % 5 != 0:
        print(ele)
    else:
        continue
print(listt[1])