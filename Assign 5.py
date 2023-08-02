#Project one!
# Author: Saskia Lopez
# July 2023


print('Hello World!')

name = input('Please enter your name')
print('Hello there, ' + name +', how are you? ')


#Project 2
# Author: Saskia Lopez
# July 2023

oranges_per_lbs = float(input('Price of Oranges Per Pound:'))
oranges_bought = float(input('Pounds of Oranges Purchased:'))
apples_per_lbs = float(input('Price of Apples Per Pound:'))
apples_bought = float(input('Pounds of Apples Purchased:'))

orange_total = oranges_per_lbs * oranges_bought
apples_total = apples_bought * apples_per_lbs
groceries_total = orange_total + apples_total
print('Oranges:', orange_total)
print('Apples:', apples_total)
print('Total:', groceries_total)


## Project 3
## Author: Saskia Lopez
## July 2023

months_total = int(input('Please Enter Total number of Months:'))
years_total = months_total //12
months_leftover = years_total % 12


print(months_total, "months is", years_total, "years and", months_leftover, "months")


#Project 4
## Author: Saskia Lopez
## July 2023

beginning_balance = float(input("Beginning Balance: "))
monthly_deps = float(input("Monthly Deposits: "))
withdrawals = float(input("Monthly Withdrawals: "))

end_balance = beginning_balance + monthly_deps - withdrawals


print("Beginning balance is", beginning_balance, ". Ending balance is", end_balance )




