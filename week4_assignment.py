import os
# function that writes, reads and modify files
def write_read_modify():
    with open("week4task.txt", 'w') as document:
        document.write("PLP academy is a tech platform worthy of recommendation to passion-driven mind. \n")
    
    with open("week4task.txt", 'r') as document:
        content = document.read()
        print(content)

    with open("week4task.txt", 'a') as document:
        document.write(" Learning Python with PLP has been an awesome experience.")
    
    with open("week4task.txt", 'r') as document:
       modify = document.read()
       print("modified: ", modify)
write_read_modify()

# user searching file
def search_file_by_user():
    input_file = input("Please enter name of file: ")
    try:
        if os.path.exists(input_file):
            print("file exists")
            with open(input_file, "r") as document:
                content = document.read()
                print(content)
        else:
            print("file doesn't exist")
    except:
        print("Error: Cannot read file")
search_file_by_user()