def repoints():
    global won
    global tie
    global lost
    won = 0
    tie = 0
    lost = 0
    
def rps():
    
    
    import random
    import time
    
    
    def mainscreen():
        while True:
            print("\nSelect option:")
            print("1) Start again")
            print("2) Back to main menu")
            print("3) Quit\n")
            
            n = int(input("your response(1,2,3): "))
            
            if n == 1:
                repoints()
                print("\n")
                rps()
                
            elif n == 2:
                print("\n\n\n")
                from lib import _est_main
                _est_main.repeat()
                
            elif n == 3:
                exit()
    
            else:
                print("\nerror!!!! incorrect option")
                mainscreen()
        
    def win():
        global won
        print("\n\nY O U   W O N\n\n")
        won += 1
        time.sleep(2)
        rps()
        
    def draw():
        global tie
        print("\n\n >>>It's a DRAW!!!\n\n")
        tie += 1
        time.sleep(2)
        rps()
        
        
    def lose():
        global lost
        print("\n\nyou lost\n\n\n")
        lost += 1
        time.sleep(2)
        rps()
        
    def exiting():
        global lost
        global won
        global tie
    
        print("\nhere's The Result:")
        print("Total match Won :",won)
        print("Total match lost :",lost)
        print("Total match Draw: ",tie)
        print("-------> Hope you enjoyed <----------- \n")
        
        time.sleep(5)
        mainscreen()
        
    def cc():
            if ccheck == 1:
                    a = 'rock'
            elif ccheck == 2:
                    a = 'paper'
            else:
                    a = 'scissors'
            return a
            

    def main():
        rock_paper_scissors()

    def rock_paper_scissors():
        
        
        number1 = random.randint(1,3)
        global ccheck
        ccheck = number1
    
        if number1 == 1:
            number2 = int(input("enter a number: "))
            if number2 == number1:
                print("Its rock and rock.")
                draw()
             
            elif number2 == 2:
                print("paper beats rock.")
                win()
            elif number2 == 3:
                print("rock beats scissors.")
                lose()
                
            elif number2 == 4:
                exiting()
            
        elif number1 == 2:
            number2 = int(input("enter a number: "))
            if number2 == number1:
                print("Its paper and paper.")
                draw()
                
            elif number2 == 1:
                print("paper beats rock.")
                lose()
            elif number2 == 3:
                print("scissors cuts paper.")
                win()
            elif number2 == 4:
                exiting()
              
        elif number1 == 3:
            number2 = int(input("enter a number: "))
            if number2 == number1:
                print("Its scissor and scissor.")
                draw()
                
            elif number2 == 1:
                print("rock crushes scissor.")
                win()
            elif number2 == 2:
                print("scissors cuts paper.")
                lose()
            elif number2 == 4:
                exiting()
        
        print("\ncomputer choice: ",cc())
        print("Your choice: ",number2)
        
            
    print("1] Choose Rock")
    print('2] Choose Paper')
    print('3] Choose Scissors\n')
    print("4] exit game")
    print("===================\n")   
    
    main()
    
lost = 0
won = 0
tie = 0