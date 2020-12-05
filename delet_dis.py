import joblib
import glob
import os 
import re

import hearty



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

col_names= {'3':'age',
            '4':'sex',
            '5':'pain_location',
            '6':'pain_provoked_by_excretion',
            '7':'relieved_after_rest',
            '9':'chest_pain_type',
            '10':'resting_blood_pressure_in_Hg_on_admission',
            '12':'serum_cholesterol_in_mg/dl',
            '13':'smoke',
            '14':'cigs_per_day',
            '15':'years_of_smoking',
            '16':'fasting_blood_sugar',
            '17':'fam_hist_of_diabetes',
            '18':'fam_hist_of_heart_disease',
            '19':'resting_electrocardiographic_results',
            '32':'maximum_heart_rate_achieved',
            '33':'resting_heart_rate',
            '37':'resting_blood_pressure',
            '38':'exercise_enduced_angina',
            '43':'height_at_peak_exercise',
            '58':'diagnosis'}

def collect_input(cols):
    user_inputs = {}
    for col in cols:
        user_input = input(f'Please enter value for {col_names[str(col)]} (E to return): ')
        if user_input == 'E':
            user_inputs = 'E'
            return user_inputs
        user_inputs[col] = user_input
    return user_inputs


testing_inputs = collect_input([3,4,13,14,15,17,18,33,37])
