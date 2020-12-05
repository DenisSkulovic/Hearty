import joblib
import glob
import os 
import re
import sqlite3
import prediction
import entry 
import search_db
import datetime
import seaborn as sns
import matplotlib.pyplot as plt


def retrieve_files(folder):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    files = {}
    for filename in os.listdir(f'{dir_path}\\models\\{folder}'):
        file = joblib.load(f'{dir_path}\\models\\{folder}\\{filename}')
        pattern = re.compile("(\\w+)(?=__\\d{4}_\\d{1,2}_\\d{1,2}__\\d{1,2}_\\d{1,2})")
        name = re.findall(pattern=pattern, string=filename)[0]
        files[name] = file
    return files


def get_conf_matrix(model_name, current_subset):
    if current_subset == "bad":
        return bad_col_conf_matrices[model_name]
    else:
        return better_col_conf_matrices[model_name]

def get_model(model_name, current_subset):
    if current_subset == "bad":
        return bad_col_models[model_name]
    else:
        return better_col_models[model_name]
    
def get_clf_report(model_name, current_subset):
    if current_subset == "bad":
        return bad_col_clf_reports[model_name]
    else:
        return better_col_clf_reports[model_name]    

   


bad_col_models = retrieve_files('bad_col_models')  
better_col_models = retrieve_files('better_col_models')

bad_col_clf_reports = retrieve_files('bad_col_clf_reports')  
better_col_clf_reports = retrieve_files('better_col_clf_reports')

bad_col_conf_matrices = retrieve_files('bad_col_conf_matrices')  
better_col_conf_matrices = retrieve_files('better_col_conf_matrices')


model_name = 'voting'
current_subset = 'bad'
model = bad_col_models[model_name]
clf_report = bad_col_clf_reports[model_name]

    


def menu():
    global current_subset
    global model_name
    
    option = ["G", "R", "S", "C"]
    while True:
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
        print('*****************************************************************************')
        print("                 Welcome to HEARTY Heart Disease Prediction                  ")
        print('*****************************************************************************')
        print('\
HEARY is a reminder that heart disease diagnosis requires medical examination. \n\
Use the below interface to get a poor prediction of heart disease by answering \n\
simple questions. \n\
HEARTY uses models trained on two subsets of a dataset from data.world \n\
The first subset is questions you can answer without consulting a doctor. \n\
The second subset are recordings of medical examinations. \n\
\n\
As one might suspect, the models trained on the second subset are much more precise. \n\
\n\
Instead of trying so self-diagnose, go see a doctor in case of any symptom.')
        print('*****************************************************************************')
        print(f"Current model - {model_name}")
        print(f"Current subset - {current_subset}")
        print('*****************************************************************************')
        print('\
Main Menu: \n\
    G: Get Prediction \n\
    R: Get model statistics \n\
    C: Change settings \n\
    S: Search previous result in the Database \n\
    ')
        print('*****************************************************************************')
        menu_choice = input("Please type your choice (E to exit): ")
    
        if menu_choice == "E":
            break
        elif menu_choice not in option:
            print("Please make sure you type the right options")
            continue

        elif menu_choice in option:
             
            if menu_choice == "G":
                entry_data = entry.get_input()
                entry.save_user_input(entry_data)
                entry_data = [float(i) for i in entry_data]
               
                score = get_model(model_name, current_subset='bad').predict([entry_data])
               
                date = datetime.datetime.now()
               
                entry.save_prediction(str(score[0]), date.strftime('%m-%d-%Y'))
                
                prediction.health_note(score[0])
                input("Enter any key to continue...")
                continue
            
            elif menu_choice == "R":
                print('-----------------------------------------------------------------------------')
                sns.heatmap(get_conf_matrix(model_name, current_subset), annot=True, fmt="d")
                plt.show()
                print(get_clf_report(model_name, current_subset))
                print('-----------------------------------------------------------------------------')
                input("Enter any key to continue...")
                continue
            
            elif menu_choice == "C":
                user_input1 = input("Change the subset to 'bad' or 'better': ")
                user_input2 = input("\
Change the model to: \
options - 'lr','knn','gauss','d_tree','r_forest','g_boost','nn','voting'\n")
                if user_input1 not in ["bad", "better"]:
                    input("Incorrect entry. Enter any key to continue...")
                    continue
                elif user_input2 not in ['lr','knn','gauss','d_tree','r_forest','g_boost','nn','voting']:
                    input("Incorrect entry. Enter any key to continue...")
                    continue
                current_subset = user_input1
                model_name = user_input2
                continue
                


            elif menu_choice == "S":
                print('-----------------------------------------------------------------------------')
                id_input = input("Enter your system ID: ")
                print('-----------------------------------------------------------------------------')
                results = search_db.find_entry_in_db_byID(id_input)

                retrieved_score = prediction.get_score_from_db(id_input)
                print(results)
                print(f'\nThe score for this ID is - {retrieved_score[0]}')
                input("Enter any key to continue...")
                continue
                

