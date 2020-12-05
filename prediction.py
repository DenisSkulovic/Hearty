import sqlite3
from entry import *

def health_note():
    score = results()
    print("Your results are {score}")
    if score == 0:
        print("The predictions says you have the potential to encounter some hard time with your heart, but thoses are ONLY predictions.\n Take some time to reste your lifesyle")
    if score == 1:
        print("Your health look just fine! Keep up with what you are doings, with hope that all well be well.")
    



def results():
    conn = connect(db_file)
    c = conn.cursor()
    get_results = '''SELECT prediction FROM predictions p
    INNER JOIN entry_data e 
    WHERE e.id == p.id
    AND p.id == (SELECT max(id) FROM predictions)'''
    
    c.execute(get_results)
    results = c.fetchone()
    print(f'this is it {results}')
    c.close()
    return results