import translator, digits, writer, checksum, alternatives


def parse_dictionary(dic):

    index = 0
    newfile = "account_numbers_after_cleaning.txt"

    while (index + 4) < len(dic):
        position = 0
        account_numbers = []    # onelist for actual accounts to print to file

        line_1 = dic[index+1]
        line_2 = dic[index+2]
        line_3 = dic[index+3]
            
        while position < 33:       # 27 characters + 9 spaces = 36 digits 
            single = []
            
            single.append(line_1[position:position+3])
            single.append(line_2[position:position+3])
            single.append(line_3[position:position+3])
           
            single = translator.translate(single) 
            
            if single in digits.translation:    # check if single is value in translation_dic and if yes return key
                check = digits.translation.index(single)
                account_numbers.append(check)
                position += 4

            else:
                account_numbers.append('?')
                questionmark = single
                position += 4

        if '?' in account_numbers:
            account_numbers.append(" ILL")
            writer.write_file(account_numbers, "Accountnumbers_as_read.txt")
            account_numbers.pop()
            account_numbers = alternatives.illegible(account_numbers, questionmark)    #-> add to second file
            writer.write_file(account_numbers, newfile)

        elif checksum.checksum(account_numbers) == False:
            account_numbers.append(" ERR")
            writer.write_file(account_numbers, "Accountnumbers_as_read.txt")
            account_numbers.pop()
            account_numbers = alternatives.wrong_checksum(account_numbers) #wrong checksum    -> add to second file
            writer.write_file(account_numbers, newfile)

        else:
            writer.write_file(account_numbers, "Accountnumbers_as_read.txt")
            writer.write_file(account_numbers, newfile)

        index += 4
