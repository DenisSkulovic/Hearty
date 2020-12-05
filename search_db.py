import sqlite3 
import db_creat_tables
from entry import connect, db_file
import pandas as pd

cols_used = [3,4,13,14,15,17,18,33,37]

col_names= {'3':'Age',
            '4':'Gender',
            '13':'Smoke Y/N',
            '14':'Cigs/Day',
            '15':'Years smoking',
            '17':'Fam hist. of diabetes',
            '18':'Fam hist. of heart disease',
            '33':'Resting Heart Rate',
            '37':'Resting Blood Pressure'}


def find_entry_in_db_byID(id):
    conn = connect(db_file)
    c = conn.cursor()
    select = '''SELECT * FROM entry_data WHERE id = ?'''
    c.execute(select, (id,))
    result = c.fetchone()
    result = [i for i in result]
    result = result[1:]
    df_column_name = [col_names[str(col)] for col in cols_used]
    df_for_print = pd.Series(data=result, index=df_column_name)
    c.close()
    return df_for_print

    



# , age, sex, smoker, nbr_cigarettes, years_smoking, fam_hist_coronary_disease, fam_hist_diabt, resting_rate