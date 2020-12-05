# need to create a db to collect all users data
# need to get the data from users
# need to save tha data into db
import sqlite3 
from sqlite3 import Error 
import os


db_file = 'users_data.db'



def connect(db_file):
    conn = sqlite3.connect(db_file)
    return conn



def get_input():
    user_data= []
    print('\n-----------------------------------------------------------------------------')
    age =input("Enter your age: ")
    sex= input("What's your gender - Female (0) or Male (1): ")   
    smoker = input("Do you smoke (1/0): ")
    nbr_cigarettes = input("Cigarettes per day (0 if don't smoke): ")
    years_smoking = input("Years of smoking (0 if don't smoke): ")
    fam_hist_coronary_disease = input("History of heart disease in family (1/0): ")
    fam_hist_diabt = input("History of diabetes in family (1/0): ")
    heart_resting_rate = input("Average resting heart rate: ")
    resting_blood_presure =  input("Average resting blood pressure: ")
    
    user_data.append(age)
    user_data.append(sex)
    user_data.append(smoker)
    user_data.append(nbr_cigarettes)
    user_data.append(years_smoking)
    user_data.append(fam_hist_coronary_disease)
    user_data.append(fam_hist_diabt)
    user_data.append(heart_resting_rate)
    user_data.append(resting_blood_presure)
    
    return tuple(user_data)



def save_user_input(user_data): 
    query = '''INSERT INTO entry_data (age, sex, smoker, nbr_cigarettes, years_smoking, fam_hist_coronary_disease, fam_hist_diabt, heart_resting_rate, resting_blood_presure)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)'''
   
    save_to_db(query,user_data)
    


def save_prediction(score, date):
    
    query = '''INSERT INTO predictions (prediction, date)
                    VALUES (?, ?) '''

    save_to_db(query, (score, date))



def save_to_db(query, data):
    conn = connect(db_file)
    c = conn.cursor()
    c.execute(query,data)
    conn.commit()
    conn.close()


