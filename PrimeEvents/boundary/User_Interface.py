import os
from boundary.Page import Page
from entity.Prime_Events import Prime_Events

class User_Interface:

    def dispaly_bookHallPage(self):
        hallsList = Prime_Events().generateHallList()
        options = {'0': 'Go Back', '1': 'Choose a Hall', '2': 'Search a Hall'}
        page = Page(title='Book Hall Page', contents=hallsList, options=options)
        print(page)
