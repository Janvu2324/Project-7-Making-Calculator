
from art import logo
def add(a,b):
  return a+b
def sub(a,b):
  return a-b
def mul(a,b):
  return a*b
def div(a,b):
  return a/b

l={'+':add,
   '-':sub,
   '*':mul,
   '/':div}
def calculator():
  print(logo)
  a=float(input('What is the first number?: '))
  
  for i in l :
    print(i)
  
  should_continue=True
  while should_continue:
    operation=input('Pick the operation: ')
    b=float(input('What is the next number?: '))
    cal=l[operation]
    answer1=cal(a,b)
    print(f'{a}{operation}{b}={answer1}')
  
    conti=input(f'Type Y to continue calculating with {answer1} ,or type N to exit.:')
  
    if conti=='y':
      a=answer1
    else:
      should_continue=False
      calculator()

calculator()


