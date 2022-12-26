
def repeat():
    
    star = "*"                                    
    print(star*75,"\n")
    print("     W E L C O M E\n")
    print(star*75,"\n")

    print("Game section :")
    print("1] Quiz\n2] Guess the number\n3] Rock-paper-scissor\n\n")

    print("utility section :")
    print("4] Calculator\n\n")
    
    print("0] Quit\n\n")

    select_menu = int(input("select your action (1 to 6) : "))


    if select_menu == 1:
        print("\n\n",star*20,"Q U I Z",star*20,"\n\n")
        
        quiz.repoints()
        quiz.quiz()
        
        
    elif select_menu == 2:
        print("\n\n",star*10,"G U E S S   T H E   N U M B E R",star*10,"\n\n")
        
        gtn.repoints()
        gtn.gtn()
    
    
    elif select_menu == 3:
        print("\n\n",star*5,"R O C K   P A P E R   S C I S S O R",star*5,"\n\n")
        
        rps.repoints()
        rps.rps()
        
    
    elif select_menu == 4:
        print("\n\n",star*15,"C A L C U L A T I O N",star*15,"\n\n")
        
        calc.calculation()
    
    elif select_menu == 0:
        exit()
    
    else:
        print("\ninvalid input choose again!!")
        repeat()
        
from lib import gtn
from lib import quiz
from lib import rps 
from lib import calculator as calc