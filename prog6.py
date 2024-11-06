#WAP that accepts char, perform the following:
#a. print whether the char is letter or numeric or special chr
def check(char1):
    if char1.isalpha()==True:
        print("char is letter")
    elif char1.isdigit()==True:
        print("char is number")
    else:
        print("char is special char")
char1=print("Enter char:")
check(char1)
#b. if the char is a letter print whether uppercase or lowercase
def case(char1):
    if char1.isupper()==True:
        print("upper case")
    if char1.islower()==True:
        print("Lower case")
    else:
        print("char is not letter")
case(char1)
#c. if the character is numric digit print its name in text
def name(char2):
    dict_1={0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"}
    if char2.isdigit()==True:
        for i in dict_1:
            if i == char2:
                print("digit in letter is:",dict_1[i])
            else:
                pass
char2=int(input("enter number:"))