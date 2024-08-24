def addDigits(num):
        if num < 10:
            return num
        else:
            number = 0
            string = str(num)
            listOfDigits = []
            for i in string:
                number += int(i)
            return addDigits(number)
            

#num = 8
#num = 38
num = 55
print(addDigits(num))