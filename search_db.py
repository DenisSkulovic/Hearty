import sqlite3 
from sqlite3 import Error 
import db_creat_tables 
from interface import *
from entry import *



def find_entry_in_db_byID(id):
    conn = connect(db_file)
    print(f"Your conection to {db_file} database is done")
    c = conn.cursor()
    select = '''SELECT * FROM entry_data WHERE id = ?'''
    c.execute(select, (id,))
    get_search = c.fetchone()
    c.close()
    return f" Your requested data: {get_search}"
    



# , age, sex, smoker, nbr_cigarettes, years_smoking, fam_hist_coronary_disease, fam_hist_diabt, resting_rate