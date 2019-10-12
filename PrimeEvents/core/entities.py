

# Parent Class User
class User:
    def __init__(self, user_name, user_email, user_id, password):
        self.user_name = user_name
        self.user_email = user_email
        self.user_id = user_id
        self.password = password

    def set_user_name(self, user_name):
        self.user_name = user_name

    def get_user_name(self):
        return self.user_name

    def set_user_email(self, user_email):
        self.user_email = user_email

    def get_user_email(self):
        return self.user_email

    def set_user_id(self, user_id):
        self.user_id = user_id

    def get_user_id(self):
        return self.user_id

    def set_password(self, password):
        self.password = password

    def get_password(self):
        return self.password

    def __str__(self):
        return 'User ID: ' + str(self.user_id) + '\n' + \
               'User Name: ' + str(self.user_name) + '\n' + \
               'E-mail: ' + str(self.user_email) + '\n' + \
               'Password: ' + str(self.password)


# Child Class Customer
class Customer(User):
    def __init__(self, cust_name, cust_email, cust_id, password, cust_address, cust_phone, login_as='Customer'):
        super().__init__(cust_name, cust_email, cust_id, password)

        self.login_as = login_as
        self.cust_address = cust_address
        self.cust_phone = cust_phone

    def set_cust_address(self, cust_address):
        self.cust_address = cust_address

    def get_cust_address(self):
        return self.cust_address

    def set_cust_phone(self, cust_phone):
        self.cust_phone = cust_phone

    def get_cust_phone(self):
        return self.cust_phone

    def get_login_as(self):
        return self.login_as


# Child Class Owner
class Owner(User):
    def __init__(self, own_name, own_email, own_id, password, own_address, own_phone, login_as='Owner'):
        super().__init__(own_name, own_email, own_id, password)

        self.login_as = login_as
        self.own_address = own_address
        self.own_phone = own_phone

    def set_own_address(self, own_address):
        self.own_address = own_address

    def get_own_address(self):
        return self.own_address

    def set_own_phone(self, own_phone):
        self.own_phone = own_phone

    def get_own_phone(self):
        return self.own_phone

    def get_login_as(self):
        return self.login_as


# Child class admin
class Admin(User):
    def __init__(self, admin_name, admin_email, admin_id, password, login_as='Administrator'):
        super().__init__(admin_name, admin_email, admin_id, password)

        self.login_as = login_as

    def get_login_as(self):
        return self.login_as


class Hall:
    def __init__(self, name, hid, oid, desc, deposit, discount=1.0):
        self.hall_name = name
        self.hall_ID = hid
        self.oid = oid
        self.hall_description = desc
        self.deposit = deposit
        self.discount = discount

    def __str__(self):
        return 'Hall Name: ' + self.hall_name + '\n' +\
               'Hall ID: ' + str(self.hall_ID) + '\n' +\
               'Description: ' + '\n' +\
               self.hall_description + '\n' +\
               'Deposit: ' + str(self.deposit) + '\n' +\
               'Discount: ' + str(self.discount)

    def get_oid(self):
        return self.oid

    def set_oid(self, oid):
        self.oid = oid

    def get_hall_name(self):
        return self.hall_name

    def get_hall_id(self):
        return self.hall_ID

    def get_hall_description(self):
        return self.hall_description

    def get_hall_deposit(self):
        return self.deposit

    def get_hall_discount(self):
        return self.discount

    def set_hall_name(self, name):
        self.hall_name = name

    def set_hall_id(self, hid):
        self.hall_ID = hid

    def set_hall_description(self, desc):
        self.hall_description = desc

    def set_hall_deposit(self, deposit):
        self.deposit = deposit

    def set_hall_discount(self, discount):
        self.discount = discount


class Booking:
    def __init__(self, bid, hid, uid, b_date, s_date, e_date, amount, pid):
        self.book_id = bid
        self.hall_ID = hid
        self.user_ID = uid
        self.booking_date = b_date
        self.s_date = s_date
        self.e_date = e_date
        self.amount = amount
        self.pid = pid

    def __str__(self):
        return 'Hall ID: ' + self.hall_ID + '\n' +\
               'Booking Date: ' + str(self.booking_date) + '\n' +\
               'Book from ' + str(self.s_date) +\
               ' To ' + str(self.e_date) + '\n' +\
               'Amount: ' + str(self.amount)

    def get_book_id(self):
        return self.book_id

    def get_hall_id(self):
        return self.hall_ID

    def get_user_id(self):
        return self.user_ID

    def get_booking_date(self):
        return self.booking_date

    def get_s_date(self):
        return self.s_date

    def get_e_date(self):
        return self.e_date

    def get_amount(self):
        return self.amount

    def get_pid(self):
        return self.pid

    def set_book_id(self, bid):
        self.book_id = bid

    def set_hall_id(self, hid):
        self.hall_ID = hid

    def set_user_id(self, uid):
        self.user_ID = uid

    def set_booking_date(self, date):
        self.booking_date = date

    def set_s_date(self, s_date):
        self.s_date = s_date

    def set_e_date(self, e_date):
        self.e_date = e_date

    def set_amount(self, amount):
        self.amount = amount

    def set_pid(self, pid):
        self.pid = pid


class Payment:

    def __init__(self, tid, date, send_from, send_to, amount):
        self.transaction_id = tid
        self.transaction_date = date
        self.send_from = send_from
        self.send_to = send_to
        self.amount = amount

    def __str__(self):
        return 'Transaction ID: ' + str(self.transaction_id) + '\n' +\
               'transaction Date: ' + str(self.transaction_date) + '\n' +\
               'Paid from ' + str(self.send_from) + ' To ' + str(self.send_to) + '\n' +\
               'Amount: ' + str(self.amount)

    def get_transaction_id(self):
        return self.transaction_id

    def get_transaction_date(self):
        return self.transaction_date

    def get_send_from(self):
        return self.send_from

    def get_send_to(self):
        return self.send_to

    def get_amount(self):
        return self.amount

    def set_transaction_id(self, tid):
        self.transaction_id = tid

    def set_transaction_date(self, date):
        self.transaction_date = date

    def set_send_from(self, uid):
        self.send_from = uid

    def set_send_to(self, uid):
        self.send_to = uid

    def set_amount(self, amount):
        self.amount = amount


class Quotation:
    def __init__(self, qid, hall_id, hall_name, cus_id, guests, s_date, e_date, amount='Unknown', status='pending'):
        self.qid = qid
        self.hall_id = hall_id
        self.hall_name = hall_name
        self.user_id = cus_id
        self.guests = guests
        self.s_date = s_date
        self.e_date = e_date
        self.amount = amount
        self.status = status

    def __str__(self):
        return 'Quotation ID: ' + str(self.qid) + '\n' +\
               'Hall Name: ' + str(self.hall_name) + '\n' +\
               'Book from ' + str(self.s_date) +\
               ' To ' + str(self.e_date) + '\n' +\
               'Quotation status:' + str(self.status) + '\n' +\
               'Amount: ' + str(self.amount)

    def set_qid(self, qid):
        self.qid = qid

    def get_qid(self):
        return self.qid

    def set_hall_id(self, hall_id):
        self.hall_id = hall_id

    def get_hall_id(self):
        return self.hall_id

    def set_user_id(self, user_id):
        self.user_id = user_id

    def get_user_id(self):
        return self.user_id

    def set_guests(self, guests):
        self.guests = guests

    def get_guests(self):
        return self.guests

    def set_amount(self, amount):
        self.amount = amount

    def get_amount(self):
        return self.amount

    def set_status(self, status):
        self.status = status

    def get_status(self):
        return self.status

    def get_s_date(self):
        return self.s_date

    def get_e_date(self):
        return self.e_date

    def set_s_date(self, s_date):
        self.s_date = s_date

    def set_e_date(self, e_date):
        self.e_date = e_date

