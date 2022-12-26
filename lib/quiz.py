def repoints():
    global pointa
    global pointb
    global pointc
    global pointd
    global pointe
    
    pointa = 0
    pointb = 0
    pointc = 0
    pointd = 0
    pointe = 0

    

def quiz():
    ##################
    from lib import _est_main

    import time
    import random
    ##################
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
                quiz()
                
            elif n == 2:
                print("\n\n\n")
                _est_main.repeat()
                
            elif n == 3:
                exit()
    
            else:
                print("\nerror!!!! incorrect option")
                mainscreen()
    
    
    
    

    ####################################################### M I S C #########################################################################

    def tc(n):
        time.sleep(n)
        
    """ 1/1/2/2/1/2/1/9///2/2/4/3///2/1/3/1////525/6/4/10 """
       
    ########################################################### E A S Y ##########################################################################


    def quiz1():
        global pointa
        print("which number is greater 99^100 or 100^99 ?")
        print("1) 99^100")
        print("2) 100^99")
        a = int(input("\nselect 1 or 2 : "))

        if a == 1:
            print( "Correct(+1)\n\n")
            pointa += 1
            
        else:
            print("Incorrect \n>>>99^100 is greater\n\n")

    def quiz2():
        global pointa
        print("In a computer, most processing takes place in ____")
        print("1) CPU")
        print("2) Monitor")
        a = int(input("\nselect 1 or 2 : "))
        if a == 1:
            print( "Correct(+1)\n\n")
            pointa += 1
        else:
            print("Incorrect \n>>>99^100 is greater\n\n")

    def quiz3():
        global pointa
        print("What converts an entire program into machine language?")
        print("1) Interpreter")
        print("2) Compiler")
        a = int(input("\nselect 1 or 2 : "))
        if a == 2:
            print( "Correct(+1)\n\n")
            pointa += 1
        else:
            print("Incorrect \n>>>compiler converts an entire program into machine language\n\n")

    def quiz4():
        global pointa
        print("Where does most data go first with in a computer memory hierarchy?")
        print("1) ROM")
        print("2) RAM")
        a = int(input("\nselect 1 or 2 : "))
        if a == 2:
            print( "Correct(+1)\n\n")
            pointa += 1
        else:
            print("Incorrect \n>>>RAM is the correct answer\n\n")
    def quiz5():
        global pointa
        print("Which of the following is an invalid identifier?")
        print("1) 12cs_")
        print("2) _12cs")
        a = int(input("\nselect 1 or 2 : "))
        if a == 1:
            print( "Correct(+1)\n\n")
            pointa += 1
        else:
            print("Incorrect \n>>>12cs_ is an invalid identifier\n\n")

    def quiz6():
        global pointa
        print("The principal value of tan-1(tan 3π/5) is: ")
        print("1) 3π/5")
        print("2) -2π/5")
        a = int(input("\nselect 1 or 2 : "))
        if a == 2:
            print( "Correct(+1)\n\n")
            pointa += 1
        else:
            print("Incorrect \n>>>option 2 is correct\n\n")

    def quiz7():
        global pointa
        print("If y = ax^2+b, then dy/dx at x = 2 is equal to")
        print("1) 4a")
        print("2) 2a")
        a = int(input("\nselect 1 or 2 : "))
        if a == 1:
            print( "Correct(+1)\n\n")
            pointa += 1
        else:
            print("Incorrect \n>>>f(x)=ax^2+b\n>>>f'(x)=2ax\nf'(2)= 2a(2)= 4a\n\n")

    def quiz8():
        global pointa
        print("what is 9÷3(2+1)")
        
        a = int(input("\ntype your awnser : "))
        if a == 9:
            print("Correct(+1) too easy right??\n\n")
            pointa += 1
        else:
            print( "Incorrect\n\n")





    #################################################### N O R M A L ##################################################################################

    def quiz9():
        global pointb
        print("Circular loop of radius 0.0157 m carries a current 2 A. The magnetic field at the centre of the loop is")
        print("1) 1.57 × 10^(-3)Wb/m²")
        print("2) 8.0 × 10^(-5) Wb/m²")
        print("3) 2.0 × 10^(-3) Wb/m²")
        print("4) 3.l4 × 10^(-1)Wb/m²")

        a = int(input("\ntype your awnser : "))
        if a == 2:
            print( "Correct(+2)\n\n")
            pointb += 2
        else:
            print("Incorrect, option 2 is correct \n\n")


    def quiz10():
        global pointb
        print("If there are 3 apples on the table and you take 2 of them, how many will you have?")
        print("1) one")
        print("2) two")
        print("3) three")
        print("4) none of these")
        
        a = int(input("\ntype your awnser : "))
        if a == 2:
            print( "Correct(+2)\n\n")
            pointb += 2
        else:
            print("Incorrect\n>>> You will take the 2 apples and they are with you, so you have 2 apples.\n\n")
            
            
    def quiz11():
        global pointb
        print("If x + 1x = 2 then the principal value of sin-1 x is x")
        print("1) π/4")
        print("2) π/2")
        print("3) π")
        print("4) 3π/2")
        
        a = int(input("\ntype your awnser : "))
        if a == 4:
            print( "Correct(+2)\n\n")
            pointb += 2
        else:
            print("Incorrect\n>>> 3π/2\n\n")
            
    def quiz12():
        global pointb
        print("A doctor gives you 3 pills and tells you take 1 every half an hour, how long would it be before the pills have been taken?")
        print("1) 0 min")
        print("2) 30 min")
        print("3) 60 min")
        print("4) 90 min")
        
        a = int(input("\ntype your awnser : "))
        if a == 3:
            print( "Correct(+2)\n\n")
            pointb += 2
        else:
            print("Incorrect\n>>> You take 1 immediately, the 2nd pill 30 minutes later and the last 30 minutes later\n\n")
        
    ############################################## H A R D ########################################################################################

    def quiz13():
        global pointc
        print("The dump method requires _________ minimum no of parameters")
        print("1) one")
        print("2) two")
        print("3) four")
        print("4) six")
        print("5) zero")
        print("6) none of these")
        
        print("0) skip")
        
        a = int(input("\ntype your awnser : "))
        if a == 2:
            print( "Correct(+2)\n\n")
            pointc += 2
        elif a == 0:
            print("Skipped (0)\n\n")
        else:
            print("Incorrect (-1) \n>>> (2)\n\n")
            pointc -= 1
            
    def quiz14():
        global pointc
        print("The pickle.load() function requires minimum _____ number of parameters")
        
        a = int(input("\ntype your awnser (Integer type answer & '0' to skip) : "))
        if a == 1:
            print( "Correct(+2)\n\n")
            pointc += 2
        elif a == 0:
            print("Skipped (0)\n\n")
        else:
            print("Incorrect (-1) \n>>> (2)\n\n")
            pointc -= 1
            
    def quiz15():
        global pointc
        print("Give the output of the following code:")
        print("import math")
        print("math.ceil(1.03)+math.floor(1.03)")
        
        a = int(input("\ntype your awnser (Integer type answer & '0' to skip) : "))
        if a == 3:
            print( "Correct(+2)\n\n")
            pointc += 2
        elif a == 0:
            print("Skipped (0)\n\n")
        else:
            print("Incorrect (-1) \n>>> (3)\n\n")
            pointc -= 1
        
        
    def quiz16():
        global pointc
        print("∫cos(√x)dx = ")
        print("1) 2[√x.sin(√x) + cos(√x)] + C")
        print("2) 2[√x.cos(√x) + sin(√x)] + C")
        print("3) 2[√x.sin(√x) - cos(√x)] + C")
        print("4) 2[√x.cos(√x) + sin(√x)] + C")
        print("5) sin(√x) + C")
        print("6) none of these")
        
        print("0) skip")
        
        a = int(input("\ntype your awnser (Integer type answer & '0' to skip) : "))
        if a == 1:
            print( "Correct(+2)\n\n")
            pointc += 2
        elif a == 0:
            print("Skipped (0)\n\n")
        else:
            print("Incorrect (-1) \n>>> (2)\n\n")
            pointc -= 1
            
    ######################################################### E X T R E M E #######################################################################

    def quiz17():
        global pointd
        print("A heavy nucleus Q of half-life 20 min undergoes alpha decay with probability of 60% and beta decay with probability of 40% . Initially , the number of Q nuclei is 1000. The number of alpha decay in first hour is ")
        
        a = int(input("\ntype your awnser (Integer type answer & '0' to skip) : "))
        if a == 525:
            print( "Correct(+4)\n\n")
            pointd += 4
        elif a == 0:
            print("Skipped (0)\n\n")
            
        else:
            print("Incorrect (-4) \n>>> (525)\n\n")
            pointd -= 4
            
    def quiz18():
        global pointd
        print("The total number of possible isomers for [Pt(NH3)4Cl2]Br2 is")
        
        a = int(input("\ntype your awnser (Integer type answer & '0' to skip) : "))
        if a == 6:
            print( "Correct(+4)\n\n")
            pointd += 4
        elif a == 0:
            print("Skipped (0)\n\n")      
        else:
            print("Incorrect (-4) \n>>> (6)\n\n")
            pointd -= 4
            
    def quiz19():
        global pointd
        print("for x∈ R then the number of real roots of the equation 3X² - 4| X² - 1 | + x - 1 = 0 is ____")
       
        print("0) skip")
        
        a = int(input("\ntype your awnser (Integer type answer & '0' to skip) : "))
        if a == 4:
            print( "Correct(+4)\n\n")
            pointd += 4
        elif a == 0:
            print("Skipped (0)\n\n")      
        else:
            print("Incorrect (-4) \n>>> (4)\n\n")
            pointd -= 4
            
    def quiz20():
        global pointd
        print("what is the output of the function:\n")
        print("def compute(num):\n     if (num==1):\n        return 1\n     else:\n          return (num + compute(num-1))\nlast = 4\nssum= compute(last)\nprint(ssum)")
        
        a = int(input("\ntype your awnser (Integer type answer & '0' to skip) : "))
        if a == 10:
            print( "Correct(+4)\n\n")
            pointd += 4
        elif a == 0:
            print("Skipped (0)\n\n")      
        else:
            print("Incorrect (-4) \n>>> (1o)\n\n")
            pointd -= 4
            
    ################################################################ B O N U S :) #################################################################

    def bonus():
        global pointe
        print( "wohooo Bonus quiz , Be ready !!!!\n\n")
        tc(5)
        print("which social media platform u like most:")
        print("1) Youtube")
        print("2) Instagram")
        print("3) Twitter")
        print("4) Tik Tok")
        print("5) Telegram")  
        print("6) Facebook") 
        
        pointr = random.randint(0, 10)
        a = int(input("select btw 1 to 6: "))
        if a == 1:
            print( "here u r rewarded with (",pointr*4,") points\n\n")
            pointe += pointr*3
        elif a == 2:
            print("here u r rewarded with (0) points\n\n")
            pointe += 0
        elif a == 3:
            print( "here u r rewarded with (",pointr,") points\n\n")
            pointe += pointr
        elif a == 4:
            print( "here u r rewarded with (",pointr*-4,") points poor soul!!\n\n")
            pointe = pointr*-4
        elif a == 5:
            print( "here u r rewarded with (-1) points\n\n")
            pointe -= 1
        elif a == 6:
            pointe += 2
            print( "here u r rewarded with (+2) points\n\n")
        else:
            pointe += pointr*0.1
            print( "well this was never been an option but luckily i am in a good mood and you're awarded with (",pointr*0.1,") points") 
            tc(1)
            
    def bonus_check():
        a = random.randint(1, 6)
        check = 0
        if a == 6:
           check += 1
        else:
            check -= 1
            
        return check   
            
    ###############################################################################################################################################
    
    print(">>> Quiz level : Easy\n>>> You Can't skip any question \n>>> For each correct awnser you will get (+1) point and will lose (0) point if incorrect\nGOOD LUCK!!!\n\n")
    
    tc(3)

    quiz1()
    tc(1)
    quiz2()
    tc(1)
    quiz3()
    tc(1)
    quiz4()
    tc(1)
    quiz5()
    tc(1)
    quiz6()
    tc(1)
    quiz7()
    tc(1)
    quiz8()
    tc(1)

    print(">>> Quiz level :Normal\n>>> You Can't skip the question \n>>> For each correct awnser you will get (+2) point and will lose (0) point if incorrect, be careful there are more option than before \nGOOD LUCK!!!\n\n")
    tc(3)

    quiz9()
    tc(1)
    quiz10()
    tc(1)
    quiz11()
    tc(1)
    quiz12()
    tc(1)

    print(">>> Quiz level :Hard\n>>> You can skip question if you don't know or you are not sure by putting '0' \n>>> For each correct awnser you will get (+2) point and will lose (-1) point if incorrect, be careful there are even more or no options \nGOOD LUCK!!!\n\n")
    tc(3)

    quiz13()
    tc(1)
    quiz14()
    tc(1)
    quiz15()
    tc(1)
    quiz16()
    tc(1)

    print(">>> Quiz level :Extreme\n>>> You can skip question if you don't know or you are not sure by putting '0' \n>>> For each correct awnser you will get (+4) point and will lose (-4) point if incorrect, be careful there are no options, Take your time before answering \nGOOD LUCK!!!\n\n")
    tc(5)

    quiz17()
    tc(1)
    quiz18()
    tc(1)
    quiz19()
    tc(1)
    quiz20()
    tc(1)

    if bonus_check() == 1:
        bonus()


    ###################################################### R E V I E W #############################################

    def review():
        if bonus_check() == 1:
            summing = pointa + pointb + pointc + pointd + pointe
            if summing < 0:
                print( "how u get there LoL")
            elif summing == 80:
                print( "AMAZING, you are the most brilliant and luckiest person!!!!!!")
            
        elif bonus_check() == -1:
            summing = pointa + pointb + pointc + pointd
            if summing == 40:
                print( "amazing a perfect score")
            elif summing >= 24:
                if pointd >= 0 and pointd <= 8:
                    print( "not perfect but this is still amazing")
                else:
                    print( "you can do much better , belive me")
            elif summing <= 15 and summing != 0:
                print( "better Luck next time")
            elif summing < 24 and summing > 15:
                print( "well played")
            else:
                print( "just how????")
        else:
            print( "nice")


#######################################################################
    print("################################################")    
    print("       Y O U R   R E S U L T")
    print("\n\ntotal easy quiz point : ",pointa)
    print("total normal quiz point : ",pointb)
    print("total hard quiz point : ",pointc)
    print("total expert quiz point : ",pointd)
    if bonus_check() == 1:
        print("total bonus quiz point: ",pointe)
    print("################################################\n\n")    
    

    if bonus_check() == 1:
        summing = pointa + pointb + pointc + pointd + pointe
    else:
        summing = pointa + pointb + pointc + pointd
        
    print("your total score : ",summing)
    
    review()
    tc(5)
    mainscreen()

pointa = 0
pointb = 0
pointc = 0
pointd = 0
pointe = 0
