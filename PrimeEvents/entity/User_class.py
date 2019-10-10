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
        return (self.user_name)

    def set_user_email(self, user_email):
        self.user_email = user_email

    def get_user_email(self):
        return (self.user_email)

    def set_user_id(self, user_id):
        self.user_id = user_id

    def get_user_id(self):
        return (self.user_id)

    def set_password(self, password):
        self.password = password

    def get_password(self):
        return (self.password)


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
        return (self.cust_address)

    def set_cust_phone(self, cust_phone):
        self.cust_phone = cust_phone

    def get_cust_phone(self):
        return (self.cust_phone)

    def get_login_as(self):
        return (self.login_as)


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
        return (self.own_address)

    def set_own_phone(self, own_phone):
        self.own_phone = own_phone

    def get_own_phone(self):
        return (self.own_phone)

    def get_login_as(self):
        return (self.login_as)


# Child class admin

class Admin(User):
    def __init__(self, admin_name, admin_email, admin_id, password, login_as='Administrator'):
        super().__init__(admin_name, admin_email, admin_id, password)

        self.login_as = login_as

    def get_login_as(self):
        return (self.login_as)

