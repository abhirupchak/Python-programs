# WAP to calculate the frequency of each character in a file

def character_frequency_in_file(filename):
    freq = {}
    with open(filename, 'r') as file:
        text = file.read()
        a=0
        for char in text:
            a+=1
            freq[char] = a
    print(freq)

character_frequency_in_file("textfile.txt")
