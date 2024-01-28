def count_letter_histogram(s):
    letter_count = {}

    for char in s:
        if char.isalpha():  # Check if the character is a letter
            char = char.lower()  # Ignore case
            letter_count[char] = letter_count.get(char, 0) + 1

    print("Letter Histogram:")
    for letter, count in letter_count.items():
        print(f"{letter}: {count}")

input_string = input("Enter a string: ")
count_letter_histogram(input_string)