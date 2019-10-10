from core.boundaries import UserInterface, Page

prime_events = UserInterface()

user = prime_events.login_boundary()
next_boundary = prime_events.register_boundary()
prime_events.view_hall_boundary()
prime_events.book_hall_boundary(user)


