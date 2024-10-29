import brick
import random
from time import sleep

def main():
  choice = brick.pick(["rock","paper","scissors"])
  com = random.randint(0,2)
  if choice == 0:
    if com == 0:
      brick.display_text.putstr("tie")
    if com == 1:
      brick.display_text.putstr("win")
    if com == 2:
      brick.display_text.putstr("you lose")
  if choice == 1:
    if com == 1:
      brick.display_text.putstr("tie")
    if com == 2:
      brick.display_text.putstr("win")
    if com == 0:
      brick.display_text.putstr("you lose")
  if choice == 2:
    if com == 2:
      brick.display_text.putstr("tie")
    if com == 0:
      brick.display_text.putstr("win")
    if com == 1:
      brick.display_text.putstr("you lose")
  brick.key_input()
  sleep(2)
  brick.display_text.clear()
  brick.display_text.putstr("do you want to play again")
  sleep(2)  
  if brick.pick(["yes","no"]) == 0:
    brick.display_text.clear()
    main()
  else:
    brick.display_text.clear()
    brick.display_text.putstr("bye")
