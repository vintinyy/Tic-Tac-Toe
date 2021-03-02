import random

board = ("""
      |     |     
1  -  | 4 - |  7  
 _____|_____|_____
      |     |     
2  -  | 5 - |  8  
 _____|_____|_____
      |     |     
3  -  | 6 - |  9  
""")
print(board)
print(" pick which spot you want to go. (you are the O character) ")

players_choices = []
bots_choices = []
for i in range(4):
  answer = int(input(" which spot? (answer with a number --)"))

  while answer < 1 or answer > 9: 
    print(" a number on that board ")
    answer = int(input(" which spot?"))
 
  players_choices.append(answer)
  board = board.replace( str(answer) , " O")

  print(board)

  a = random.randint(1,9)


  while answer == a :
    a = random.randint(1,9)
  print( "I choose" , "....." + str(a) + "!")
  bots_choices.append(a)
  board = board.replace( str(a) , "X")

  print(board)

for i in players_choices:

  for j in players_choices:

    for k in players_choices:
      if i == 1 and j == 4 and k ==7:
        print(" Yay! You won!")
      elif i == 1 and j ==5 and k ==9:
        print("Yay! You win!")
      elif i == 2 and j ==5 and k ==8:
        print("Yay! You win!")
      elif i == 2 and j == 1 and k ==3:
        print("Yay! You win!")
      elif i == 3 and j ==5 and k ==7:
        print("Yay! You win!")
      elif i == 3 and j == 6 and k ==9:
        print("Yay! You win!")
      elif i == 7 and j == 8 and k ==9:
        print("Yay! You win!")
      elif i == 4 and j == 5 and k == 6:
        print("Yay! You win!")
for i in bots_choices:

  for j in bots_choices:

    for k in bots_choices:
      if i == 1 and j == 4 and k ==7:
        print(" I win!")
      elif i ==   1 and j ==5 and k ==9:
        print("I win!")
      elif i == 2 and j ==5 and k ==8:
        print("I win!")
      elif i == 2 and j == 1 and k ==3:
        print("I win!")
      elif i == 3 and j ==5 and k ==7:
        print("I win!")
      elif i == 3 and j == 6 and k ==9:
        print("I win!")
      elif i == 7 and j == 8 and k ==9:
        print("I win!")
      elif i == 4 and j == 5 and k == 6:
        print("I win!")
    else:
        print("draw!")
        break


