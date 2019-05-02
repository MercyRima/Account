from datetime import datetime


class Account:
    def __init__(self, first_name, second_name):
        self.first_name=first_name
        self.second_name=second_name
        self.balance=0
        self.deposits=[]
        self.withdrawals=[]
        self.loan=0

    def deposit(self,amount):
        time=datetime.now()
        object={"time":time,"amount":amount}
        deposit=amount
        self.balance=self.balance+amount
        self.deposits.append (object)
        print("Hello {} {},you deposited ksh {} in your Account,your current balance is {}".format(self.first_name,self.second_name,amount,self.balance))

    def withdraw(self,amount):
        if amount<self.balance:
            self.balance=self.balance-amount
            time=datetime.now()
            object={"time":time,"amount":amount}
            self.withdrawals.append(object)
            print ("Dear {} {} your withdrawal of ksh {} was successful.your current balance is {}".format(self.first_name,self.second_name,amount,self.balance))
        else:
            print("you have insufficient funds")

    def showbalance(self):
        showbalance=self.balance
        return "your current balance is {}".format (self.balance)

    def my_deposits(self):
        for deposit in self.deposits:
            time=deposit["time"]
            formated_time=time.strftime("%c")
            amount=deposit["amount"]
            print("on {} you deposited {}".format(formated_time,amount))
            

    def my_withdrawals(self):
        for withdrawal in self.withdrawals:
            time=withdrawal["time"]
            formated_time=time.strftime("%c")
            amount=withdrawal["amount"]
            print("you have withdrawn ksh {} on {}".format(amount,formated_time))

            

    def give_loan(self,n):
        loan = n
        total = 0
        for amount in self.deposits:
            amount=amount["amount"]
            total+=amount

        if len(self.deposits)>=5 and n<total/3 and self.loan==0:
            self.loan= self.loan+n
            print("Dear {} {} your loan of {} has been approved".format(self.first_name,self.second_name,n))
        else:
            print("loan not approved")

    def repay_loan(self,f):
        repay=f
        if f < self.loan:
            self.loan=self.loan-f
            print ("Dear {} {},your loan balance is {}".format(self.first_name,self.second_name,self.loan))

        elif f>self.loan:
             extra_repay=f-self.loan
             self.loan=f-extra_repay-self.loan
             self.balance=extra_repay-self.balance
             print("Dear {} {}, your loan is fully paid and your exceeding balance has been deposited to your Account".format(self.first_name,self.second_name))
        
        else:
            self.loan==0
            print("Dear {} {},your loan of {} is fully paid".format(self.first_name,self.second_name,self.loan))


