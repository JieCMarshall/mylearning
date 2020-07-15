# a group of coins: 1 quarter (25 cents), 1 dime (10 cents), 1 nickel (5 cents), 1 penny (1 cent)
# num_coins(31) = 3

def num_coins(cents):
    if cents < 1:
        return 0
    coins = [25,10,5,1]
    num_of_coins = 0
    for coin in coins:
        if cents < coin:
            pass
        else:
           num_of_coins += cents//coin #floor value
           cents = cents%coin # remaider
           print ("cents is ", cents)
           print ("coins is", coin)

    return num_of_coins

print (num_coins(31))


