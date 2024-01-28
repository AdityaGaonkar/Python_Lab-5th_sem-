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

n = int(input("Enter a number of elements"))

ans = []

for i in range(n):
    a = int(input("Enter the number "))
    ans.append(a)

even_sum = odd_sum = 0

for i in ans:
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i

print("Even sum is ", even_sum)
print("Odd sum is ", odd_sum)

n = int(input("Enter a number of elements"))

ans = []
fans = []

for i in range(n):
    a = int(input("Enter the number "))
    ans.append(a)

for i in range(n):
    if i % 2 != 0: fans.append(ans[i])

print(fans)

n = int(input("Enter a number of elements"))

ans = []

for i in range(n):
    a = int(input("Enter the number "))
    ans.append(a)

fans = list(set(ans))

print(ans)
print(set(ans))