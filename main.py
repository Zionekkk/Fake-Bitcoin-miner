from colorama import Fore
import time
import secrets
from random import randint
btcval = 28858.20
try:
  with open("bal.txt", "r") as file:
    total_balance = float(file.read().strip())
except ValueError:
  total_balance = 0
total_balance = float(open("bal.txt", "r").read().strip())
while True:
  with open("bal.txt", "w") as file:
    file.write(str(total_balance))
  time.sleep(.1)
  ranInt = randint(0, 2500)
  if ranInt <= 1:
    randomBTC = randint(1,220)/100
    balance = round(btcval * randomBTC, 2) 
    total_balance += balance 
    print(Fore.WHITE + "> 0x" + secrets.token_hex(20) + Fore.GREEN + " > " + str(randomBTC) + " BTC ($" + str("{:,}".format(balance)) + ") Total Balance: $" + str("{:,}".format(round(total_balance,2))))
    time.sleep(0.5)
  else:
    print(Fore.WHITE + "> 0x" + secrets.token_hex(20) + Fore.RED + " > 0.00 BTC ($0.00)")
