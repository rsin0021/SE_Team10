import pandas as pd
from core.entities import Customer, Owner, Admin, Hall, Payment, Booking, User, Quotation


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
            halls_list.append(Hall(row[0], row[1], row[2], row[3], row[4], row[5]))
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
        booking = Booking(bid, hid, uid, b_date, s_date, e_date, amount, pid)
        data = {'bid': [bid], 'hid': [hid], 'uid': [uid], 'b_date': [b_date],
                's_date': [s_date], 'e_date': [e_date], 'amount': [amount], 'pid': [pid], 'status': [booking.get_status()]}
        booking_row = pd.DataFrame(data)
        booking_row.to_csv('../data/bookings.csv', mode='a', header=False, index=False)
        self.bookings = pd.read_csv('../data/bookings.csv')
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

    def add_quotation(self, hid, s_date, e_date, num_of_ges, cus_id):
        qid = self.generate_id('quotation')
        hall_name = (self.halls[self.halls['hid'] == 1])['Hall_name'].values[0]

        quo = Quotation(qid, hid, hall_name, cus_id, num_of_ges, s_date, e_date)

        data = {'qid': [qid], 'hid': [hid], 'hall_name': [hall_name], 'cus_id': [cus_id],
                'guests': [num_of_ges], 's_date': [s_date], 'e_date': [e_date],
                'amount': [quo.get_amount()], 'status': [quo.get_status()]}
        quotation_row = pd.DataFrame(data)
        quotation_row.to_csv('../data/quotations.csv', mode='a', header=False, index=False)
        # refresh
        self.quotations = pd.read_csv('../data/quotations.csv')
        return True, quo

    def check_hall_exist(self, hid):
        return not self.halls[self.halls['hid'] == int(hid)].size == 0


class OwnerController(UserController):

    def get_quotations_by_oid(self, oid):
        # first get all hid of this owner
        hid_list = []
        for row in (self.halls[self.halls['oid'] == int(oid)]).values:
            hid_list.append(row[1])

        # second get all quotations which match these hid
        quo_list = []
        for hid in hid_list:
            for row in self.quotations[(self.quotations['hid'] == int(hid))
                                       & (self.quotations['status'] == 'pending')].values:
                quo = Quotation(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
                quo_list.append(quo)

        return True, quo_list

    def update_quotation_status(self, qid, decision, amount):
        if decision == 'R':
            decision = 'rejected'
        else:
            decision = 'approved'
        self.quotations.loc[self.quotations['qid'] == int(qid), 'status'] = decision
        self.quotations.loc[self.quotations['qid'] == int(qid), 'amount'] = amount
        self.quotations.to_csv('../data/quotations.csv', header=True, index=False)
        return True


class AdminController(UserController):
    pass
