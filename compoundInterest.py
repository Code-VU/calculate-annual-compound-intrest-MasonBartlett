def calculateCompoundInterest():
    
# This first 3 lines are provided for yougetACompoundIntrest()
# This first 3 lines are provided for you
    count = 0
    divider = '---'
    while count < 3 :
        client_one_principal = float(input("Principle (amount): "))
        client_one_time =      float(input("Time:               "))
        client_one_rate =      float(input("Rate:               "))

        amount = client_one_principal * (1 + (client_one_rate / 100))**client_one_time

        intrest = round(amount - client_one_principal, 2)

        print ('Compound Interest:', intrest)
        print(divider)
        count = count + 1




 #print("Compound Interest: "+str(intrest))

    # end assignment

## if you want to test locally before you try to sync
## uncomment calculateCompoundInterest() and run > python monkeyCalculator.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN

#calculateCompoundInterest()
