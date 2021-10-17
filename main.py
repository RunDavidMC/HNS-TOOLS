#import time
import string
import random
import os
from namebase_marketplace.marketplace import *
from pycoingecko import CoinGeckoAPI

import generator
import bidder
import status
import info

def dMenu():

  print(25 * "-", "HN$ TOOLS", 25 * "-")
  print("[1] Generate HN$ names ")
  print("[2] Bid on HN$ names ")
  print("[3] Get status on HN$ names ")
  print("[4] Update DNS settings on HN$ names ")
  print("[5] Display info about HN$ TOOLS ")
  print("[6] Display info about Handshake ")
  print("[7] Display info about Namebase ")
  print("[8] Exit HN$ TOOLS ")
  print(61 * "-")

  try:
    mChoice = int(input("Enter your choice [1-8]: "))
  except ValueError:
    print("Please choose a valid option.")
    return


  if mChoice == 1:
    generator.start()

  elif mChoice == 2:
    bidder.start()
    
  elif mChoice == 3:
    status.start()

  elif mChoice == 4:
    return
    
  elif mChoice == 5:
    info.hnsTools()

  elif mChoice == 6:
    info.handshake()
    
  elif mChoice == 7:
    info.namebase()

  elif mChoice == 8:
    print("Thank you for using HN$ TOOLS!")
    exit()

  else:
    print("You must select a valid option!")
    return
    
  
x = 1
while x == 1:
  dMenu()


