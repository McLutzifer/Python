def read_file(filename):
    read_lines = {}
    try:
        with open(my_test_file, 'r') as file:
            lines = file.readlines()

            count = 0
            for line in lines:
                count += 1
                read_lines[count] = line

            #if len(read_lines) %4 != 0:
                #error_input()
    except:
        print("An Error occured - unable to read file")

    #return read_lines