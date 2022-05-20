import math 

def welcome(): 
  print('Welcome to my first python cli calculator App, follow the instructions to use the calculator')

#To Proceed after the welcome
def proceed():
  calcOperation = input('''
Please type in the type of operation you want to execute.
N for normal Arimetic operations like addition, substraction and all
C for further arithmetic operations like square root, approximation...
  ''')
  if calcOperation.upper() == 'N':
    calculate()
  elif calcOperation.upper() == 'C':
    complexcalc()
  else:
    print("select a valid operation")

#Perform basic arithmetic operations
def calculate():
  operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
** for power
% for modulo
sqrt for squareroot
''')

  number_1 = int(input('Please enter the first number: '))
  number_2 = int(input('Please enter the second number: '))

  if operation == '+':
      print('{} + {} = '.format(number_1, number_2))
      print(number_1 + number_2)

  elif operation == '-':
      print('{} - {} = '.format(number_1, number_2))
      print(number_1 - number_2)

  elif operation == '*':
      print('{} * {} = '.format(number_1, number_2))
      print(number_1 * number_2)

  elif operation == '/':
      print('{} / {} = '.format(number_1, number_2))
      print(number_1 / number_2)
  
  elif operation == '**':
      print('{} ** {} = '.format(number_1, number_2))
      print(number_1 ** number_2)
  
  elif operation == '%':
      print('{} % {} = '.format(number_1, number_2))
      print(number_1 % number_2)

  else:
      print('You have not typed a valid operator, please run the program again.')

  # To ask user if they want to perform another operation
  again()

# This is where we perform complex operation
def complexcalc():
  complexOperator = input('''
Which operation will you like to carry out
sqrt for Squareroot
''')

  value = int(input('Input a number: '))

  if complexOperator == 'sqrt':
    print('The square root of ' + str(value) + ' is ' + str(math.sqrt(value)))
  else:
      print('You have not typed a valid operator, please run the program again.')
  
  #To rerun the program
  again()

#The again function
def again():
  calc_again = input('''
Do you want to run the calculator again?
Please type Y for YES or N for NO.
''')

  if calc_again.upper() == 'Y':
    proceed()
  elif calc_again.upper() == 'N':
    print('Thanks for using my calculator app')
  else:
    again()

welcome()
proceed()
