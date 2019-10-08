import pandas as pd


class Controller_user:
    def __init__(self):
        pass

    def check_input(self):
        operation = input("enter N to next page" + '\n' + "enter B to exit" + '\n' +
                          "enter index to select hall" + '\n' + "enter F to search hall" + '\n')
        if operation == 'n' or operation == 'N':
            return 'N'
        elif operation == 'b' or operation == 'B':
            return 'B'
        elif operation in range(0,self.view_hall().df.shape[0] + 1):
            return operation
        else:
            print("please ensure vaild input")
            self.check_input()

    def view_hall(self):
        df = pd.read_csv('Hall_db.csv')
        for i in range(1, int(df.shape[0] / 10) + 2):  # for each page, only display 10 halls
            if i == int(df.shape[0] / 10) + 1:
                print(df[int(df.shape[0] / 10) * 10:])
            else:
                print(df[(i - 1) * 10:i * 10])
            operation = self.check_input()
            if operation == 'N':
                continue
            elif operation == 'B':
                return
            else:
                return df.iat[operation,1]   # return hall_id
        self.check_input()

    def search_hall(self):
        pass