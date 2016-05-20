num_cents = int(input( "How much change? :"))
print ("You have " + str(num_cents//25) + " quarters," + str(num_cents % 25//10) + " dimes," + str(num_cents % 25 % 10//5) + " nickels, and "  + str(num_cents % 25 % 10 % 5//1) + " pennies.")
