line_1 = "     _   _       _   _   _   _   _   _  "
line_2 = "  |  _|  _| |_| |_  |_    | |_| |_| | | "
line_3 = "  | |_   _|   |  _| |_|   | |_|  _| |_| "

i = 0
while i < 31:       # 27 characters + 9 spaces = 36 digits 
    print(line_1[i:i+3])
    print(line_2[i:i+3])
    print(line_3[i:i+3])
    i += 4