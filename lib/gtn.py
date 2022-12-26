def repoints():
    global total_guess
    total_guess = 0

def gtn():
    
    import random
    import time
    
    global total_guess
    
    def mainscreen():
        while True:
            print("\nSelect option:")
            print("1) Start again")
            print("2) Back to main menu")
            print("3) Quit\n")
            
            n = int(input("your response(1,2,3): "))
            print("\n")
            
            if n == 1:
                repoints()
                gtn()
                
            elif n == 2:
                print("\n\n\n")
                from lib import _est_main
                _est_main.repeat()
                
            elif n == 3:
                exit()
    
            else:
                print("\nerror!!!! incorrect option")
                mainscreen()     
                
    print("NOTE : higher the difference in number higher the difficulty")

    min_range = int(input("Select The minimum range of your guess: "))
    max_range = int(input("Select The maximum range of your guess: "))
    
    guess_number = random.randrange(min_range,max_range)

    your_guess = int(input("\nGuess the number : "))

    while your_guess != guess_number:
        
        
        if your_guess < guess_number:
            print("Incorrect guess, HINT: you need to guess higher")
            your_guess = int(input("\nGuess the number : "))
            total_guess +=1

        else:
            print("Incorrect guess, HINT: you need to guess lower")
            your_guess = int(input("\nGuess the number :"))
            total_guess +=1

    print("\nWell done !!!!! you guessed the correct number (",guess_number,")")
    print("Total guess :",total_guess + 1)
    print("\n")
    
    
    time.sleep(5)
    mainscreen()
    
total_guess = 0