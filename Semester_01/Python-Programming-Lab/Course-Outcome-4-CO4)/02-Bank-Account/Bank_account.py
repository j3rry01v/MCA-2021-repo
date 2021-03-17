class Bank:
    __acc_name = ""
    __acc_no = ""
    __acc_type = ""
    __acc_balance = 0

    def __init__(self, a_name, a_no, a_type, a_balance):
        self.__acc_name = a_name
        self.__acc_no = a_no
        self.__acc_type = a_type
        self.__acc_balance = a_balance

    def deposit(self, a_deposit):
        print("Initial balance is  :💵 ", self.__acc_balance)
        print("Deposit is  : 💸 ", a_deposit)
        self.__acc_balance += a_deposit
        print(" Your Current balance is  : 💰", self.__acc_balance)

    def withdraw(self):
        print("Your Current balance is  : ", self.__acc_balance)
        self.amount = int(input("How much amount need to withdraw : "))
        if self.amount > self.__acc_balance:
            print("You don't have enough balance to withdraw !!")
            print("Your Current balance is  : ", self.__acc_balance)
        else:
            print(self.amount, " is withdrawn from .", self.__acc_type)
            self.__acc_balance -= self.amount
            print("Current balance is  : ", self.__acc_balance)

    def acc_info(self):
        print("\n ♦︎ ♦︎ ♦︎ ♦︎ ♦︎ ♦︎ ♦︎ ♦︎ ♦︎ ♦︎ ♦︎ ♦︎ ♦︎ ♦︎ ♦︎ \n")
        print("Account Holder Name 📇 :  ", self.__acc_name)
        print("Account Number  🪙       :  ", self.__acc_no)
        print("Account Type    💳      :  ", self.__acc_type)
        print("Account Balance is  💵    :  ", self.__acc_balance)
    no = input("Enter Account number        : ")
    atype = input("Enter Account type             : ")
    bal = int(input("Enter Account initial balance : "))
    holder = Bank(name, no, atype, bal)

    while True:
        print("\n ❖ ❖ ❖ ❖ ❖ ❖ ❖ ❖ ❖ ❖ ❖ ❖ ❖ ❖ ❖ ❖ ❖ ❖\n")
        opt = int(input("1)Deposit 💰 \n2)Withdraw 💸 \n3)Account info ℹ️ \n0)Exit\nChoose your option :: "))
        print("\n ❖ ❖ ❖ ❖ ❖ ❖ ❖ ❖ ❖ ❖ ❖ ❖ ❖ ❖ ❖ ❖ ❖ ❖ ❖ \n")
        if opt == 1:
            amount = int(input("Deposite amount : "))
            holder.deposit(amount)
        elif opt == 2:
            holder.withdraw()
        elif opt == 3:
            holder.acc_info()
        elif opt == 0:
            break
        else:
            print("Invalid Option !")


if __name__ == "__main__":
    while True:
        main()



