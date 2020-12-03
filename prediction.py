import sqlite3


def connect(db_file):
    conn = sqlite3.connect(db_file)
    print("connected")
    return conn


def health_note():
    score = results()
    print("Your results are {score}")
    if score == 0:
        print("Please watch out ilfe is short, you have to take care of you health")
    if score == 1:
        print("your are at risque...might you your life style and your genetics, watch you habits")
    if score == 2: 
        print(" you are not too much in danger ...I believe some extra sport and healty food will do the job")
    if score ==3 : 
        print("well it looks like you are doing something good...keep on doing it :)")




def results():
    conn = connect(db_file)
    c = conn.cursor
    get_results = '''SELECT prediction FROM predictions p
    INNER JOIN entry_data e 
    WHERE e.id == p.id'''
 

    conn.execute(get_results, health_note())
    conn.commit()
    return results