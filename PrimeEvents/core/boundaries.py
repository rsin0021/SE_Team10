from core.controllers import UserController, OwnerController, CusController, AdminController
from datetime import date
import re


class Page:
    """
    This class help to build user interface.
    An object of this class can be printed as a user friendly page

    title: the title of the page
    content: a list of any object
    options: the options for user to choose which is a dict: (str : str) pairs.
    wide: the number of characters of the page
    """
    def __init__(self, title='Unknown', contents=None, options=None):
        if contents is None:
            contents = []
        if options is None:
            options = dict()
        self.pageTitle = title
        self.index = 1
        self.contents = contents
        if len(contents) > 3:
            self.show_contents = [self.contents[0], self.contents[1], self.contents[2]]
            self.has_next_page = True
            self.max_index = len(contents) // 3 + 1
        else:
            self.show_contents = contents
            self.has_next_page = False
            self.max_index = 1
        self.current_index = 1
        self.options = options
        self.wide = 50

    def __str__(self):
        return self.generateTitleLine() + self.generateBodyLine() + self.generateBottonLine()

    def generateTitleLine(self):
        titleLength = len(self.pageTitle)
        if ((self.wide - 2) - titleLength) % 2 == 0:
            return '+' + '-' * (((self.wide - 2) - titleLength) // 2) \
                   + self.pageTitle + '-' * (((self.wide - 2) - titleLength) // 2) + '+\n'
        else:
            return '+' + '-' * (((self.wide - 2) - titleLength) // 2) \
                   + self.pageTitle + '-' * (((self.wide - 2) - titleLength) // 2 + 1) + '+\n'

    def generateBodyLine(self):
        result = ''
        for content in self.show_contents:
            lines = content.__str__().split('\n')
            for line in lines:
                lineLength = len(line)
                result = result + '|' + line + ' ' * (self.wide - 2 - lineLength) + '|\n'
            result += '|' + '-' * (self.wide - 2) + '|\n'
        result += '|' + ' ' * (self.wide - 2) + '|\n'
        if self.current_index == 1 and self.max_index != 1:
            if 'P' in self.options:
                self.options.pop('P')
            self.options['N'] = 'next page'
        elif self.current_index == self.max_index and self.max_index != 1:
            if 'N' in self.options:
                self.options.pop('N')
            self.options['P'] = 'pre page'
        elif 1 < self.current_index < self.max_index:
            self.options['P'] = 'pre page'
            self.options['N'] = 'next page'
        else:
            if 'P' in self.options:
                self.options.pop('P')
            if 'N' in self.options:
                self.options.pop('N')
        for option in self.options:
            toPrint = 'Press ' + option + ' to ' + self.options[option]
            optionLength = len(toPrint)
            result = result + '|' + toPrint + ' ' * (self.wide - 2 - optionLength) + '|\n'
        return result

    def next_page(self):
        self.current_index += 1
        if self.current_index < self.max_index:
            self.show_contents = [self.contents[self.current_index * 3 - 3],
                                  self.contents[self.current_index * 3 - 2],
                                  self.contents[self.current_index * 3 - 1]]
        elif self.current_index == self.max_index:
            num = len(self.contents) % 3
            self.show_contents = []
            for i in range(len(self.contents) - 1, len(self.contents) - num):
                self.show_contents.append(self.contents[i])

    def pre_page(self):
        self.current_index -= 1
        if self.current_index >= 1:
            self.show_contents = [self.contents[self.current_index * 3 - 3],
                                  self.contents[self.current_index * 3 - 2],
                                  self.contents[self.current_index * 3 - 1]]

    def generateBottonLine(self):
        return '+' + '-'*48 + '+'

    def setTitle(self, title):
        self.pageTitle = title

    def setContents(self, alist):
        self.contents = list(alist)

    def setOptions(self, adict):
        self.options = dict(adict)

    def getTitle(self):
        return self.pageTitle

    def getContents(self):
        return self.contents

    def getOptions(self):
        return self.options


class Scanner:

    def __init__(self):
        self.massage = 'Enter your option: '

    def accept_register_type(self):
        while True:
            user_input = str(input(self.massage))
            if user_input.lower() not in ['c', 'o', 'a']:
                print('Invalid input!! TRY AGAIN')
            elif user_input.lower() == 'c':
                user_input = 'Customer'
                break
            elif user_input.lower() == 'o':
                user_input = 'Owner'
                break
            elif user_input.lower() == 'a':
                user_input = 'Administrator'
                break
        return user_input

    def accept_normal_attributes(self, name):
        self.massage = 'Enter the ' + name + ': '
        while True:
            user_input = str(input(self.massage))
            if not len(user_input) > 0:
                print('Invalid input!! TRY AGAIN')
            else:
                break
        return user_input

    def accept_integer(self, name):
        self.massage = 'Enter the ' + name + ': '
        while True:
            user_input = str(input(self.massage))

            if user_input.isdigit():
                break
            else:
                print('Invalid input!! TRY AGAIN')
        return user_input

    def accept_phone(self):
        self.massage = 'Enter the phone: '
        while True:
            user_input = str(input(self.massage))
            if len(user_input) != 10:
                print('Invalid input!! TRY AGAIN')
            else:
                break
        return user_input

    def accept_option(self, options):
        self.massage = 'Your Option: '
        while True:
            user_input = str(input(self.massage))
            if not user_input.upper() in options:
                print('Invalid input!! TRY AGAIN')
            else:
                break
        return user_input.upper()

    def accept_any_key(self):
        self.massage = ''
        input(self.massage)

    def accept_book_date(self):
        self.massage = 'Book from (YYYY-MM-DD): '
        start_str = str(input(self.massage))
        s_date = date.fromisoformat(start_str)

        self.massage = 'Book until (YYYY-MM-DD): '
        end_str = str(input(self.massage))
        e_date = date.fromisoformat(end_str)

        return s_date, e_date

    def accept_owner_quotation_id(self, quo_list):
        self.massage = 'Enter the Quotation ID: '
        while True:
            user_input = str(input(self.massage))
            if user_input in [str(quo.get_qid()) for quo in quo_list]:
                break
            else:
                print('Invalid input!! TRY AGAIN')
        return user_input

    def accept_owner_decision(self):
        self.massage = 'Enter your decision[A:approve, R:reject]: '

        while True:
            user_input = str(input(self.massage).upper())
            if user_input not in ['A', 'R']:
                print('Invalid input!! TRY AGAIN')
            else:
                break
        return user_input

    def accept_quotation_amount(self):
        self.massage = 'Enter the quotation amount: '

        float_value = re.compile(r'^[+]?[0-9]+\.[0-9]+$')
        int_value = re.compile(r'^[+]?[0-9]+$')
        while True:
            user_input = str(input(self.massage))
            if float_value.match(user_input) or int_value.match(user_input):
                break
            else:
                print('Invalid input!! TRY AGAIN')
        return user_input

    def accept_cus_quotation_id(self, quo_list):
        self.massage = 'Enter the Quotation ID: '
        while True:
            user_input = str(input(self.massage))
            if user_input in [str(quo.get_qid()) for quo in quo_list]:
                break
            else:
                print('Invalid input!! TRY AGAIN')
        return user_input

    def accept_cus_booking_id(self, booking_list):
        self.massage = 'Enter the Booking ID: '
        while True:
            user_input = str(input(self.massage))
            if user_input in [str(booking.get_book_id()) for booking in booking_list]:
                break
            else:
                print('Invalid input!! TRY AGAIN')
        return user_input

    def accept_bankcard_num(self):
        self.massage = 'Enter Bank Card Num(12 digits): '
        while True:
            user_input = str(input(self.massage))
            if user_input.isdecimal() and len(user_input) == 12:
                break
            else:
                print('Invalid input!! TRY AGAIN')
        return user_input

    def accept_valid_date(self):
        self.massage = 'Enter Vaild Date(MM-YY): '
        ok_date = re.compile(r'^([0][1-9])|([1][0-2])-[0-9][0-9]$')
        while True:
            user_input = str(input(self.massage))
            if ok_date.match(user_input):
                break
            else:
                print('Invalid input!! TRY AGAIN')
        return user_input

    def accept_save_code(self):
        self.massage = 'Enter Save Code(3digits): '
        code = re.compile(r'^[0-9]{3}$')
        while True:
            user_input = str(input(self.massage))
            if code.match(user_input):
                break
            else:
                print('Invalid input!! TRY AGAIN')
        return user_input


class UserInterface:

    def __init__(self):
        self.user_controller = UserController()
        self.owner_controller = OwnerController()
        self.cus_controller = CusController()
        self.admin_controller = AdminController()

    # W
    def login_or_rigster_boundary(self):
        welcome_page = Page(title='Welcome to Prime Events',
                            contents=['We are the best hall booking app in FIT5136!'],
                            options={'R': 'register', 'L': 'login', 'C': 'close the program'})
        print(welcome_page)
        scanner = Scanner()
        option = scanner.accept_option(welcome_page.getOptions())
        return option

    # R
    def register_boundary(self):
        # setup the register page
        register_page = Page(title='Register',
                             options={'C': 'register as customer',
                                      'O': 'register as owner',
                                      'A': 'register as admin'})
        # print the page
        print(register_page)

        # get the attributes from user
        scanner = Scanner()
        register_type = scanner.accept_register_type()
        # uid = scanner.accept_normal_attributes('id')
        name = scanner.accept_normal_attributes('name')
        email = scanner.accept_normal_attributes('email')
        password = scanner.accept_normal_attributes('password')
        address = 'NA'
        phone = 'NA'
        if register_type != 'a':
            address = scanner.accept_normal_attributes('address')
            phone = scanner.accept_phone()

        # pass the attributes to controller to do the register process
        state, user = self.user_controller.register(register_type, name, email, password, address, phone)

        # If register successfully display the information of the account
        if state:
            ok_page = Page(title='Register',
                           contents=['Succeed!', user],
                           options={'Any Key': 'go to login/register page'})
            print(ok_page)
        else:
            not_ok_page = Page(title='Register',
                               contents=['Failed!'],
                               options={'Any Key': 'go to login/register page'})
            print(not_ok_page)
        scanner.accept_any_key()
        # To tell main function which boundary should called next
        return 'W'

    # testing
    # L
    def login_boundary(self):
        scanner = Scanner()
        email = scanner.accept_normal_attributes('email')
        password = scanner.accept_normal_attributes('password')
        state, user = self.user_controller.check_login(email, password)
        if not state:
            login_fail_page = Page(title='Login',
                                   contents='Failed!',
                                   options={'Any Key': 'go to login/register page'})
            print(login_fail_page)
            scanner.accept_any_key()
            option = 'W'
        else:
            login_ok_page = Page(title='Login', contents=['Succeeded'], options={'Any Key': 'go to home page'})
            print(login_ok_page)
            scanner.accept_any_key()
            option = 'H'

        return option, user

    # Q
    def request_quotation_boundary(self, user):

        scanner = Scanner()

        while True:
            hid = scanner.accept_normal_attributes('Hall ID(enter -1 to view hall page)')
            if hid == '-1':
                return 'V'
            # check if the hall exists
            exists = self.cus_controller.check_hall_exist(hid)
            if exists:
                break
            else:
                print('Invalid input!! TRY AGAIN')

        s_date, e_date = scanner.accept_book_date()
        num_of_ges = scanner.accept_integer('number of guest')
        cus_id = user.get_user_id()

        # call controller
        state, quo = self.cus_controller.add_quotation(hid, s_date, e_date, num_of_ges, cus_id)

        send_page = Page(title='Request Quotation', contents=['Send successfully!', quo],
                         options={'Any Key': 'go to home page'})
        print(send_page)
        scanner.accept_any_key()
        return 'H'

    # V
    def view_hall_boundary(self):
        scanner = Scanner()
        # Get a halls stored in a list
        halls_list = self.user_controller.get_halls_list()
        view_page = Page(title='View Halls', contents=halls_list,
                         options={'B': 'book a hall', 'S': 'search a hall', 'H': 'home page'})
        print(view_page)
        option = scanner.accept_option(view_page.getOptions())
        while True:
            if option == 'P':
                view_page.pre_page()
            elif option == 'N':
                view_page.next_page()
            else:
                break
            print(view_page)
            option = scanner.accept_option(view_page.getOptions())
        return option

    # B
    def book_hall_boundary(self, user):
        scanner = Scanner()
        state, quo_list = self.cus_controller.get_approved_quotations(user.get_user_id())
        if state:
            if len(quo_list) > 0:
                quo_page = Page(title='Your Approved Quotations', contents=quo_list,
                                options={'C': 'choose', 'B': 'back to view hall page'})
                print(quo_page)
                option = scanner.accept_option(quo_page.getOptions())
            else:
                quo_page = Page(title='Your Approved Quotations', contents=['You have no approved quotation'],
                                options={'Any Key': ' go to home page'})
                print(quo_page)
                scanner.accept_any_key()
                option = 'H'
                return option
            # first choose which hall to book
            if option == 'C':
                qid = scanner.accept_cus_quotation_id(quo_list)
                # second do the pay depose
                next_option, payment = self.pay_depose_boundary(user, qid)

                # if paid
                if next_option in ['R', 'S']:
                    state2, booking = self.cus_controller.add_booking(payment, qid)
                    if next_option == 'R':
                        receipt = self.cus_controller.generate_receipt(payment)
                        receipt_page = Page(title='Your Receipt', contents=[receipt],
                                            options={'Any Key': 'see booking detail'})
                        print(receipt_page)
                        scanner.accept_any_key()
                    if next_option == 'R':
                      booking_ok_page = Page(title='Booking Detail', contents=[booking],
                                           options={'Any Key': 'back to view hall page'})
                      print(booking_ok_page)
                    scanner.accept_any_key()
                    return 'V'
                # if not paid
                elif next_option == 'G':

                    return 'V'
            else:
                return 'V'

    def pay_depose_boundary(self, user, qid):
        scanner = Scanner()
        bankcard = scanner.accept_bankcard_num()
        name = scanner.accept_normal_attributes('Name on the Card')
        valid_date = scanner.accept_valid_date()
        code = scanner.accept_save_code()
        deposit = self.cus_controller.get_deposit_by_qid(qid)
        discount = self.cus_controller.get_discount_by_qid(qid)
        # negative
        cut = float(deposit) * float(discount)
        confirm_page = Page(title='Pay Deposit', contents=['Deposit: ' + str(deposit) + ' - ' + str(-cut)],
                            options={'C': 'confirm', 'G': 'give up'})
        print(confirm_page)
        option1 = scanner.accept_option(confirm_page.getOptions())
        if option1 == 'C':
            state, payment = self.cus_controller.add_payment(user.get_user_id(), qid)
            if state:
                pay_ok_page = Page(title='Pay Deposit', contents=['Payment Approved!', payment],
                                   options={'R': 'print receipt', 'S': 'see booking detail'})
                print(pay_ok_page)
                option = scanner.accept_option(pay_ok_page.getOptions())
                return option, payment
        else:
            return 'G', None

    # RQ
    def response_quotation_boundary(self, owner):
        scanner = Scanner()
        state, quo_list = self.owner_controller.get_quotations_by_oid(owner.get_user_id())
        quo_page = Page(title='Quotation Requests', contents=quo_list,
                        options={'Q': 'response a quotation', 'H': 'go to home page'})
        print(quo_page)
        option = scanner.accept_option(quo_page.getOptions())
        while True:
            if option == 'P':
                quo_page.pre_page()
            elif option == 'N':
                quo_page.next_page()
            else:
                break
            print(quo_page)
            option = scanner.accept_option(quo_page.getOptions())
        if option == 'H':
            return option
        else:
            qid = scanner.accept_owner_quotation_id(quo_list)
            decision = scanner.accept_owner_decision()
            if decision == 'A':
                amount = scanner.accept_quotation_amount()
            else:
                amount = 'Unknown'
            state = self.owner_controller.update_quotation_status(qid, decision, amount)
            if state:
                response_page = Page(title='Quotation Requests', contents=['Response send!'],
                                     options={'Any Key': 'back to quotation requests page'})
                print(response_page)
            else:
                error_page = Page(title='Quotation Requests', contents=['Error!'],
                                  options={'Any Key': 'back to quotation requests page'})
                print(error_page)
            return 'RQ'

    # S
    def search_hall_boundary(self):
        scanner = Scanner()
        keyword = scanner.accept_normal_attributes('keyword to search')
        hall_list = self.cus_controller.get_halls_list()
        result = []
        for hall in hall_list:
            if keyword.lower() in str(hall.get_hall_description()).lower() \
                    or keyword.lower() in str(hall.get_hall_name()).lower():
                result.append(hall)
        if len(result) == 0:
            result = ['No halls found']
        result_page = Page(title='Search Result', contents=result,
                           options={'V': 'View hall page', 'Q': 'Request quotation', 'B': 'Book hall',
                                    'H': 'to home page'})
        print(result_page)
        option = scanner.accept_option(result_page.getOptions())
        while True:
            if option == 'P':
                result_page.pre_page()
            elif option == 'N':
                result_page.next_page()
            else:
                break
            print(result_page)
            option = scanner.accept_option(result_page.getOptions())
        return option

    # H
    def home_page_boundary(self, user):
        scanner = Scanner()
        if user.get_login_as() == 'Customer':
            options = {'V': 'View hall',
                       'S': 'Search hall',
                       'B': 'Book hall',
                       'Q': 'Request quotation',
                       'M': 'Manage booking',
                       'W': 'Logout'}
            home_page1 = Page(title='Home', contents=['Hi! What do you want?'], options=options)
            print(home_page1)
            option = scanner.accept_option(home_page1.getOptions())
        elif user.get_login_as() == 'Owner':
            options = {'MH': 'Manage hall',
                       'M': 'Manage booking',
                       'RQ': 'Response quotation',
                       'W': 'Logout'}
            home_page1 = Page(title='Home', contents=['Hi! What do you want?'], options=options)
            print(home_page1)
            option = scanner.accept_option(home_page1.getOptions())
        elif user.get_login_as() == 'Administrator':
            options = {'U': 'Manage user',
                       'D': 'Manage discount',
                       'W': 'Logout'}
            home_page1 = Page(title='Home', contents=['Hi! What do you want?'], options=options)
            print(home_page1)
            option = scanner.accept_option(home_page1.getOptions())

        return option

    # M
    def cus_manage_booking_boundary(self, user):
        while True:
            scanner = Scanner()
            hall_list = self.cus_controller.get_bookings_by_id(user.get_user_id())
            if len(hall_list) > 0:
                contents = hall_list
                options = {'D': 'change date of a booking', 'C': 'cancel a booking', 'H': 'home page'}
            else:
                contents = ['You don\'t have booking']
                options = {'H': 'home page'}
            manage_booking_page = Page(title='Manage Booking', contents=contents,
                                       options=options)
            print(manage_booking_page)
            option = scanner.accept_option(manage_booking_page.getOptions())
            if option == 'H':
                return option
            while True:
                if option == 'P':
                    manage_booking_page.pre_page()
                elif option == 'N':
                    manage_booking_page.next_page()
                else:
                    break
                print(manage_booking_page)
                option = scanner.accept_option(manage_booking_page.getOptions())
            if option == 'D':
                bid = scanner.accept_cus_booking_id(hall_list)
                s_date, e_date = scanner.accept_valid_date()
                self.cus_controller.update_booking_date(bid, s_date, e_date)
            elif options == 'C':
                bid = scanner.accept_cus_booking_id(hall_list)
                self.cus_controller.cancel_booking(bid)
            else:
                return 'H'

    def close_boundary(self):
        return 'C'

    def manage_hall_boundary(self):
        page = Page(title='Manage Hall', contents=['function being implemented...'],
                    options={'H': 'go to home page'})
        print(page)
        option = Scanner().accept_option(page.getOptions())
        return option

    def manage_user_boundary(self):
        page = Page(title='Manage User', contents=['function being implemented...'],
                    options={'H': 'go to home page'})
        print(page)
        option = Scanner().accept_option(page.getOptions())
        return option

    def manage_discount_boundary(self):
        page = Page(title='Manage Discount', contents=['function being implemented...'],
                    options={'H': 'go to home page'})
        print(page)
        option = Scanner().accept_option(page.getOptions())
        return option
