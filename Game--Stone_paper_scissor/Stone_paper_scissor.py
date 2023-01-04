import random
import os 
play='y'

def Gamewinner(comp, you):
        if (comp == you):
            return None

        elif (comp == 'st' and you == 'p'):
            return True

        elif (comp == 'st' and you == 'sc'):
            return False

        elif (comp == 'p' and you == 'st'):
            return False

        elif (comp == 'p' and you == 'sc'):
            return True

        elif (comp == 'sc' and you == 'p'):
            return False

        elif (comp == 'sc' and you == 'st'):
            return True


def computer():
        comp=0
        a = random.randint(1, 3)
        if (a == 1):
            comp = 'st'
        elif (a == 2):
            comp = 'p'
        elif (a == 3):
            comp = 'sc'
        return comp

  
       
while (play == 'y'):
        os.system('cls' if os.name == 'nt' else 'clear')

        print ('-----------------------STONE--PAPER--SCISSOR----------------------\n\n')
    
        ch= int(input("Play with \n1.computer--press 1\n2.friend--press 2\n\n"))
        os.system('cls' if os.name == 'nt' else 'clear')
        while(ch!=1 and ch!=2):
           print("Enter valid choice")
           ch= int(input("Play with \n1.computer--press 1\n2.friend--press 2\n\n"))
           os.system('cls' if os.name == 'nt' else 'clear')

        if(ch==1 ):
         
         print("Computer's turn:\n  Stone(st) paper(p) scissor(sc) ??")
         comp=computer()
         you = input("Yours turn:\n  Stone(st) paper(p) scissor(sc) ??\n")
         os.system('cls' if os.name == 'nt' else 'clear')
         
        
         while ((you != "st") and (you != "p") and (you != "sc") ):
             print('enter correct Choice!\n')
             you = input("Your's turn:\n  Stone(st) paper(p) scissor(sc) ??\n")
        

         print("\n-------------------------------------------------------------------")
         print(f"You chose -->[{you}]", end='\n')
         print(f"computer chose-->[{comp}]\n")

         winner = Gamewinner(comp, you)

         if (winner == None):
             print("Winner---> Tie")
         elif (winner == True):
             print("Winner---> You win!")
         else:
             print("Winner---> Comp win!")

         print("-------------------------------------------------------------------")
         play = input("\nWant to play more??\nYes-- y\nNo-- n \n")
         if(play=='n'):
             print("\nGood bye!")



        else:
         player1=input("Enter player 1 name:\n")
         os.system('cls' if os.name == 'nt' else 'clear')
         player2=input("Enter player 2 name:\n")
         os.system('cls' if os.name == 'nt' else 'clear')
         you = input(f"{player1}'s turn:\n  Stone(st) paper(p) scissor(sc) ??\n")
         
            
         while ((you != "st") and (you != "p") and (you != "sc") ):
             print(f'{player1} correct Choice!')
             you = input("Your's turn:\n  Stone(st) paper(p) scissor(sc) ??\n")
         os.system('cls' if os.name == 'nt' else 'clear')

         firend=input(f"{player2}'s turn:\n  Stone(st) paper(p) scissor(sc) ??\n")

         while ((firend != "st") and (firend != "p") and (firend != "sc") ):
             print(f'{player2} Enter correct Choice!')
             firend = input("Your's turn:\n  Stone(st) paper(p) scissor(sc) ??\n")
         os.system('cls' if os.name == 'nt' else 'clear')

         print("\n-------------------------------------------------------------------")
         print(f"{player1} chose -->[{you}]", end='\n')
         print(f"{player2} chose-->[{firend}]\n")

         winner = Gamewinner(firend, you)

         if (winner == None):
             print("Winner---> Tie")
         elif (winner == True):
             print(f"Winner---> {player1} win!")
         else:
             print(f"Winner---> {player2} win!")

         print("-------------------------------------------------------------------")
         play = input("\nWant to play more??\nYes-- y\nNo-- n \n")
         if(play=='n'):
             print("\nGood bye!")


        



  