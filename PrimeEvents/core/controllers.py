import pandas as pd
from datetime import datetime
from core.entities import Customer, Owner, Admin, Hall, Payment, Booking, Quotation


class UserController:

    def __init__(self):
        pass
        # self.users = pd.read_csv('../data/users.csv')
        # self.halls = pd.read_csv('../data/halls.csv')
        # self.payments = pd.read_csv('../data/payments.csv')
        # self.bookings = pd.read_csv('../data/bookings.csv')
        # self.reviews = pd.read_csv('../data/reviews.csv')
        # self.quotations = pd.read_csv('../data/quotations.csv')

    def register(self, register_type, name, email, password, address='NA', phone='NA'):
        uid = self.generate_id('user')
        # dictionary of lists
        data = {'name': [name], 'email': [email], 'uid': [uid], 'password': [password],
                'address': [address], 'phone': [phone], 'account_type': [register_type]}

        # Write to pandas data frame
        user_row = pd.DataFrame(data)

        # Append Row to csv
        user_row.to_csv('../data/users.csv', mode='a', header=False, index=False)

        # Refresh the data of the controller
        # self.users = pd.read_csv('../data/users.csv')

        # If register successfully
        if register_type == 'Administrator':
            user = Admin(name, email, uid, password)
        elif register_type == 'Customer':
            user = Customer(name, email, uid, password, address, phone)
        elif register_type == 'Owner':
            user = Owner(name, email, uid, password, address, phone)
        return True, user

    def check_login(self, enter_email, enter_password):
        users = pd.read_csv('../data/users.csv')
        for i in range(len(users)):
            name = users.loc[i][0]
            email = users.loc[i][1]
            userid = users.loc[i][2]
            password = users.loc[i][3]
            address = users.loc[i][4]
            phone = users.loc[i][5]
            account_type = users.loc[i][6]
            if str(enter_email) == str(email) and str(enter_password) == str(password):
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

    def check_email_exists(self, email):
        users = pd.read_csv('../data/users.csv')
        exists = False
        if len(users[users['email'] == str(email)]) != 0:
            exists = True
        return exists

    def get_halls_list(self):
        halls = pd.read_csv('../data/halls.csv')
        halls_list = []
        # get numpy array of halls
        for row in halls.values:
            halls_list.append(Hall(row[0], row[1], row[2], row[3], row[4], row[5]))
        return halls_list

    def get_users_list(self):
        users = pd.read_csv('../data/users.csv')
        users_list = []
        for row in users.values:
            users_list.append(Customer(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
        return users_list

    def generate_id(self, name_of_entity):
        data = pd.read_csv('../data/' + name_of_entity + 's.csv')
        if name_of_entity == 'user':
            col = 'uid'
        elif name_of_entity == 'hall':
            col = 'hid'
        elif name_of_entity == 'payment':
            col = 'pid'
        elif name_of_entity == 'booking':
            col = 'bid'
        elif name_of_entity == 'quotation':
            col = 'qid'
        elif name_of_entity == 'review':
            col = 'rid'
        if data.size > 0:
            new_id = int(data.tail(1)[col]) + 1
        else:
            new_id = 1
        return new_id


class CusController(UserController):

    def __init__(self):
        super().__init__()

    def update_booking_date(self, bid, s_date, e_date):
        bookings = pd.read_csv('../data/bookings.csv')
        bookings.loc[bookings['bid'] == int(bid), 's_date'] = s_date
        bookings.loc[bookings['bid'] == int(bid), 'e_date'] = e_date
        bookings.to_csv('../data/bookings.csv', mode='w', header=True, index=False)

    def get_bookings_by_id(self, cid):
        bookings = pd.read_csv('../data/bookings.csv')
        booking_list = []
        for row in bookings[bookings['uid'] == int(cid)].values:
            booking = Booking(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
            booking_list.append(booking)
        return booking_list

    def add_booking(self, payment, qid):
        # once the hall is booked, change its quotation status to 'finished'
        quotations = pd.read_csv('../data/quotations.csv')
        quotations.loc[quotations['qid'] == int(qid), 'status'] = 'completed'
        quotations.to_csv('../data/quotations.csv', header=True, index=False)
        # refresh
        quotations = pd.read_csv('../data/quotations.csv')

        bid = self.generate_id('booking')
        hid = quotations[quotations['qid'] == int(qid)].values[0][1]
        uid = payment.get_send_from()
        now = datetime.now()
        b_date = '{0}-{1}-{2} {3}:{4}:{5}'.format(str(now.day), str(now.month), str(now.year), str(now.hour),
                                                  str(now.minute), str(now.second))
        s_date = quotations[quotations['qid'] == int(qid)].values[0][5]
        e_date = quotations[quotations['qid'] == int(qid)].values[0][6]
        amount = quotations[quotations['qid'] == int(qid)].values[0][7]
        pid = payment.get_transaction_id()
        booking = Booking(bid, hid, uid, b_date, s_date, e_date, amount, pid)
        data = {'bid': [bid], 'hid': [hid], 'uid': [uid], 'b_date': [b_date],
                's_date': [s_date], 'e_date': [e_date], 'amount': [amount], 'pid': [pid]}
        booking_row = pd.DataFrame(data)
        booking_row.to_csv('../data/bookings.csv', mode='a', header=False, index=False)
        # refresh
        # self.bookings = pd.read_csv('../data/bookings.csv')
        return True, booking

    def cancel_booking(self, bid):
        bookings = pd.read_csv('../data/bookings.csv')
        index = bookings[bookings['bid'] == int(bid)].index.values.astype(int)[0]
        bookings = bookings.drop([index])
        bookings.to_csv('../data/bookings.csv', mode='w', header=True, index=False)

    def add_payment(self, cid, qid):
        # generate payment id
        pid = self.generate_id('payment')
        # get system date
        now = datetime.now()
        pay_date = '{0}-{1}-{2} {3}:{4}:{5}'.format(str(now.day), str(now.month), str(now.year), str(now.hour),
                                                    str(now.minute), str(now.second))
        # find the owner id
        quotations = pd.read_csv('../data/quotations.csv')
        hid = quotations[quotations['qid'] == int(qid)].values[0][1]
        halls = pd.read_csv('../data/halls.csv')
        oid = halls[halls['hid'] == int(hid)].values[0][2]

        # find the deposit amount
        amount = float(halls[halls['hid'] == int(hid)].values[0][4]) \
                 + float(halls[halls['hid'] == int(hid)].values[0][4]) \
                 * float(halls[halls['hid'] == int(hid)].values[0][5])

        payment = Payment(pid, pay_date, cid, oid, round(amount, 2))
        # pid,date,send_from,send_to,amount
        data = {'pid': [pid], 'date': [pay_date],
                'send_from': [cid], 'send_to': [oid], 'amount': [amount]}
        payment_row = pd.DataFrame(data)
        payment_row.to_csv('../data/payments.csv', mode='a', header=False, index=False)
        # refresh
        # self.payments = pd.read_csv('../data/payments.csv')
        return True, payment

    def add_quotation(self, hid, s_date, e_date, num_of_ges, cus_id):
        qid = self.generate_id('quotation')
        halls = pd.read_csv('../data/halls.csv')
        hall_name = (halls[halls['hid'] == int(hid)])['Hall_name'].values[0]

        quo = Quotation(qid, hid, hall_name, cus_id, num_of_ges, s_date, e_date)

        data = {'qid': [qid], 'hid': [hid], 'hall_name': [hall_name], 'cus_id': [cus_id],
                'guests': [num_of_ges], 's_date': [s_date], 'e_date': [e_date],
                'amount': [quo.get_amount()], 'status': [quo.get_status()]}
        quotation_row = pd.DataFrame(data)
        quotation_row.to_csv('../data/quotations.csv', mode='a', header=False, index=False)
        # refresh
        # self.quotations = pd.read_csv('../data/quotations.csv')
        return True, quo

    def check_hall_exist(self, hid):
        halls = pd.read_csv('../data/halls.csv')
        return not halls[halls['hid'] == int(hid)].size == 0

    def get_approved_quotations(self, cid):
        quotations = pd.read_csv('../data/quotations.csv')
        quo_list = []
        for row in quotations[(quotations['cus_id'] == int(cid))
                              & (quotations['status'] == 'approved')].values:
            quo = Quotation(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
            quo_list.append(quo)
        return True, quo_list

    def get_deposit_by_qid(self, qid):
        quotations = pd.read_csv('../data/quotations.csv')
        hid = quotations[quotations['qid'] == int(qid)].values[0][1]
        halls = pd.read_csv('../data/halls.csv')
        deposit = halls[halls['hid'] == int(hid)].values[0][4]
        return deposit

    def get_discount_by_qid(self, qid):
        quotations = pd.read_csv('../data/quotations.csv')
        hid = quotations[quotations['qid'] == int(qid)].values[0][1]
        halls = pd.read_csv('../data/halls.csv')
        discount = halls[halls['hid'] == int(hid)].values[0][5]
        return discount

    def generate_receipt(self, payment):
        pid = payment.get_transaction_id()
        p_date = payment.get_transaction_date()
        cid = payment.get_send_from()
        oid = payment.get_send_to()
        amount = payment.get_amount()
        users = pd.read_csv('../data/users.csv')
        cus_name = users[users['uid'] == int(cid)].values[0][0]
        owner_name = users[users['uid'] == int(oid)].values[0][0]
        receipt = 'Transaction ID: ' + str(pid) + '\n' +\
                  'Transaction time: ' + str(p_date) + '\n' +\
                  'Send from: ' + str(cus_name) + '(id=' + str(cid) + ')\n' +\
                  'Send to: ' + str(owner_name) + '(id=' + str(oid) + ')\n' +\
                  'Amount: ' + str(amount)
        return receipt


class OwnerController(UserController):

    def __init__(self):
        super().__init__()

    def get_user_by_qid(self, qid):
        quotations = pd.read_csv('../data/quotations.csv')
        users = pd.read_csv('../data/users.csv')
        row1 = quotations[quotations['qid'] == int(qid)].values[0]
        uid = row1[3]
        row = users[users['uid'] == int(uid)].values[0]
        user = Customer(row[0], row[1], row[2], row[3], row[4], row[5])
        return user

    def get_approve_quotation(self, oid):
        halls = pd.read_csv('../data/halls.csv')
        # first get all hid of this owner
        hid_list = []
        for row in (halls[halls['oid'] == int(oid)]).values:
            hid_list.append(row[1])

        # second get all quotations which match these hid
        quotations = pd.read_csv('../data/quotations.csv')
        quo_list = []
        for hid in hid_list:
            for row in quotations[(quotations['hid'] == int(hid))
                                  & (quotations['status'] == 'approved')].values:
                quo = Quotation(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
                quo_list.append(quo)

        return True, quo_list

    def get_quotations_by_oid(self, oid):
        halls = pd.read_csv('../data/halls.csv')
        # first get all hid of this owner
        hid_list = []
        for row in (halls[halls['oid'] == int(oid)]).values:
            hid_list.append(row[1])

        # second get all quotations which match these hid
        quotations = pd.read_csv('../data/quotations.csv')
        quo_list = []
        for hid in hid_list:
            for row in quotations[(quotations['hid'] == int(hid))
                                  & (quotations['status'] == 'pending')].values:
                quo = Quotation(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
                quo_list.append(quo)

        return True, quo_list

    def update_quotation_status(self, qid, decision, amount):
        if decision == 'R':
            decision = 'rejected'
        else:
            decision = 'approved'
        quotations = pd.read_csv('../data/quotations.csv')
        quotations.loc[quotations['qid'] == int(qid), 'status'] = decision
        quotations.loc[quotations['qid'] == int(qid), 'amount'] = amount
        quotations.to_csv('../data/quotations.csv', header=True, index=False)
        # refresh
        # self.quotations = pd.read_csv('../data/quotations.csv')
        return True

    def delete_booking(self, bid):
        bookings = pd.read_csv('../data/bookings.csv')
        index = bookings[bookings['bid'] == int(bid)].index.values.astype(int)[0]
        bookings = bookings.drop([index])
        bookings.to_csv('../data/bookings.csv', mode='w', header=True, index=False)

    def get_bookings_by_id(self, oid):
        bookings = pd.read_csv('../data/bookings.csv')
        halls = pd.read_csv('../data/halls.csv')
        booking_list = []
        hid_list = []
        for row in halls[halls['oid'] == int(oid)].values:
            hid_list.append(int(row[1]))
        for hid in hid_list:
            for row in bookings[bookings['hid'] == int(hid)].values:
                booking = Booking(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
                booking_list.append(booking)
        return booking_list


class AdminController(UserController):
    def __init__(self):
        super().__init__()
