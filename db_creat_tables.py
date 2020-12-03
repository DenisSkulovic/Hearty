import sqlite3

db_file = 'users_data.db'


def create_connection(db_file):
    conn= None
    try:
        conn = sqlite3.connect(db_file)
        print("Opened database successfully")
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()    



def create_tables():
    conn = create_connection(db_file)
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS users_data")
    c.execute('''CREATE TABLE users_data (
        id SERIAL PRIMARY KEY, 
        age INTEGER NOT NULL, 
        sex INTEGER NOT NULL, 
        smoker INTEGER NOT NULL, 
        nbr_cigarettes INTEGER NOT NULL, 
        years_smoking INTEGER NOT NULL, 
        fam_hist_coronary_disease INTEGER NOT NULL, 
        fam_hist_diabt INTEGER NOT NULL, 
        heart_resting_rate INTEGER NOT NULL) ''')
    
    
    
    c.execute('''CREATE TABLE IF NOT EXISTS predictions (
        id SERIAL PRIMARY KEY,
        prediction integer NOT NULL,
        date DATE NOT NULL,
        FOREIGN KEY (id) REFERENCES projects (id))''')
    
    print("Table created successfully")


    conn.commit()
    conn.close() 