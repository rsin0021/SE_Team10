import pandas as pd
import User_class

# Method to fetch the user object

def account_type_func():
    account = input("Enter 'C' to register as customer, 'O' to register as owner, 'A' to register as admin : ")
    if (account == 'C'):
        c = User_class.Customer('', '', '', '', '', '')
        return c
    elif (account == 'O'):
        o = User_class.Owner('', '', '', '', '', '')
        return o
    elif (account == 'A'):
        a = User_class.Admin('', '', '', '')
        return a
    else:
        print('Invalid input!! TRY AGAIN')
        return account_type_func()


# Methods for Attribues

def user_id_func(acc_type):
    user_id = input('Enter User ID')
    if len(user_id) > 0:
        acc_type.set_user_id(user_id)
        return user_id
    else:
        return user_id_func(acc_type)


def user_name_func(acc_type):
    name = input('Enter name of the User')
    if len(name) > 0:
        acc_type.set_user_name(name)
        return name
    else:
        return user_name_func(acc_type)


def user_email_func(acc_type):
    email = input('Enter email of the User')
    if len(email) > 0:
        acc_type.set_user_email(email)
        return email
    else:
        return user_email_func(acc_type)


def password_func(acc_type):
    password = input('Enter password ')
    if len(password) > 0:
        acc_type.set_password(password)
        return password
    else:
        return password_func(acc_type)


def address_func(acc_type):
    if acc_type.get_login_as() == 'Customer':
        address = input('Enter User address ')
        if len(address) > 0:
            acc_type.set_cust_address(address)
            return address
        else:
            return address_func(acc_type)


    elif acc_type.get_login_as() == 'Owner':
        address = input('Enter User address ')
        if len(address) > 0:
            acc_type.set_own_address(address)
            return address
        else:
            return address_func(acc_type)

    else:
        address = 'NA'
        return address


def phone_func(acc_type):
    if acc_type.get_login_as() == 'Customer':
        phone = input('Enter User phone number ')
        if len(phone) > 0:
            acc_type.set_cust_phone(phone)
            return phone
        else:
            return phone_func(acc_type)


    elif acc_type.get_login_as() == 'Owner':
        phone = input('Enter User phone number ')
        if len(phone) > 0:
            acc_type.set_own_phone(phone)
            return phone
        else:
            return phone_func(acc_type)

    else:
        phone = 'NA'
        return phone
