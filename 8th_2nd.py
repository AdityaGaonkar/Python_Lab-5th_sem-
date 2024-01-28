def copy_lowerCase(input_filename, output_file_name):
    with open(input_filename, 'r') as file1:
        with open(output_file_name, 'w') as file2:
            num_lines_copied = 0
            for line in file1:
                for char in line:
                    if char.islower():
                        file2.write(char)
                    if any(char.islower() for char in line):
                        num_lines_copied += 1

            print(f"Number of lines with lowercase content: {num_lines_copied}")

    print(f'copied lower case from {input_filename} to {output_file_name}')


str = input("enter file name\n")
str2 = input("enter output file name\n")
copy_lowerCase(str, str2)
