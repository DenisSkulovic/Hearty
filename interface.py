# need to create a db to collect all users data
# need to get the data from users
# need to save tha data into db
import sqlite3 
from sqlite3 import Error 
import db_creat_tables 


db_file = 'users_data.db'

def conn(db_file):
    conn= None
    try:
        conn = sqlite3.connect(db_file)
        print("connected")
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()




user_data= []

def getInput():
    conn = conn
    age =input("Enter your age ")
    sex= input("what's your gender 0:Female - 1: Male ")   
    smoker = input("are you smoking? 0:No - 1:Yes ")
    nbr_cigarettes = input("How many cigarettes daily? if you dont somke input 0 ")
    years_smoking = input("How many years are you somking? ")
    fam_hist_coronary_disease = input("Do you have history of Coronary disease in your family 0: No, 1: Yes ")
    fam_hist_diabt = input(" Do you hav in you family history for Diabetes 0:No, 1: Yes ")
    resting_rate = input("Whats your resting heart rate average (if you dont know put 80 ")
     
    user_data.append(age)
    user_data.append(sex)
    user_data.append(smoker)
    user_data.append(nbr_cigarettes)
    user_data.append(years_smoking)
    user_data.append(fam_hist_coronary_disease)
    user_data.append(fam_hist_diabt)
    user_data.append(resting_rate)
    
    print(user_data)

tbl_users_data = '''SELECT id FROM users_data where id = NULL '''

test = ['lola', '1', '1', '0', '12', '23', '1', '0', '89']

def save_users_data(test, tbl_users_data):
    conn = create_connection(db_file)
    c = conn.cursor()
    print("Opened database successfully")

    add_entry = '''INSERT INTO COMPANY ( age, sex, smoker, nbr_cigarettes, years_smoking, fam_hist_coronary_disease, fam_hist_diabt,resting_rate)
                    VALUES ({test})'''

    conn.execute(add_entry, tbl_users_data)
    conn.commit()
    print("Data in process.....Thank you for participating in our servey")
    conn.close()





    #  VALUES ("{age}, {sex}, {smoker}, {nbr_cigarettes}, {years_smoking}, {fam_hist_coronary_disease}, {fam_hist_diabt},{resting_rate})