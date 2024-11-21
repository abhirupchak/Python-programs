# WAP to print the words in a file in reverse order

def reverse_words_in_file(filename):
    with open(filename, 'r') as file:
        words = file.read().split()
    print(' '.join(reversed(words)))

reverse_words_in_file("sample.txt")
