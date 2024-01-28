def symmetrical(s1, s2):
    if s1 == s2:
        print("symmetrical")
    else:
        print("not symmetrical")


def palindromic(s1, s2):
    if s1 == s2:
        print("palindrome")
    else:
        print("not palindrome")


s1 = input("enter the string\n")
length = len(s1)
m = length // 2
a1 = s1[:m]
a2 = s1[m:length]
symmetrical(a1, a2)
a3 = s1
a4 = s1[::-1]
palindromic(a3, a4)

