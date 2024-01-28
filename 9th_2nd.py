def vowel_count(str):
    vowels = 'AEIOUaeiou'
    count = 0
    for char in str:
        if char in vowels:
            count += 1
    return count


def printt(str):
    filteredchar = ""
    for char in str:
        if char not in ['s', 'e']:
            filteredchar += char
    print(filteredchar)


strings = input("enter the string\n")
count = vowel_count(strings)
print(f'number of vowels are {count}')
