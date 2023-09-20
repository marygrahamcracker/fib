response = input('please enter maxium number of elements to print for fib sequences')

if not response.isnumeric():
    print('enter a number, dummy')
else:
    y = int(response)
    myoutput = ''
    if y > 0:
        myoutput += '0\t'
    if y > 1:
        myoutput += '1\t'
    if y > 2:
        previousNumber1 = 0
        previousNumber2 = 1
        for x in range(2, y):
            currentNumber = previousNumber1 + previousNumber2
            myoutput += f'{currentNumber}\t'
            previousNumber2 = currentNumber
    
    print(myoutput)