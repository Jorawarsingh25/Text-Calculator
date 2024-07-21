
                  #### Welcome to Text Calculator####

def addition(a,b):
    return a+b
def multiply(a,b):
    return a*b
def subtraction(a,b):
    return a-b
def division(a,b):
    if b==0:
        print('zero not dvide!')
    return a/b

def calculator(expression):
    try:
        result=eval(expression)
        return result
    except ZeroDivisionError:
        return 'zero not divide'
    except Exception as e:
        return f'Error: {str(e)}'

def main_display():
    print('Welcome to Text Based Calculator')
    print('support feature>> +, -, *, /')
    print('exit')
    while True:
        user=input('entert the choice with number: ')
        if user=='exit':
            print('You choice the exit..Good Bye!!')
            break
        result=calculator(user)
        print (f'Result: {result}')
if __name__=="__main__":
    main_display()




