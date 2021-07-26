#print(1/0)
#ZeroDivisionError: division by zero

#print(4+'spam')
#TypeError

#print(4 + spam)
#NameError

x = input('enter int >> ')
while True:
    try:
        y = x % 2
        print(y)
        break
    except ValueError:
        print("Try again....")
        break
    except TypeError:
        print('NoonoType')
        break