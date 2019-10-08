class Hall:
    def __init__(self, name, id, desc, deposit, discount=1.0):
        self.Hall_name = name
        self.Hall_ID = id
        self.Hall_description = desc
        self.Deposit = deposit
        self.Discount = discount

    def get_Hall_name(self):
        return self.Hall_name

    def get_Hall_ID(self):
        return self.Hall_ID

    def get_Hall_description(self):
        return self.Hall_description

    def get_Hall_Deposit(self):
        return self.Deposit

    def get_Hall_Discount(self):
        return self.Discount

    def set_Hall_name(self, name):
        self.Hall_name = name

    def set_Hall_ID(self, id):
        self.Hall_ID = id

    def set_Hall_description(self, desc):
        self.Hall_description = desc

    def set_Hall_Deposit(self, deposit):
        self.Deposit = deposit

    def set_Hall_Discount(self, discount):
        self.Discount = discount

