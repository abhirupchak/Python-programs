# WAP to read a file and print the total number of characters, words, and lines

def file_statistics(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        num_lines = len(lines)
        num_words = sum(len(line.split()) for line in lines)
        num_chars = sum(len(line) for line in lines)
    print(num_chars, num_words, num_lines)

file_statistics("abc.txt")
