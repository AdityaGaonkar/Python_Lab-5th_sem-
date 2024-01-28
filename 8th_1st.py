str = input("enter the file name\n")
try:
    with open(str) as file:
        content = file.read()
    num_sentences = len(content.split("."))
    num_words = len(content.split())
    num_char = len(content)
    print("number of sentences are ", num_sentences)
    print("mumber of words are ", num_words)
    print("numer of characters are ", num_char)
except FileNotFoundError:
    print(f'file {content} not found')
