import string
import random
import os

def start():
  prefix = input('Enter Prefix (Optional): ')

  tempLength = int(input('Enter Length (Generated names will be this length even if a prefix is given): '))

  amount = int(input('Enter Amount: '))

  prefixLength = len(prefix)

  length = tempLength - prefixLength

  if length <= 0:
    print("The length cannot be less than or equal to your prefix!")
    exit()

  fileName = prefix + "[" + str(length) + "]" + ".txt"

  w = open(fileName,"a+")

  for x in range(amount):
    
    letters = string.ascii_lowercase
    numbers = string.digits

    gen = letters + numbers

    tempName = random.sample(gen,length)

    name = prefix + "".join(tempName)

    print(name)

    w.write(name + "\n")



  seen = set()
  with open(fileName, "r+") as f:
      d = f.readlines()
      f.seek(0)
      for i in d:
          if i not in seen:
              f.write(i)
              seen.add(i)
      f.truncate()

  

