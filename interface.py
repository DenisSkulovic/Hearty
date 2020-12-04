import sqlite3
from entry import *
from search_db import *




def menu():
    
    option = ["G", "S"]
    while True:
        print("\n\n\nWelcome to your HEARTY Health Prediction")
        menu_choice = input("\nPlease type you choice G: to get prediction S to search results")
    
        if menu_choice == "E":
            break
        elif menu_choice not in option:
            print("Please make sure you type the right options")
            continue

        elif menu_choice in option:
             
            if menu_choice == "G":
                entry_data = get_input()
                save_user_input(entry_data)
                # score = prediction(entry_data)to go thourh the prediction model 
                score = 10
                save = save_prediction(score)
                print(results()) 
                print(health_note())
                continue

            elif menu_choice == "S":
                id_input = input("What's the ID number?")
                results= find_entry_in_db_byID(id_input)
            
                print(results)
                input("Enter any key to continue")
                continue
                

