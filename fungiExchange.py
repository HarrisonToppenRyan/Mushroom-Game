# Author : Harrison Toppen-Ryan
# Description : Homework 2, CSCI 141
# Date : October 13th, 2020

# How many shitake mushrooms were found
numFungi = int(input("How many shitake did you find on your trek?: "))
# How many shitake mushrooms were found5
numPorta = int(input("How many portabelle did you find on your trek?: "))
  
print("You mender through the forest, and you encounter a soup chef.")

# How many shitake mushrooms were traded 
numFunTrade = int(input("She says to you, how many shitake would you like to trade?: "))      
# How many Portabella mushrroms were traded 
numPorTrade = int(input("How many portabella would you like to trade?: "))
# How many Shitaki mushrooms the player will have after trading
remFungai = numFungi - numFunTrade
# How many Portabella mushrroms the player will have after trading
remPor = numPorta - numPorTrade 


# This function serves as the question of wheather or not the player wants to trade thier mushrooms or not (Main prupose is to reduce the number of 'if' statemnets)
def askTrade(the_ask, the_rubies, the_remFungi, the_remPor, the_numFungi, the_numPorta):
    
    # player accepts the trade
    if the_ask == "y":
        print("You make the trade! You walk away with", the_rubies, "rubies", the_remFungi,"Shitake mushrooms and", the_remPor, "portabella. ""Soup's on!" )  
    # player declines the trade offer
    elif the_ask == "n":
        print("You decide to not trade with the chief, and walk away with 0 rubies,", the_numFungi,"Shitake mushrooms, and", the_numPorta, "portabella as you continue on your way.")



# If player offers 0 mushrooms or if they offer more mushrooms to trade then they found
if (numFunTrade == 0 and numPorTrade == 0) or (numPorTrade > numPorta) or (numFunTrade > numFungi):
    print("The soup chef twitches and says, 'I do not deal with imaginary mushrooms!' The chef then runs away.")
    raise SystemExit

# If less than 10 Shitaki mushrooms and less than 10 Portabella mushrroms are offered to be traded 
elif numFunTrade < 10 and numPorTrade < 5:
    rubies = int(numFunTrade * 2)
    print("She says, I will offer you", rubies, "rubies.")
    ask = input("Do you wish to take the trade? (y or n): ")
    askTrade(ask,rubies,remFungai,remPor, numFungi, numPorta)
    
# If less than 10 Shitaki mushrooms and more then or equal to 5 Portabella mushrroms are offered to be traded  
elif numFunTrade < 10 and numPorTrade >= 5:
    rubies = int(numPorTrade * 3)
    print("She says, I will offer you", rubies, "rubies.")
    ask = input("Do you wish to take the trade? (y or n): ")
    askTrade(ask,rubies,remFungai,remPor, numFungi, numPorta)

# If the number of Shitaki mushrooms is a multiple of 12 but NOT a multiple of 24 and more then or equal to 20 Portabella mushrroms are offered to be traded  
elif (numFunTrade % 12 == 0 and numFunTrade % 24 != 0) and numPorTrade >= 20:
    rubies = int(numPorTrade * 4)
    print("She says, I will offer you", rubies, "rubies.")
    ask = input("Do you wish to take the trade? (y or n): ")
    askTrade(ask,rubies,remFungai,remPor, numFungi, numPorta)

# If the number of Shitaki mushrooms is a multiple of 12 but NOT a multiple of 24 and more less than 20 Portabella mushrroms are offered to be traded  
elif (numFunTrade % 12 == 0 and numFunTrade % 24 != 0) and numPorTrade < 20:
    rubies = int(numPorTrade)
    print("She says, I will offer you", rubies, "rubies.")
    ask = input("Do you wish to take the trade? (y or n): ")
    askTrade(ask,rubies,remFungai,remPor, numFungi, numPorta)

# If more to equal to and is NOT a mutiple of 12 Shitaki mushrooms and more than 0 Portabella mushrroms are offered to be traded 
elif (numFunTrade >= 10 and numFunTrade % 12 != 0) and numPorTrade > 0:
    rubies = int(numFunTrade * 5)
    print("She says, I will offer you", rubies, "rubies.")
    ask = input("Do you wish to take the trade? (y or n): ")
    askTrade(ask,rubies,remFungai,remPor, numFungi, numPorta)


