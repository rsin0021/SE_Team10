import pandas as pd


class Controller_user:
    def __init__(self):
        pass

    def check_input(self,df):
        operation = input("enter N to next page" + '\n' + "enter B to exit" + '\n' +
                          "enter index to select hall" + '\n' + "enter F to search hall" + '\n')
        if operation == 'n' or operation == 'N':
            return 'N'
        elif operation == 'b' or operation == 'B':
            return 'B'
        elif operation == 'f' or operation == 'F':
            return 'F'
        elif operation in range(0,df.shape[0] + 1):
            return operation
        else:
            print("Please ensure vaild input" + '\n')
            self.check_input()

    def view_hall(self):
        df = pd.read_csv('Hall_db.csv')
        for i in range(1, int(df.shape[0] / 10) + 2):  # for each page, only display 10 halls
            if i == int(df.shape[0] / 10) + 1:
                print(df[int(df.shape[0] / 10) * 10:])
            else:
                print(df[(i - 1) * 10:i * 10])
            operation = self.check_input(df)
            if operation == 'N':
                continue
            elif operation == 'B':
                return                             # go back to the previous page
            elif operation == 'F':
                self.search_hall()
            else:
                return df.iat[operation,1]   # return hall_id
        self.view_hall()

    def search_hall(self):
        df = pd.read_csv('Hall_db.csv')
        address = input("Enter address information to search: " + '\n')
        res = df.loc[df['Hall_description'].str.contains(address)]
        if res.shape[0] == 0:
            print("No correspond information is found" + '\n')
            self.search_hall()
        print(res)
        operation = input("enter B to go back" + '\n' + "enter index to select hall" + '\n')
        if operation in range(0,res.shape[0] + 1):
            return operation
        else:
            return                             # go back to the previous page