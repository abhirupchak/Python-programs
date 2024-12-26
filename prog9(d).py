def copy_lines_to_files():
    inpfile = open('textfile.txt', 'r')
    file1 = open('File1.txt', 'w')
    file2 = open('File2.txt', 'w')
    
    line_number = 1 
    for line in inpfile:
        if line_number % 2 == 0:
            file1.write(line)
        else:
            file2.write(line)
        line_number += 1  
    inpfile.close()
    file1.close()
    file2.close()
copy_lines_to_files()
def readfiles():
    file1=open('File1.txt','r')
    file2=open('File2.txt','r')
    print(file1.read(),'\n',file2.read())
readfiles()
