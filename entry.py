# need to create a db to collect all users data
# need to get the data from users
# need to save tha data into db
import sqlite3 
from sqlite3 import Error 
import os


db_file = 'users_data.db'



def connect(db_file):
    conn = sqlite3.connect(db_file)
    print("connected")
    return conn



def get_input():
    user_data= []
    age =input("Enter your age ")
    sex= input("what's your gender 0:Female - 1: Male ")   
    smoker = input("are you smoking? 0:No - 1:Yes ")
    nbr_cigarettes = input("How many cigarettes daily? if you dont somke input 0 ")
    years_smoking = input("How many years are you somking? ")
    fam_hist_coronary_disease = input("Do you have history of Coronary disease in your family 0: No, 1: Yes ")
    fam_hist_diabt = input(" Do you hav in you family history for Diabetes 0:No, 1: Yes ")
    heart_resting_rate = input("Whats your resting heart rate average (if you dont know put 80 ")
     
    user_data.append(age)
    user_data.append(sex)
    user_data.append(smoker)
    user_data.append(nbr_cigarettes)
    user_data.append(years_smoking)
    user_data.append(fam_hist_coronary_disease)
    user_data.append(fam_hist_diabt)
    user_data.append(heart_resting_rate)
    
    return tuple(user_data)




def save_user_input(user_data):
 
    query = '''INSERT INTO entry_data (age, sex, smoker, nbr_cigarettes, years_smoking, fam_hist_coronary_disease, fam_hist_diabt,heart_resting_rate)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)'''
    save_to_db(query,user_data)
    



def save_prediction(score):
    
    query = '''INSERT INTO predictions (prediction, date)
                    VALUES (?, ?)'''

    save_to_db(query, score)





def save_to_db(query, data):
    conn = connect(db_file)
    c = conn.cursor()
    c.execute(query,data)
    conn.commit()
    print("Your data was successfuly added to the DataBase")
    conn.close()


