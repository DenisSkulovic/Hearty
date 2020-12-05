import sqlite3
from entry import connect, db_file


def results():
    conn = connect(db_file)
    c = conn.cursor()
    query = '''SELECT prediction FROM predictions p
    INNER JOIN entry_data e 
    WHERE e.id == p.id
    AND p.id == (SELECT max(id) FROM predictions)'''
    
    c.execute(query)
    results = c.fetchone()
    c.close()
    return results


def get_score_from_db(id):
    conn = connect(db_file)
    c = conn.cursor()
    query = '''SELECT prediction FROM predictions p
    INNER JOIN entry_data e 
    WHERE e.id == p.id
    AND p.id == '''+str(id)
    
    c.execute(query)
    results = c.fetchone()
    c.close()
    return results


def health_note(score):
    print('*****************************************************************************')
    print(f"Your result is - {score}")
    print('*****************************************************************************')
    
