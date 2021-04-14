budget = {}
class Budget:
    def __init__(self,category,amount):
        self.category = category
        self.amount = amount
    def withdraw(self):
        withdrawAmount = int(input('How much do you wnat to withdraw? \n'))
        newBalance = self.amount - withdrawAmount
        self.amount = newBalance
        print('Your new %s balance is %d' % (self.category, self.amount)) 
    def transfer(self):
        transferTo = int(input('Which category do you want to transfer to? \n (1) Food \n (2) Entertainment \n (3) Transport \n (4) Miscellaneous \n'))
        transferAmount = int(input('How much do you want to transfer? \n'))
        if(transferTo == 1):
             print('%d naira has been transferred from the %s category to the food category' % (transferAmount, self.category))
             categoryOne.amount = categoryOne.amount + transferAmount
             self.amount = self.amount - transferAmount
        elif(transferTo == 2):
             print('%d naira has been transferred from the %s category to the Entertainment category' % (transferAmount, self.category))
             categoryOne.amount = categoryOne.amount + transferAmount
             self.amount = self.amount - transferAmount
        elif(transferTo == 3):
             print('%d naira has been transferred from the %s category to the Transport category' % (transferAmount, self.category))
             categoryOne.amount = categoryOne.amount + transferAmount
             self.amount = self.amount - transferAmount
        elif(transferTo == 4):
             print('%d naira has been transferred from the %s category to the Miscellaneous category' % (transferAmount, self.category))
             categoryOne.amount = categoryOne.amount + transferAmount
             self.amount = self.amount - transferAmount
        else:
            print('error, please try again')
            transferFrom()
    def checkBalance(self):
        print(self.amount)
    def deposit(self):
        depositAmount = int(input('How much do you wnat to deposit? \n'))
        newBalance = self.amount + depositAmount
        self.amount = newBalance
        print('Your new %s balance is %d' % (self.category, self.amount)) 

categoryOne = Budget('Food', 70000)
categoryTwo = Budget('Entertainment', 25000)
categoryThree = Budget('Transport', 20000)
categoryFour = Budget('Miscellaneous', 15000)

def budgetOperation():
    print('This is your monthly budget')
    operation = int(input('What do you want to do? \n (1) withdraw \n (2) transfer \n (3) check balance \n (4) deposit \n (5) nothing \n'))
    if(operation == 1):
        withdrawalFrom()
    elif(operation == 2):
        transferFrom()
    elif(operation == 3):
        checkingBalance()
    elif(operation == 4):
        depositInto()
    elif(operation == 5):
        exit()
    else:
        print('ínvalid option, please try again')
        budgetOperation()

def withdrawalFrom():
    withdrawFrom = int(input('Which category do you want to withdraw from? \n (1) Food \n (2) Entertainment \n (3) Transport \n (4) Miscellaneous \n'))
    if(withdrawFrom == 1):
        categoryOne.withdraw()
    elif(withdrawFrom == 2):
        categoryTwo.withdraw()
    elif(withdrawFrom == 3):
        categoryThree.withdraw()
    elif(withdrawFrom == 4):
        categoryFour.withdraw()
    else:
        print('category not found, please try again')
        withdrawalFrom()
def transferFrom():
    transferringFrom = int(input('Which category do you want to transfer from? \n (1) Food \n (2) Entertainment \n (3) Transport \n (4) Miscellaneous \n'))
    if(transferringFrom == 1):
        categoryOne.transfer()
    elif(transferringFrom == 2):
        categoryTwo.transfer()
    elif(transferringFrom == 3):
        categoryThree.transfer()
    elif(transferringFrom == 4):
        categoryFour.transfer()
    else:
        print('category not found, please try again')
        transferFrom()
def checkingBalance():
    checkingWhichBalance = int(input('Which category do you want to check from? \n (1) Food \n (2) Entertainment \n (3) Transport \n (4) Miscellaneous \n'))
    if(checkingWhichBalance == 1):
        categoryOne.checkBalance()
    elif(checkingWhichBalance == 2):
        categoryTwo.checkBalance()
    elif(checkingWhichBalance == 3):
        categoryThree.checkBalance()
    elif(checkingWhichBalance == 4):
        categoryFour.checkBalance()
    else:
        print('category not found, please try again')
        checkingBalance()
def depositInto():
    depositingInto = int(input('Which category do you want to withdraw from? \n (1) Food \n (2) Entertainment \n (3) Transport \n (4) Miscellaneous \n'))
    if(depositingInto == 1):
        categoryOne.deposit()
    elif(depositingInto == 2):
        categoryTwo.deposit()
    elif(depositingInto == 3):
        categoryThree.deposit()
    elif(depositingInto == 4):
        categoryFour.deposit()
    else:
        print('category not found, please try again')
        depositInto()
budgetOperation()