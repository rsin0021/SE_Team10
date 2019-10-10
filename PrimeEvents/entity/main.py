import pandas as pd
import Prime_events
import methods as m

#Main() Function
def main():
    acc_type=m.account_type_func()
    user_id=m.user_id_func(acc_type)
    name=m.user_name_func(acc_type)
    email=m.user_email_func(acc_type)
    password=m.password_func(acc_type)
    address=m.address_func(acc_type)
    phone=m.phone_func(acc_type)

    # dictionary of lists
    dict = {'name': [name], 'email': [email], 'user_id': [user_id],'password':[password],
            'address':[address],'phone':[phone],'account_type':[acc_type.get_login_as()]}

    #Write to pandas dataframe
    user_row = pd.DataFrame(dict)

    #Append Row to csv
    user_row.to_csv('User_data.csv', mode='a', header=False,index=False)

    #User record

    user_df=Prime_events.user_data.get_user_df()
    print(user_df)

if __name__=='__main__':
    main()