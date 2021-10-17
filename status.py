from os import stat
from namebase_marketplace.marketplace import *
import string

def start():

  def dsMenu():

    print(22 * "-", "HN$ TOOLS Status", 22 * "-")
    print("[1] Get details about a specific name ")
    print("[2] Get details on multiple names ")
    print("[3] Get domains on the Marketplace ")
    print("[4] Get ending soon domains ")
    print("[5] Get deatils on my domains ")
    print("[6] Exit HN$ TOOLS status ")
    print(62 * "-")

    try:
      mChoice = int(input("Enter your choice [1-6]: "))
    except ValueError:
      print("Please choose a valid option.")
      return

    def lookup(names, marketplace, fileName):
      w = open(fileName,"a+")
      for x in names:
        dInfo = marketplace.get_domain_info(x)
        try:
          dMarketTemp = marketplace.get_domain_price(x)
          dMarket = "Domain is availible on the market for: " + str(dMarketTemp)
        except Exception:
          dMarket = "Domain is not for sale on the market"
        def pwLog(value):
          print(value)
          w.write(value)
          w.write("\n")
        pwLog(70 * "*")
        dName = "Domain: " + dInfo['name']
        pwLog(dName)
        pwLog(dMarket)
        bids = dInfo['bids']
        numWatching = "Number of people watching: " + str(dInfo['numWatching'])
        pwLog(numWatching)
        numberViews = "Number of views: " + str(dInfo['numberViews'])
        pwLog(numberViews)
        releaseBlock = "Release block: " + str(dInfo['releaseBlock'])
        pwLog(releaseBlock)
        openBlock = "Open block: " + str(dInfo['openBlock'])
        pwLog(openBlock)
        revealBlock = "Reveal block: " + str(dInfo['revealBlock'])
        pwLog(revealBlock)
        closeBlock = "Close block: " + str(dInfo['closeBlock'])
        pwLog(closeBlock)
        try:
          closeAmount = "Close amount: " + str(int(dInfo['closeAmount']) / 1000000)
        except TypeError:
          closeAmount = "Close amount: null"
        pwLog(closeAmount)
        reserved = "Reserved: " + str(dInfo['reserved'])
        pwLog(reserved)
        highestLockup = "Highest lockup: " + str(int(dInfo['highestStakeAmount']) / 1000000)
        pwLog(highestLockup)
        bidAmt = len(bids)
        pwLog("Amount of bids: " + str(bidAmt))
        pwLog("Bids: ")
        bNum = bidAmt
        if bNum < 1:
          pwLog("There are no bids.")
        else:
          for x in bids:
            pwLog(50 * "-")
            pwLog("Bid number: " + str(bNum))
            lockup = "Lockup: " + str(int(x['stake_amount']) / 1000000)
            try:
              bid = "Bid: " + str(int(x['bid_amount']) / 1000000)
            except TypeError:
              bid = "Bid: not revealed"
            try:
              blind = "Blind: " + str((int(x['stake_amount']) - int(x['bid_amount'])) / 1000000)
            except TypeError:
              blind = "Blind: not revealed"
            status = "Status: " + x['status']
            try:
              tx = "TX Hash: " + x['tx_hash']
            except TypeError:
              tx = "TX Hash: not availible"
            cBlock = "Confirm Block: " + str(x['confirm_block'])
            crDateTemp = x['created_at']
            crDate = "Created at " + crDateTemp[12:23] + " on " + crDateTemp[0:10]
          
            pwLog(lockup)
            pwLog(bid)
            pwLog(blind)
            pwLog(status)
            pwLog(tx)
            pwLog(cBlock)
            pwLog(crDate)
            bNum = bNum - 1


    if mChoice == 1:
      sName = [input("What name would you like to get details about? ")]
      marketplace = Marketplace()
      fileName = 'singleLog.txt'
      lookup(sName, marketplace, fileName)

    elif mChoice == 2:
      namesTemp = str(input("TXT File to Import (TXT File name without .txt extension): ")) + ".txt"
      nameFile = open(namesTemp, 'r')
      namesTemp = nameFile.readlines()
      names = []
      for x in namesTemp:
        names.append(x.strip())
      print(names)
      marketplace = Marketplace()
      fileName = str(input("File to write to (without .txt extension): ")) + ".txt"
      lookup(names, marketplace, fileName)
      
    elif mChoice == 3:
      print("[1] Bid amount (Default)")
      print("[2] Price")
      print("[3] Name")
      print("[4] Date")
      sByTemp = input("What would you like to sort by? ")
      if sByTemp == 2:
        sBy = 'price'
      elif sByTemp == 3:
        sBy = 'name'
      elif sByTemp == 4:
        sBy = 'date'
      else:
        sBy = 'bid'
      print("[1] Ascending (Default)")
      print("[2] Descending")
      sDrTemp = input("What direction would you like to sort in? ")
      if sDrTemp == 2:
        sDr = 'desc'
      else:
        sDr = 'asc'
      fCh = str(input("What is the first character (Optional, use # to start with any number)? "))
      if len(fCh) == 1:
        fChTemp = fCh
      elif len(fCh) < 1:
        fChTemp = ''
      else:
        fChTemp = fCh[1]
      if fChTemp.isnumeric() == True:
        fCh = '#'
      else:
        fCh = fChTemp
      try:
        mLn = str(input("What is the max length (Optional)? "))
      except ValueError:
        mLn = '100'
      try:
        offset = int(input("What would you like the offset to be (0 = top 0-100 domains, 1 = 101-200, etc)? "))
      except ValueError:
        offset = 0
      options = {
        "sortKey": sBy,
        "sortDirection": sDr,
        "firstCharacter": fCh,
        "maxLength": mLn,
      }
      marketplace = Marketplace()
      mInfoTemp = marketplace.get_marketplace_domains(offset, options)
      w = open((str(input("What file would you like to write to (without .txt extension)? ")) + ".txt"), "a+" )
      def pwLog(value):
          print(value)
          w.write(value)
          w.write("\n")
      mInfo = mInfoTemp['domains']
      for x in mInfo:
        dId = "ID: " + x['id']
        dName = "Name: " + x['name']
        dPrice = "Price: " + str(int(x['amount']) / 1000000)

        pwLog(50 * "*")
        pwLog(dName)
        pwLog(dId)
        pwLog(dPrice)

    elif mChoice == 4:
      try:
        offset = int(input("What would you like the offset to be (0 = top 0-100 domains, 1 = 101-200, etc)? "))
      except ValueError:
        offset = 0
      w = open((str(input("What file would you like to write to (without .txt extension)? ")) + ".txt"), "a+" )
      def pwLog(value):
          print(value)
          w.write(value)
          w.write("\n")
      marketplace = Marketplace()
      esInfo = marketplace.get_ending_soon(offset)
      for x in esInfo['domains']:
        name = "Name: " + x['name']
        bidAmt = "Amount of bids: " + str(x['total_number_bids'])
        rBlock = "Reveal block: " + str(x['reveal_block'])

        pwLog(50 * "*")
        pwLog(name)
        pwLog(bidAmt)
        pwLog(rBlock)

    elif mChoice == 5:
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

      try:
        offset = int(input("What would you like the offset to be (0 = top 0-100 domains, 1 = 101-200, etc)? "))
      except ValueError:
        offset = 0

      w = open((str(input("What file would you like to write to (without .txt extension)? ")) + ".txt"), "a+" )
      def pwLog(value):
          print(value)
          w.write(value)
          w.write("\n")
      
      gmInfo = marketplace.get_my_domains(offset)
      for x in gmInfo:
        gmName = "Name: " + x['name']
        grBlock = "Renewal block: " + str(x['renewalBlock'])
        uTD = "Up to date: " + str(x['upToDate'])
        gnViews = "Number of views: " + str(x['numberViews'])
        nbNs = "Uses Namebase nameservers: " + str(x['usesOurNameservers'])

        pwLog(50 * "*")
        pwLog(gmName)
        pwLog(grBlock)
        pwLog(uTD)
        pwLog(gnViews)
        pwLog(nbNs)
      
    elif mChoice == 6:
      return

    else:
      print("You must select a valid option!")
      return

  
  dsMenu()





