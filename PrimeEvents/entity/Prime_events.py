import pandas as pd
class Prime_events():

    def __init__(self, user_df=pd.read_csv("User_data.csv")):
        self.user_df = user_df

    def get_user_df(self):
        return self.user_df

user_data=Prime_events()