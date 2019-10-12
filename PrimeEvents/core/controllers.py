import pandas as pd
from core.entities import Customer, Owner, Admin, Hall, Payment, Booking, User


class UserController:

    def __init__(self):
        self.users = pd.read_csv('../data/users.csv')
        self.halls = pd.read_csv('../data/halls.csv')
        self.payments = pd.read_csv('../data/payments.csv')
        self.bookings = pd.read_csv('../data/bookings.csv')
        self.reviews = pd.read_csv('../data/reviews.csv')
        self.quotations = pd.read_csv('../data/quotations.csv')

    def register(self, register_type, uid, name, email, password, address='NA', phone='NA'):

        # dictionary of lists
        data = {'name': [name], 'email': [email], 'uid': [uid], 'password': [password],
                'address': [address], 'phone': [phone], 'account_type': [register_type]}

        # Write to pandas data frame
        user_row = pd.DataFrame(data)

        # Append Row to csv
        user_row.to_csv('../data/users.csv', mode='a', header=False, index=False)

        # Refresh the data of the controller
        self.users = pd.read_csv('../data/users.csv')

        # If register successfully
        if register_type == 'Administrator':
            user = Admin(name, email, uid, password)
        elif register_type == 'Customer':
            user = Customer(name, email, uid, password, address, phone)
        elif register_type == 'Owner':
            user = Owner(name, email, uid, password, address, phone)
        return True, user

    def check_login(self, enter_email, enter_password):
        for i in range(len(self.users)):
            name = self.users.loc[i][0]
            email = self.users.loc[i][1]
            userid = self.users.loc[i][2]
            password = self.users.loc[i][3]
            address = self.users.loc[i][4]
            phone = self.users.loc[i][5]
            account_type = self.users.loc[i][6]
            if enter_email == email and enter_password == password:
                if account_type == 'Administrator':
                    user = Admin(name, email, userid, password)
                    return True, user
                elif account_type == 'Owner':
                    user = Owner(name, email, userid, password, address, phone)
                    return True, user
                elif account_type == 'Customer':
                    user = Customer(name, email, userid, password, address, phone)
                    return True, user
        return False, None

    def get_halls_list(self):
        halls_list = []
        # get numpy array of halls
        for row in self.halls.values:
            halls_list.append(Hall(row[0], row[1], row[2], row[3], row[4]))
        return halls_list

    def get_users_list(self):
        users_list = []
        for row in self.users.values:
            users_list.append(Customer(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
        return users_list

    def generate_id(self, name_of_entity):
        if name_of_entity == 'user':
            col = 'uid'
            data = self.users
        elif name_of_entity == 'hall':
            col = 'hid'
            data = self.halls
        elif name_of_entity == 'payment':
            col = 'pid'
            data = self.payments
        elif name_of_entity == 'booking':
            col = 'bid'
            data = self.bookings
        elif name_of_entity == 'quotation':
            col = 'qid'
            data = self.quotations
        elif name_of_entity == 'review':
            col = 'rid'
            data = self.reviews
        if data.size > 0:
            new_id = int(data.tail(1)[col]) + 1
        else:
            new_id = 1
        return new_id


class CusController(UserController):

    def add_booking(self, bid, hid, uid, b_date, s_date, e_date, amount, pid):
        data = {'bid': [bid], 'hid': [hid], 'uid': [uid], 'b_date': [b_date],
                's_date': [s_date], 'e_date': [e_date], 'amount': [amount], 'pid': [pid]}
        booking_row = pd.DataFrame(data)
        booking_row.to_csv('../data/bookings.csv', mode='a', header=False, index=False)
        self.bookings = pd.read_csv('../data/bookings.csv')
        booking = Booking(bid, hid, uid, b_date, s_date, e_date, amount, pid)
        return True, booking

    def delete_booking(self, bid):
        pass

    def add_payment(self, tid, date, send_from, send_to, amount):
        data = {'tid': [tid], 'date': [date], 'send_from': [send_from],
                'send_to': [send_to], 'amount': [amount]}
        payment_row = pd.DataFrame(data)
        payment_row.to_csv('../data/payments.csv', mode='a', header=False, index=False)
        self.payments = pd.read_csv('../data/payments.csv')
        payment = Payment(tid, date, send_from, send_to, amount)
        return True, payment

    def check_payment(self):
        pass


class OwnerController(UserController):
    pass


class AdminController(UserController):
    pass
