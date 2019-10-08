class Booking:
    def __init__(self, tid, hallid, uid, date, amount):
        self.Transaction_ID = tid
        self.Hall_ID = hallid
        self.User_ID = uid
        self.Booking_date = date
        self.Amount = amount

    def search_booking(self):
        pass

    def pay_deposit(self):
        pass

    def verify_deposit(self):
        pass

    def get_Transaction_ID(self):
        return self.Transaction_ID

    def get_Hall_ID(self):
        return self.Hall_ID

    def get_User_ID(self):
        return self.User_ID

    def get_Booking_date(self):
        return self.Booking_date

    def get_Amount(self):
        return self.Amount

    def set_Transaction_ID(self, id):
        self.Transaction_ID = id

    def set_Hall_ID(self, id):
        self.Hall_ID = id

    def set_User_ID(self, id):
        self.User_ID = id

    def set_Booking_date(self, date):
        self.Booking_date = date

    def set_Amount(self, amount):
        self.Amount = amount
