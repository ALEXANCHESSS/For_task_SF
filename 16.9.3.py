class Wallet():
    def __init__(self, name, cash):
        self.name = name
        self.cash = cash

    def get_balance(self):
        return f'Клиент "{self.name}". Баланс {self.cash} руб.'

user1 = Wallet('Иван Петров', 50)
print(user1.get_balance())