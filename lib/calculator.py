def calculation():
    import time
    
    def mainscreen():
        while True:
            print("\nSelect option:")
            print("1) Start again")
            print("2) Back to main menu")
            print("3) Quit\n")
            
            n = int(input("your response(1,2,3): "))
            
            if n == 1:
                calculation()
                
            elif n == 2:
                print("\n\n\n")
                from lib import _est_main
                _est_main.repeat()
                
            elif n == 3:
                exit()
    
            else:
                print("\nerror!!!! incorrect option")
                mainscreen()
    
    num1 = int(input( "Enter first number: "))
    num2 = int(input( "Enter second number: "))

    print("\nSelect operation:")

    print( "1. Plus")
    print( "2. Minus")
    print( "3. Multiply")
    print( "4. Divide\n")


    option = input( "Enter option(1 or 2 or 3 or 4):")


    def plus(x, y):  
       return x + y

    def minus(x, y):
       return x - y

    def multiply(x, y):
       return x * y

    def divide(x, y):
       return x / y

    if option == '1':
       print(num1,"+",num2,"=", plus(num1,num2))

    elif option == '2':
       print(num1,"-",num2,"=", minus(num1,num2))

    elif option == '3':
       print(num1,"*",num2,"=", multiply(num1,num2))

    elif option == '4':
       print(num1,"/",num2,"=", divide(num1,num2))
    else:
       print("\nError!!!")
       print("Error!!!\n\n\n")
       calculation()
       
    time.sleep(3)
    mainscreen()