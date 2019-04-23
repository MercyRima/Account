class Account:
	def __init__(self,first_name,second_name,initial_balance):
		self.first_name=first_name
		self.second_name=second_name
		self.initial_balance=initial_balance


	def greetings(self):
		greetings="Hello {} {} Welcome to your bank Account your balance is {}".format(self.first_name,self.second_name,self.initial_balance)
		return greetings
	def deposit(self):
		amount=float(input("enter amount to be deposited: "))
		self.initial_balance +=amount
		print("\n amount deposited:",amount)
	def withdraw(self):
	    amount=float(input("enter amount to be withdrawed:"))	
	    if self.initial_balance>=amount:
	       self.initial_balance-=amount
	       print("\n you withdrawed:",amount)
	    else:
	    	print("\n Insufficient balance")
	    	