import sqlite3
from entry import *


db_file = 'users_data.db'



def connect(db_file):
    conn = sqlite3.connect(db_file)
    print("connected")
    return conn






def start():
    menu_choice = input("Welcome to your hearty Health prediction please type you choice G: to get prediction S to search results")
    option = ["G", "S"]
    if menu_choice not in option:
        print("Please make sure you type the right options")
    elif:
        if menu_choice == "G":
            entry_data = saveInput()
            # score = prediction(entry_data)to go thourh the prediction model 
            save = savePrediction(score)
            print(results()) 
            print(health_note())

        elif menu_choice == "S":
            search = search_db()

         


