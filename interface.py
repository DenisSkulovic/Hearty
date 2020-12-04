import sqlite3
from entry import *
from search_db import *




def menu():
    menu_choice = input("Welcome to your hearty Health prediction please type you choice G: to get prediction S to search results")
    option = ["G", "S"]
    while True:
        if menu_choice not in option:
            print("Please make sure you type the right options")
            continue
        else: 
            if menu_choice == "G":
                entry_data = get_input()
                save_user_input(entry_data)
                # score = prediction(entry_data)to go thourh the prediction model 
                save = save_prediction(score)
                print(results()) 
                print(health_note())

            elif menu_choice == "S":
                get_id = input("What's the ID number?")
                search_db(get_id)

            


