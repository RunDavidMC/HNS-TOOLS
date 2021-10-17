from namebase_marketplace.marketplace import *
import time

def start():

  accTypeTemp = input("Does your Namebase account have 2FA enabled or GitHub linked [y/n]? ")
  accType = accTypeTemp.lower()

  uEmail = ''
  uPwd = ''

  if accType == "y":
    print("To setup a 2FA or GitHub account, follow this guide: https://github.com/pretended/namebase-marketplace#github-oauth-bypass-and-2fa-auth-bypass")
  elif accType == "n":
    li = open("userCred.txt","r+")
    uEmailTemp = li.readline(1)
    uPwdTemp = li.readline(2)
    if uEmailTemp == "" or uPwdTemp == "":
      lr = open("userCred.txt", "w+")
      lr.write(input("What's the email for your Namebase account? "))
      lr.write("\n")
      lr.write(input("What's the password for your Namebase account? "))
      uEmail = uEmailTemp
      uPwd = uPwdTemp
    else:
      uEmail = uEmailTemp
      uPwd = uPwdTemp

  marketplace = Marketplace(email=uEmail, pwd=uPwd)

  fileTemp = (input("TXT File to Import (TXT File name without .txt extension): "))
  file = fileTemp + ".txt"
  print("Importing from " + file)

  try:
    bidVal = int(input("What would you like to bid? "))
  except ValueError:
    bidVal = 0
  try:
    blindVal = int(input("What would you like to add as a blind? "))
  except ValueError:
    blindVal = 0.4
  if (bidVal + blindVal) < 0.4:
    bidVal = 0
    blindVal = 0.4
  
  print("You are bidding " + str(bidVal) + " HN$.")
  print("You are adding an additional " + str(blindVal) + " HN$ as a blind.")
  confirmation = input("If you have confirmed these values and want to continue, enter Y: ")

  if confirmation.lower() == 'y':

    logFileName = fileTemp + "-bidlog.txt"
    wl = open(logFileName,"a+")

    fList = open(file, "r")
    domains = fList.read().splitlines()

    uInfo = marketplace.get_user_info()
    print(uInfo)
    time.sleep(5)

    for x in domains:
      status = marketplace.get_domain_info(x)

      if status["openBlock"] != None:
        print(status["name"] + " is taken.")
        print(status["openBlock"])
        wl.write(status["name"] + " is taken or in bidding." + "\n")
      else:
        marketplace.open_bid(domain=x, bid_amount=bidVal, blind_amount=blindVal)
        print(status["name"] + " is availible, bidding now.")
        wl.write(status["name"] + " is availible, bidding now." + "\n")
  else:
    print("Aborting...")
    return



