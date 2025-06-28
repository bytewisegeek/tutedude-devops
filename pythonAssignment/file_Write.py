with open('file.txt', 'w') as file:
    file.write("Hello\n")
    file.write("Another line.\n")   
    file.close
    
    #read
with open('file.txt', 'r') as file:    
    lines = file.readlines()
    print(lines)
    file.close
