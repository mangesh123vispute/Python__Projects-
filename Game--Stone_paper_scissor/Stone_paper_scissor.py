import random


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


a = random.randint(1, 3)
if (a == 1):
    comp = 'st'
elif (a == 2):
    comp = 'p'
elif (a == 3):
    comp = 'sc'


play=1

while (play != 0):

  print ('-----------------------STONE--PAPER--SCISSOR----------------------\n\n')
  print("Computer's turn:\n  Stone(st) paper(p) scissor(sc) ??")
  print()
  you = input("Your's turn:\n  Stone(st) paper(p) scissor(sc) ??\n")

  while ((you != "st") and (you != "p") and (you != "sc")):
    print('Enter correct Choice!')
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
  play = int(input("\nWant to play more??\n1 for yes\n0 for no \n"))
