class BankAccount:
    def __init__(self, name, account_number, balance):
        self.__name = name
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        self.__service_charge()

    def withdraw(self, amount):
        self.__balance -= amount
        self.__service_charge()

    @property
    def balance(self):
        return self.__balance

    def __service_charge(self):
        self.__balance *= 0.99