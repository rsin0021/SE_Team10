from core.boundaries import UserInterface

prime_events = UserInterface()

while True:
    option = prime_events.login_or_rigster_boundary()
    if option == 'L':
        next_page, user = prime_events.login_boundary()
        break
    elif option == 'R':
        prime_events.register_boundary()


prime_events.response_quotation_boundary(user)
#prime_events.view_hall_boundary()
prime_events.request_quotation_boundary(user)
prime_events.book_hall_boundary(user)


