# WAP to calculate the frequency of each character in a file

def character_frequency_in_file(filename):
    freq = {}
    with open(filename, 'r') as file:
        text = file.read()
        for char in text:
            freq[char] = freq.get(char, 0) + 1
    print(freq)

character_frequency_in_file("sample.txt")
