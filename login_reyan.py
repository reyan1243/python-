import pandas as pd
import numpy as np
import csv
import pandas as pd
import csv
# with open('data.csv', 'r') as csv_file:
#     csv_read = csv.reader(csv_file)
#     #     for line in csv_read:
#     #         print(line)
#     with open('new_data.csv', 'w') as newcsv_file:
#         csv_write = csv.writer(newcsv_file)#, delimiter='-')
#         for line in csv_read:
#             csv_write.writerow(line)
#
############################################################################

        #return record
## login system:

#create new login (usr_name , pass)
#store new login_created data in (txt,csv,json,(dict,list)) file.
#login for existing users
#check weather user exists or pass/usr_name is correct from existing record
#if pass/usr_name is not correct then ask for try again (may be while loop)
#
def load(f):
    data=pd.read_csv(f)
    usr_name=data['user']
    password=data['password']
    a=[]
    for i in usr_name:
        a.append(i)
       # print(i)
    # print(a)
    b=[]
    for i in password:
        b.append(i)
       # print(i)
    # print(b)
    return a,b




new_login=input('do yo want to create new login y/n: ')
if new_login=='y':
 with open('record.csv','a') as record:
     usr=input('enter user name: ')
     pas=input('enter password: ')
     rec='\n'+(usr)+','+(pas)
     record.write(rec)
old_login=input('do yo want to login your existing account y/n: ')
x=True
while x:

    if old_login=='y':
        usr_l,pas_l=load('record.csv')
        username = input('Enter username: ')
        passw = input('Enter password: ')
        if  username in usr_l and passw in pas_l:
            print('***Welcome you are logged in***')
            break
        else:
            print('no such pass/user')
            try_again=input('Do yo want to try again y/n: ')
            if try_again=='y':
                continue
                x=True
            else:
                break
    else:
        x=False





