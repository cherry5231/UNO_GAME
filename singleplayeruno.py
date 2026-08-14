import random
import time
cards = [
  "R1","R2","R3","R4","R5","R6","R7","R8","R9","Rskip","Rreverse","u+4","R+1","U",
  "B1","B2","B3","B4","B5","B6","B7","B8","B9","Bskip","Breverse","u+4","B+1","U",
  "G1","G2","G3","G4","G5","G6","G7","G8","G9","Gskip","Greverse","u+4","G+1","U",
  "Y1","Y2","Y3","Y4","Y5","Y6","Y7","Y8","Y9","Yskip","Yreverse","u+4","Y+1","U",
]
starting_card = ["R1","R2","R3","R4","R5","R6","R7","R8","R9",
  "B1","B2","B3","B4","B5","B6","B7","B8","B9",
  "G1","G2","G3","G4","G5","G6","G7","G8","G9",
  "Y1","Y2","Y3","Y4","Y5","Y6","Y7","Y8","Y9"]
player = random.sample(cards,7)
system = random.sample(cards,7)
penalty = 0
last_card = random.choice(starting_card)
turn = "player"
p = []
print("Starting card : ", last_card)
while True:
 # PLAYER LOGIC 

 if len(player) == 0:
             print("Player won")
             break
 if turn == "player":
    print("Your remaining cards :",player)
    a = input("Enter your card:      (or Type X to take a card)") 
  
    
 # PENALTY LOGIC
    if penalty > 0:
            plus_cards_player = []
            for e in player:
                    if e[1:] == "+1" or e[1:] == "+4":
                            plus_cards_player.append(e)
            if len(plus_cards_player)> 0:
                            
                            if a in plus_cards_player:
                              if a[1:] == "+1":
                                   penalty = penalty + 1
                                   last_card = a
                                   print("player stacked a +1 card",a)
                                   player.remove(a)
                                
                                   if len(player) == 0:
                                                                       print("player won")
                                                                       break
                                   else:
                                           turn = "system"
                                   continue

                              elif a[1:] == "+4":
                                      print("ITS A WILD +4 CARD........")
                                      time.sleep(2)
                                      ee = input("Choose a color: R/B/G/Y  ")
                                      if ee == "R":
                                               ay = "R0"

                                      elif ee =="B":
                                          ay = "B0"
                                      elif  ee =="G": 
                                          ay ="G0"
                                      elif  ee == "Y":
                                          ay = "Y0"
                                      else:
                                          print("Enter a valid color")
                                          continue

                                      last_card = ay

                                      
                                      penalty = penalty + 4
                                      print("player stacked +4 cards",penalty)
                                      player.remove(a)
                                      if len(player) == 0:
                                                                                                             print("player won")
                                                                                                             break
                                      else:
                                                                                 turn = "system"
                                                                                 continue
                                                                                 

                            elif a == "X" or a == "x":
                                                                     print("player doesnt have a +1 card")
                                                                     extraaa = random.sample(cards,penalty)
                                                                     player.extend(extraaa)
                                                                     print("Player took",penalty," extra cards")
                                                                     penalty = 0
                                                                     turn = "system"
                                                                     continue                       
                                      
                            else:
                                    print("pls enter a valid card")
                                    continue
                              
                            
          
            else:
                            print("player doesnt have a +1 card")
                            extraaa = random.sample(cards,penalty)
                            player.extend(extraaa)
                            print("Player took",penalty," extra cards")
                            penalty = 0
                            turn = "system"
                            continue


                            
    time.sleep(1)
    if a == "x" or a == "X":
                print("Player hit pull, taking one extra card")
                time.sleep(2)
                extra_cardd = random.choice(cards)
                player.append(extra_cardd)
                print("Player took one extra card.....",extra_cardd)
                turn = "system"
                continue
    if a not in player:
     print("pls enter valid card")
     continue
    # UNIVERSAL CARD LOGIC 
   
    if   len(last_card) == 0 and ( a[1:] == "reverse" or a[1:] == "skip" or a[1:]== "+1" or a[0] == "u" or a[0] == "U"):
                  print("cannot throw a wild card in start")
                  continue
    # last CARD LOGIC 
    if len(player) == 1 and (a[1:] == "skip" or a[1:] == "reverse" or a[1:] == "+4" or a[1:] == "+1" or a[0] == "U") :
                         print("last card cannot be a wild card.......")
                         time.sleep(2)
                         
                         
                         extraa = random.choice(cards)
                         player.append(extraa)
                         print("So player took an extra card",extraa)
                         
                         turn = "system"
                         continue
    elif (len(player) == 0) :
                                       time.sleep(2)
                                       print("Player has won")
                                       break
    
   

    if a[0] == "U":
           print("ITS  A WILD UNIVERSAL CARD")
           time.sleep(2)
           print("Choose a color")
           uc = input("R or Y or B or G:")
           if uc == "R":
                  last_card = "R0"
                  time.sleep(1)
                  print("PLAYER CHOSE RED.....")
                   
                  player.remove("U")
                  turn = "system"
           elif uc == "B":
                  last_card = "B0"
                  time.sleep(1)
                  print("PLAYER CHOSE BLUE.....")
                  player.remove("U")
                  turn = "system"
           elif uc == "G":
                  last_card = "G0"
                  time.sleep(1)
                  print("PLAYER CHOSE GREEN.....")
                  player.remove("U")
                  turn = "system"
           elif uc == "Y":
                  last_card = "Y0"
                  time.sleep(1)
                  print("PLAYER CHOSE YELLOW....")
                  player.remove("U")
                  turn = "system"
           else:
                  print("Invalid Color , Use a Valid Color")
                  continue
    elif a[0] == "u":
       print("ITS A WILD +4 CARD")
       time.sleep(2)

       uc2 = input("Choose a color R/Y/B/G: ")

       if uc2 in ["R", "B", "G", "Y"]:
              ay = uc2 + "0"
              last_card = ay
              penalty += 4
              player.remove(a)

              print("PLAYER CHOSE:", uc2)
              print("Current penalty:", penalty)

              turn = "system"
       else:
              print("Invalid Color, Use a Valid Color")
              continue
    elif len(last_card) != 0 and (a[1:] == last_card[1:] or a[0] == last_card [0] or a == "U" or a == "u+4"):
        print("you threw:", a)
        player.remove(a)
        last_card = a
        print("current deck :",last_card)
# PLUS CARDS LOGIC
        if a[1:] == "+1":
                penalty = penalty + 1                            
             
                turn = "system"
                time.sleep(2)

        elif a[1:] == "reverse":
              print("player threw reverse")
              turn = "player"
              time.sleep(2)
        elif a[1:] == "skip":
                      print("player threw skip")
                      turn = "player"
                      time.sleep(2)
        else: 
               turn = "system"
      
       

    elif len(last_card) != 0 and (a[0] != last_card[0] and a[1:] != last_card[1:] or a == "U" or a == "u+4"):
        print("Invalid card, try to throw same color card")
        time.sleep(2)
        extra2 = random.choice(cards)
        player.append(extra2)
        print("You took extra")
        turn = "system"
    else:

        print("you threw :",a)
        player.remove(a)
        last_card = a
        time.sleep(2)
        print("current deck :",last_card)
        turn = "system"
    if len(player) == 0:
            print("Player won")
            break
 
# SYSTEM LOGIC 
 elif turn == "system":


     
        print("System's turn.....")
        time.sleep(2)
        print("system's cards:",len(system))
        time.sleep(1)
        print("current deck: ",last_card)
# PENALTY LOGIC
        if penalty > 0:
                      plus_cards = []

                      for s in system:
                            if s[1:] == "+1" or s == "u+4":
                             plus_cards.append(s)

                      if len(plus_cards) > 0:

                            ae = random.choice(plus_cards)

                            if ae[1:] == "+1":
                             penalty += 1
                             last_card = ae
                             system.remove(ae)

                             print("System stacked +1:", ae)
                             time.sleep(2)
                             print("Current penalty:", penalty)
 
                            elif ae == "u+4":
                                   print("System stacked +4")
                                   time.sleep(2)
                                   uc2 = random.choice(["R", "B", "G", "Y"])
                                   print("System chose:", uc2)

                                   if uc2 == "R":
                                          last_card = "R0"
                                   elif uc2 == "B":
                                          last_card = "B0"
                                   elif uc2 == "G":
                                          last_card = "G0"
                                   elif uc2 == "Y":
                                          last_card = "Y0"

                                   penalty += 4
                                   system.remove(ae)

                                   print("Current penalty:", penalty)

                            if len(system) == 0:
                             print("System won")
                             break
                            else:
                             turn = "player"
                             continue

                      else:
                                   print("System cannot stack.")
                                   time.sleep(2)

                                   extraaa = random.sample(cards, penalty)
                                   system.extend(extraaa)
                                   time.sleep(2)
                                   print("System took", penalty, "extra cards")

                                   penalty = 0
                                   turn = "player"
                                   continue
 
        possible_cards = []
        for card in system:

            if card[0] == last_card[0] or card[1:] == last_card[1:]   or card == "U" or card == "u+4" :
                possible_cards.append(card)

        


        if len(possible_cards) == 0:

            extra = random.choice(cards)

            system.append(extra)

            print("System has no valid card")
            time.sleep(2)
            print("System took:", extra)
            time.sleep(1)
            turn = "player"

        else:

            system_card = random.choice(possible_cards)
# last CARD LOGIC 
            if len(system) == 1 and (system_card[1:] == "skip" or system_card[1:] == "reverse" or system_card[1:] == "+4" or system_card[1:] == "+1" or system_card[0] == "U") :
                                                     print("last card cannot be a wild card.......")
                                                     time.sleep(2)
                                                     
                                                     
                                                     extraa = random.choice(cards)
                                                     system.append(extraa)
                                                     print("So system took an extra card",extraa)
                                                     
                                                     turn = "player"
                                                     continue
          
            system.remove(system_card)
 


                
            if (len(system) == 0) :
                                                                               time.sleep(2)
                                                                               print("System has won")
                                                                               break

            print("System threw:", system_card)
            time.sleep(2)

            last_card = system_card
            print("current deck :",last_card)
  
                    
# UNIVERSALCARD  LOGIC 
            if system_card == "U":
                              print("ITS A WILD UNIVERSAL CARD")
                              time.sleep(2)
                              print("Choose a color")
                              uc = random.choice(["R", "B", "G", "Y"])
                              print("System chose : ",uc)

                              if uc == "R":
                                     last_card = "R0"
                                     time.sleep(1)
                                     print("SYSTEM CHOSE RED.....")
                                     
                                  
                                     turn = "player"
                              elif uc == "B":
                                     last_card = "B0"
                                     time.sleep(1)
                                     print("SYSTEM CHOSE BLUE.....")
                                     turn = "player"
                              elif uc == "G":
                                     last_card = "G0"
                                     time.sleep(1)
                                     print("SYSTEM CHOSE GREEN.....")
                                    
                                     turn = "player"
                              elif uc == "Y":
                                     last_card = "Y0"
                                     time.sleep(1)
                                     print("SYSTEM CHOSE YELLOW.....")
                                   
                                     turn = "player"
                              else:
                                     print("Invalid Color , Use a Valid Color")
                                     continue
            elif system_card == "u+4":
                                                 print("ITS A WILD +4 CARD")
                                                 time.sleep(2)

                                                 uc2 = random.choice(["R", "B", "G", "Y"])
                                                 print("System chose:", uc2)

                                                 if uc2 == "R":
                                                        last_card = "R0"
                                                 elif uc2 == "B":
                                                        last_card = "B0"
                                                 elif uc2 == "G":
                                                        last_card = "G0"
                                                 elif uc2 == "Y":
                                                        last_card = "Y0"

                                                 penalty += 4

                                                 print("System played +4")
                                                 print("Current penalty:", penalty)

                                                 turn = "player"
# PLUS CARDS LOGIC 
            if system_card[1:] == "+1":
             
                     penalty += 1
                     print("System threw +1.")
                     print("Current penalty:", penalty)
                     time.sleep(2)
                     turn = "player"
           
            
            elif system_card[1:] == "reverse":
                  print("system threw reverse")
                  turn = "system"
                  time.sleep(2)
            elif system_card[1:] == "skip":
                               print("system threw skip")
                               turn = "system"
                               time.sleep(2)
            else:
                   turn = "player"
                   time.sleep(1)
            if len(system) == 0:
                    print("System won")
                    break        