import pandas as pd
from entity.Hall import Hall

class Prime_Events:
    def __init__(self):
        self.User_db = None
        self.Halls_db = pd.read_csv('../table/halls.csv')
        self.Booking_db = None
        self.Payments_db = None
        self.Quotation_db = None
        self.Reviews_db = None

    def generateHallList(self):
        hallList = []
        # get numpy array of halls
        for row in self.Halls_db.values:
            hallList.append(Hall(row[0], row[1], row[2], row[3], row[4]))
        return hallList

    def set_discount(self):
        pass

    def add_user(self):
        pass

    def remove_user(self):
        pass

    def update_user(self):
        pass

