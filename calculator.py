import pyfiglet
import termcolor

header = pyfiglet.figlet_format("CALCULATOR MADE BY PC")   
header = termcolor.colored(header, color="red")
print(header)

def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def divide(x,y):
    return x/y
def multiply(x,y):
    return x*y 
while True:
    print("select  the operation")
    print("1.add")
    print("2.subtract")
    print("3.divide")
    print("4.multiply")
    print("5.exit")
    choice= input("enter the choice(1/2/3/4/5)")


    if choice=='1':
        num1=int(input("enter the first number"))
        num2=int(input("enter the second number"))
        print(num1,"+",num2,"=",add(num1,num2))
        
    elif choice=='2':
        num1=int(input("enter the first number"))
        num2=int(input("enter the second number"))
        print(num1,"-",num2,"=",add(num1,num2))
        
    elif choice=='3':
        num1=int(input("enter the first number"))
        num2=int(input("enter the second number"))
        print(num1,"/",num2,"=",add(num1,num2))
        
    elif choice=='4':
        num1=int(input("enter the first number"))
        num2=int(input("enter the second number"))
        print(num1,"*",num2,"=",add(num1,num2))
        
    elif choice=='5':    
        break
