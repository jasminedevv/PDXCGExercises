def getChange(init_cents):
    # if number > 100 give error
    if init_cents > 100:
        init_cents = input("No. There can't be more than 100 cents.\nPlease enter actual change: ")
    # exit early if no change
    if init_cents == 100 or init_cents == 0:
        print("No change!")
        raise SystemExit
    cents = init_cents

    # get the number of quarters (//)
    quarters = cents // 25
    print("%d quarters" % quarters)
    # remove the number of quarters from total
    cents = cents - quarters * 25

    # get dimes
    dimes = cents // 10
    print("%d dimes" % dimes)
    # remove dimes
    cents = cents - dimes * 10

    # get nickels
    nickels = cents // 5
    print("%d nickels" % nickels)
    # remove nickels from total to get pennies
    cents = cents - nickels * 5

    pennies = cents
    print("%d pennies" % pennies)
    if pennies + nickels * 5 + dimes * 10 + quarters * 25 != init_cents:
        print("Except it looks like the function messed up somehow. Time to debug!")

getChange(int(input("Please enter change: ")))
