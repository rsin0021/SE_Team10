class Payment:
    def __init__(self, sendFrom, sendTo, amount, id, date):
        self.From = sendFrom
        self.To = sendTo
        self.Amount = amount
        self.Transaction_ID = id
        self.Transaction_Date = date

    def search_payment(self):
        pass

    def view_receipt(self):
        pass

    def __str__(self):
        return s