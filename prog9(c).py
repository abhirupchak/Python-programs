# WAP to print the words in a file in reverse order

def reverse_words_in_file(filename):
    with open(filename, 'r') as file:
        f=file.read()
        print(f[::-1])
reverse_words_in_file("textfile.txt")
