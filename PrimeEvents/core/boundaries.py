from core.controllers import UserController, OwnerController, CusController, AdminController
from datetime import date


class Page:
    """
    This class help to build user interface.
    An object of this class can be printed as a user friendly page

    title: the title of the page
    content: a list of any object
    options: the options for user to choose which is a dict: (str : str) pairs.
    wide: the number of characters of the page
    """
    def __init__(self, title='Unknown', contents=[], options=dict()):
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


class UserInterface:

    def __init__(self):
        self.user_controller = UserController()
        self.owner_controller = OwnerController()
        self.cus_controller = CusController()
        self.admin_controller = AdminController()

    def login_or_rigster_boundary(self):
        welcome_page = Page(title='Welcome to Prime Events',
                            contents=['We are the best hall booking app in FIT5136!'],
                            options={'R': 'register', 'L': 'login'})
        print(welcome_page)
        scanner = Scanner()
        option = scanner.accept_option(welcome_page.getOptions())
        return option

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
        uid = scanner.accept_normal_attributes('id')
        name = scanner.accept_normal_attributes('name')
        email = scanner.accept_normal_attributes('email')
        password = scanner.accept_normal_attributes('password')
        address = 'NA'
        phone = 'NA'
        if register_type != 'a':
            address = scanner.accept_normal_attributes('address')
            phone = scanner.accept_phone()

        # pass the attributes to controller to do the register process
        state, user = self.user_controller.register(register_type, uid, name, email, password, address, phone)

        # If register successfully display the information of the account
        if state:
            ok_page = Page(title='Register Successfully!',
                           contents=[user],
                           options={'Any Key': 'go to login/register page'})
            print(ok_page)
        else:
            not_ok_page = Page(title='Register Failed!',
                               options={'Any Key': 'go to login/register page'})
            print(not_ok_page)
        scanner.accept_any_key()
        # To tell main function which boundary should called next
        return 'L'

    # testing
    def login_boundary(self):
        scanner = Scanner()
        email = scanner.accept_normal_attributes('email')
        password = scanner.accept_normal_attributes('password')
        state, user = self.user_controller.check_login(email, password)
        if not state:
            login_fail_page = Page(title='Login Failed',
                                   options={'Any Key': 'go to login/register page'})
            print(login_fail_page)
            scanner.accept_any_key()
            option = 'L'
        else:
            login_ok_page = Page(title='Login Succeeded', options={'Any Key': 'go to home page'})
            print(login_ok_page)
            scanner.accept_any_key()
            option = 'H'

        return option, user

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

    # testing
    def book_hall_boundary(self, user):

        # get user inputs
        scanner = Scanner()
        hid = scanner.accept_normal_attributes('Hall ID')
        s_date, e_date = scanner.accept_book_date()
        uid = user.get_user_id()
        bid = self.user_controller.generate_id('booking')
        b_date = date.today()
        pid = None
        amount = 'Unknown'

        # create the booking
        state, booking = self.cus_controller.add_booking(bid, hid, uid, b_date, s_date, e_date, amount, pid)

        # now the booking is added, but cus has to paid deposit to make sure it would not be deleted
        if state:
            book_page = Page(title='Booking Page', contents=[booking],
                             options={'C': 'confirm', 'G': 'give up'})

        print(book_page)
        option = scanner.accept_option(book_page.getOptions())
        if option == 'G':
            # if give up, delete the booking
            self.cus_controller.delete_booking(booking.get_book_id())
        return option
