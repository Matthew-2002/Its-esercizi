class Account:

    account_id: str
    balance: float

    def __init__(self,
        account_id: str
    ):
        self.account_id = account_id
        self.balance: float = 0
    
    def deposit(self,
        amount: float
    )-> None:
        if amount < 0:
            raise ValueError
        self.balance += amount
    
    def get_balance(self)-> float:
        return self.balance

class Bank:
    
    accounts: dict[str, Account]

    def __init__(self):

        self.accounts = {}

    def create_account(self,
        account_id
    )-> Exception|None:
        if account_id in self.accounts:
            raise Exception
        self.accounts[account_id] = Account(account_id)
        return self.accounts[account_id]
        

    def deposit(self,
        account_id,
        amount
    )-> Exception|None:
        if account_id not in self.accounts:
            raise Exception
        self.accounts[account_id].deposit(amount)
    
    def get_balance(self,
        account_id
    )-> Exception|None:
        if account_id not in self.accounts:
            raise Exception
        return self.accounts[account_id].get_balance()
    

 	
def lista_a_dizionario(tuples: list[tuple]) -> dict[str:list[int]]:
    dict_ = {}
    for tuple in tuples:
        if tuple[0] in dict_:
            dict_[tuple[0]].append(tuple[1])
        else:
            dict_[tuple[0]] = [(tuple[1])]
    return dict_

print(lista_a_dizionario([('a', 1), ('b', 2), ('a', 3)]))