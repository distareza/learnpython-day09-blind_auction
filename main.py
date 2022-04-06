from replit import clear
#HINT: You can call clear() to clear the output in the console.

from art import logo

bids = {}

win_bid = ""
max_bid = 0
while True :
  print(logo)
  name = input("What is your name? ")
  price = int(input("What is your bit? $"))

  if max_bid < price:
    max_bid = price
    win_bid = name
    
  bids[name] = price
  
  answer = input("is there any other bidder [y/n] ?")
  if "n" == answer:
    break
  clear()  

clear()  
print(logo)
print(f"{win_bid} is the winner bidder {max_bid}")