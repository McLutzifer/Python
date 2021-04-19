#import sys

fulename = "/home/lukas/Documents/Programming/Python/BANK/testfile.txt"

def read_file(filename):
    num_dic = {}
    with open(filename, 'r') as file:
        lines = file.readlines()

        count = 0
        for line in lines:
            count += 1
            num_dic[count] = line

        if len(num_dic) %4 != 0:
            print("ERROR")

    print(len(num_dic))
    return num_dic

x = read_file(fulename)
