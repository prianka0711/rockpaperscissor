import random

while True:
               choices=['rock','paper','scissor']
               computer=random.choice(choices)
               player=None
               while player not in choices:
                  player=input("rock,paper,scissor:")

                  if player==computer:
                      print("computer:",computer)
                      print("player:",player)
                      print("Tie!")

                  elif player=='rock':
                        if computer=='paper':
                            print("computer:",computer)
                            print("player:",player)
                            print("you lose!")
                        if computer=='scissor':
                            print("computer:",computer)
                            print("player:",player)
                            print("you win!")
                  elif player=='paper': 
                        if computer=='scissor':
                            print("computer:",computer)
                            print("player:",player)
                            print("you lose!")
                        if computer=='rock':
                            print("computer:",computer)
                            print("player:",player)
                            print("you win!")
                  elif player=='scissor':
                        if computer=='rock':
                              print("computer:",computer)
                              print("player:",player)
                              print("you lose!")
                        if computer=='paper':
                              print("computer:",computer)
                              print("player:",player)
                              print("you win!")
                              
                  playagain=input("playagain?yes/no:")
                  if   playagain =="yes":
                       break
                  else:
                       print("goodbye!better luck for next time!")
                      

