def copy_lines_to_files(input_file):
    # Open the files for reading and writing
    infile = open(input_file, 'r')
    file1 = open('File1.txt', 'w')
    file2 = open('File2.txt', 'w')
    
    line_number = 1 
    for line in infile:
        if line_number % 2 == 0:
            file1.write(line)
        else:
            file2.write(line)
        line_number += 1  
      
    infile.close()
    file1.close()
    file2.close()

    print("Lines copied successfully to File1.txt and File2.txt.")
