import sqlite3

def db_connection(db):
    print('database connection')
    connection = None
    try:
        connection = sqlite3.connect(db)
        return connection
    except Error as e:
        print(e)
    
    return connection

def create_table(coin, con):
    print('Create table: ' + coin)
    try:            
        c = con.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS " + coin + "(id integer PRIMARY KEY, date integer UNIQUE, price integer)")      
    except sqlite3.Error as e:
        print(e)

def data_record(data, con):
    print('Saving in the database')
    try:        
        c = con.cursor()
        for coin in data:
            insert_query = "INSERT or IGNORE INTO " + coin + "(date, price) values (?,?)"
            c.executemany(insert_query, data[coin])             
    except sqlite3.Error as e:
        print(e)