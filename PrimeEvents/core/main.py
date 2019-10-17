from core.boundaries import UserInterface


class PrimeEvent:

    def __init__(self):
        self.user = None
        self.ui = UserInterface()
        self.states = {'W': self.ui.login_or_rigster_boundary,
                       'R': self.ui.register_boundary,
                       'L': self.ui.login_boundary,
                       'C': self.ui.close_boundary,
                       'H': self.ui.home_page_boundary,
                       'V': self.ui.view_hall_boundary,
                       'S': self.ui.search_hall_boundary,
                       'B': self.ui.book_hall_boundary,
                       'Q': self.ui.request_quotation_boundary,
                       'M': self.ui.cus_manage_booking_boundary,
                       'RQ': self.ui.response_quotation_boundary,
                       'MH': self.ui.manage_hall_boundary,
                       'U': self.ui.manage_user_boundary,
                       'D': self.ui.manage_discount_boundary,
                       'MB': self.ui.owner_manage_booking_boundary}

    def main(self):
        option = 'W'
        while option != 'C':
            if option == 'L':
                option, self.user = self.states[option]()
            elif option in ['C', 'B', 'Q', 'M', 'H', 'RQ', 'MB']:
                option = self.states[option](self.user)
            else:
                option = self.states[option]()


if __name__ == '__main__':
    program = PrimeEvent()
    program.main()


