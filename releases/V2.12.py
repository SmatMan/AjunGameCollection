from random import randint 
import time
import sys
def pla():
  print "Play Again?"
  plaa = raw_input("Type Yes or No: ")
  if plaa == "Yes" or plaa == "yes":
    mg()
  else:
    start()
def mgc(mgameg, ab, a, b, mghn):
  if mgameg == ab:
    print "You Got It!!"
    mggg(mghn)
  else:
    if mgameg == 112277:
      start()
    else:
      print "Nope"
      mgg(a, b, ab)
    
def mgg(aa, bb, ab, mghn):
  a = int(aa)
  b = int(bb)
  print a, "+", b
  mgamegg = raw_input("Answer")
  mgameg = int(mgamegg)
  mgc(mgameg, ab, a, b, mghn)
def mggg(mghn):
    a = randint(0, mghn)
    b = randint(0, mghn)
    ab = a + b
    mgg(a, b, ab, mghn)
def mg():
  print "\n" * 100
  print "Addition Math Game"
  print "Type 112277 to quit at anytime"
  print "If you get an error like Traceback (most recent call last) then restart the game, it means wrong answer."
  print "\n" * 31
  mgll = raw_input("What is the highest number you can add? (Type 9999 for random): ")
  mgl = int(mgll)
  if mgl == 9999:
    mghn = randint(0, 9999)
    mggg(mghn)
  else:
    mghn = mgl
    mggg(mghn)
def easygg(rn): 
    ganswer = raw_input("Guess:") 
    easyg(ganswer, rn) 
def easyg(num, rn): 
    if num == rn:
        print "You got it!"
        pa = raw_input("Would you like to play again? Type here: ")
        if pa == "yes" or pa == "Yes":
            game()
        else:
            print "Well, goodbye then!"
            print "\n" * 100
            sys.exit()
    else:
        print "Nope!"
        easygg(rn)
def easymode(mvar):
    print "\n" * 100
    randnum = randint(0, mvar)
    mvars = str(mvar)
    randnums = str(randnum)
    print "I am thinking of a number between 0 and " + mvars + "!"
    easygg(randnums)
    


def gamelc(level):
        print "\n" * 100
        if level == "1":
            print("Easy Mode")
            mvar = 10
            easymode(mvar)
        else:
            if level == "2":
                print("Medium Level")
                mvar = 50
                easymode(mvar)
                
            else:
              if level == "q" or level == "Q":
                start()
              else:
                if level == "3":
                    print "Hard Level"
                    mvar = 100
                    easymode(mvar)
                else:
                    if level == "4":
                      print "Almost Impossible Level"
                      mvar = 500
                      easymode(mvar)
                    else:
                      if level == "5":
                        print "Impossible Level"
                        mvar = 1000
                        easymode(mvar)
                      else:
                        if level == "6":
                          mvaro = raw_input("What's the Max Number?")
                          print "Custom Level (0 to " + mvaro + ")"
                          mvar = int(mvaro)
                          easymode(mvar)
                        print "Please choose either 1, 2, 3, 4, 5 or 6, not " + level + "!"
                        game()
                
def game():
    print "\n" * 100
    print("Difficulty Levels")
    print("Easy = 1")
    print("Medium = 2")
    print("Hard = 3")
    print("Almost Impossible = 4")
    print("Impossible = 5")
    print("Custom = 6")
    print("Quit = Q")
    dl = raw_input("Level Number: ")
    dls = str(dl)
    gamelc(dls)
    
def uc():
  print "\n" * 100
  print "--------------"
  print "Coming Soon:"
  print "--------------"
  print "V2.63:"
  print "Suggest whats next!"
  print "--------------"
  print "\n" * 28
  time.sleep(3)
  start()
def cl():   
  print "\n" * 100
  print "---------------------"
  print "Changelog:"
  print "---------------------"
  print "V1.0 Alpha:"
  print "Released As Alpha"
  print "------------------------"
  print "V1.5 Alpha:"
  print "Math Addition Game added"
  print "------------------------"
  print "V2.12 Beta:"
  print "Released As Alpha!"
  print "Made it so math game keeps repeating until user quits"
  print "Released to GitHub"
  print "------------------------"  
  print "\n" * 22
  time.sleep(3)
  start()
def start():   
  print "\n" * 100
  print "Ajun Game Collection"
  print "Version 1.5"
  print "1: Guessing Game"
  print "2: Math Addition Game"
  print "3: Changelog"
  print "4: Upcoming"
  print "Q: Quit"
  print "\n" * 28
  c = raw_input("Choose an option:")
  
  if c == "1":
    game()
  else:
    if c == "3":
      cl()
    else:
      if c == "4":
        uc()
      else:
        if c == "q" or c == "Q":
          sys.exit()
        else:
          if c == "2":
            mg()
start()
