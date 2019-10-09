import pandas as pd
from entity.Prime_Events import Prime_Events

class Controller_user:
    def __init__(self):
        pass

    def check_input(self):
        df = Prime_Events().Halls_db
        operation = input("enter N to next page" + '\n' + "enter B to exit" + '\n' +
                          "enter index to select hall" + '\n' + "enter F to search hall" + '\n')
        if operation == 'N':
            return 'N'
        elif operation == 'B':
            return 'B'
        elif operation == 'F':
            return 'F'
        elif int(operation) in range(0,df.shape[0]):

            return operation
        else:
            print("Please ensure vaild input" + '\n')
            return self.check_input()

    def view_hall(self):
        df = Prime_Events().Halls_db
        for i in range(1, int(df.shape[0] / 10) + 2):  # for each page, only display 10 halls
            if i == int(df.shape[0] / 10) + 1:
                print(df[int(df.shape[0] / 10) * 10:])
            else:
                print(df[(i - 1) * 10:i * 10])
            operation = self.check_input()
            if operation == 'N':
                continue
            elif operation == 'B':
                return                             # go back to the previous page
            elif operation == 'F':
                res = self.search_hall()
                if res != None:
                    return res
            else:
                return df.iat[int(operation),1]   # return hall_id
        self.view_hall()

    def search_hall(self):
        df = Prime_Events().Halls_db
        address = input("Enter address information to search: " + '\n')
        res = df.loc[df['Hall_description'].str.contains(address)]
        res.index = range(len(res))
        if res.shape[0] == 0:
            print("No correspond information is found" + '\n')
            self.search_hall()
        print(res)
        operation = input("enter index to select hall" + '\n' + "enter any other to go back" + '\n')
        try:
            var = int(operation)
        except ValueError:
            return               # go back to the previous page
        if int(operation) in range(0,res.shape[0]):
            return res.iat[int(operation),1]
        else:
            return

a = Controller_user()
a.view_hall()