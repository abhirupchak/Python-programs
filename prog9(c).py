# WAP to print the words in a file in reverse order

def reverse_words_in_file(filename):
    with open(filename, 'r') as file:
        f=file.read()
        s=""
        for i in range(len(f),0,-1):
            s=""
            s+=f[i]
        print(s)

reverse_words_in_file("textfile.txt")
