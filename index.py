#Function that computes and prints the bill
def computebill():
    s = 0
    for i in groceryList.keys():
        s = s+ groceryList[i][0]*groceryList[i][1]
    print("Bill Amounts to Rs "+str(s))
    print('Amount left in your budget is Rs '+str(budget))


# print the grocery list
def printlist():
    print('The Grocery List is as foloows :-')
    print()
    print('Name     Quantity     Price')
    for i in groceryList.keys():
        print(i +'      ' +str(groceryList[i][0] ) +'          ' +str(groceryList[i][1] ) )
    print()


# Function that manages budget
def managebudget(q, p,budget):
    if q*p > budget:
        print()
        print('Cant Buy !! Budget Exceeded')
        print("Things you can add")
        print(list(i for i in groceryList.keys() if groceryList[i][1] <= budget))
    else:
        budget = budget - (q*p)
        print("You now have Rs " + str(budget) + " left")
    return budget


# Function to add items in the grocery list
def addelement():
    global budget
    ename = input('Enter item name:')
    equant = eval(input('Quantity:'))
    eprice = eval(input('Price per unit:'))
    if eprice*equant > budget:
        budget = managebudget(equant, eprice, budget)
    else:

        groceryList[ename] = [equant, eprice]
        budget = managebudget(equant, eprice, budget)


# function to print choices
def printchoices():
    print("Enter Choice :")
    print('   1. Add Items')
    print('   2.Bill')
    print('   3. Exit')
    ch = int(input())
    return ch


# the Grocery list in the form of dictionary {item:[quantity, price]
groceryList = {}

budget = eval(input("Enter Budget : ")) # budget

moreItem = 'Y'
while moreItem == 'Y':
    if int(budget) == 0:
        print('''You don't have money ''')
        printlist()
        exit()
    else:

        ch = printchoices()
        if ch == 1:
            addelement()
            continue
        elif ch == 3:
            printlist()
            exit()
        elif ch == 2:
            computebill()
           # exit()
else:
    printlist()