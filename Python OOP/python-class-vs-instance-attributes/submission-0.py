class BankAccount: 
    # TODO: Add class and instance attributes at their appropriate places
    total_balance=0
    total_accounts=0
    def __init__(self,name,balance) -> None:
        self.name=name
        self.balance=balance
        BankAccount.total_balance+=balance
        BankAccount.total_accounts+=1


# TODO: Create two accounts
# TODO: Print the information using the mentioned format
a=BankAccount("Alice",1000)
b=BankAccount("Bob",2000)

print(f"Alice's balance: ${a.balance}")
print(f"Bob's balance: ${b.balance}")
print(f"Total Accounts: {a.total_accounts}")
print(f"Total Balance: ${a.total_balance}")