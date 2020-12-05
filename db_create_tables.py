import sqlite3

db_file = 'users_data.db'


def connect(db_file):
    conn = sqlite3.connect(db_file)
    print("connected")
    return conn



def create_tables():
    conn = connect(db_file)
    c = conn.cursor()
    
    drop = "DROP TABLE IF EXISTS entry_data"
    c.execute(drop)

    entries_table ='''CREATE TABLE entry_data (
        id INTEGER PRIMARY KEY, 
        age INTEGER NOT NULL, 
        sex INTEGER NOT NULL, 
        smoker INTEGER NOT NULL, 
        nbr_cigarettes INTEGER NOT NULL, 
        years_smoking INTEGER NOT NULL, 
        fam_hist_coronary_disease INTEGER NOT NULL, 
        fam_hist_diabt INTEGER NOT NULL, 
        heart_resting_rate INTEGER NOT NULL,
        resting_blood_presure INTEGER NOT NULL )'''
        
    c.execute(entries_table)
    
    predictions_table = '''CREATE TABLE IF NOT EXISTS predictions (
        id INTEGER PRIMARY KEY,
        prediction integer NOT NULL,
        date DATE NOT NULL,
        FOREIGN KEY (id) REFERENCES entry_data (id))'''
    c.execute(predictions_table)
    
    print("Table created successfully")


    conn.commit()
    conn.close() 