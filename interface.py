import joblib
import glob
import os 
import re
import sqlite3
from entry import *
from search_db import *




def retrieve_models(folder):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    models = {}
    for file in os.listdir(f'{dir_path}\\models\\{folder}'):
        model = joblib.load(f'{dir_path}\\models\\{folder}\\{file}')
        pattern = re.compile("(\\w+)(?=__\\d{4}_\\d{1,2}_\\d{1,2}__\\d{1,2}_\\d{1,2})")
        model_name = re.findall(pattern=pattern, string=file)[0]
        models[model_name] = model
    return models
bad_col_models = retrieve_models('bad_col_models')  
better_col_models = retrieve_models('better_col_models')






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
                # entry_data = get_input()
                # save_user_input(entry_data)
                # entry_data = [float(i) for i in entry_data]
                # print(entry_data)
                score = bad_col_models['voting'].predict([[1,2,3,4,5,6,7,8]])
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
                

