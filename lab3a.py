#!/usr/bin/env python3

# return_text_value() function

# 'Author ID:' 146466230

def return_text_value():
    name = 'Terry'
    greeting = 'Good Morning ' + name 
    return greeting
return_text_value()

# return_number_value() function

def return_number_value():
    num1 = 10
    num2 = 5
    num3 = num1 + num2
    return num3


# Main Program

# print('python code') # this is to test that main function is indeed not being executed when imported into another python file. Anything below the main function will not be imported.

if __name__ == '__main__':
    print('python code')
    text = return_text_value()
    print(text)
    number = return_number_value()
    print(str(number))
    
