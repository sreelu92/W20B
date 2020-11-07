import dbcreds
def insert_data(user):
    for user in users:
        user[0]
    
    try:
        
        conn=mariadb.connect(user=dbcreds.user, password=dbcreds.password, host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
        cursor=conn.cursor()
        content=input("Write your content: ")
        cursor.execute("INSERT INTO exploits(content,user_id) VALUES(?,?)", [content,user[0],])
        conn.commit()
    except:
        print("Operation failed")
        
def select_data(users):
    for user in users:
        user[0]
    try:
        conn=mariadb.connect(user=dbcreds.user, password=dbcreds.password, host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
        cursor=conn.cursor()
        cursor.execute("SELECT content FROM exploits WHERE user_id=?",[user[0],])
        users=cursor.fetchall()
        for user_list in users:
            print(user_list[0])
    except:
        print("Operation failed")
       
def get_alldata(users):
    try:
        cursor.execute("SELECT content FROM exploits WHERE user_id!=?",[users[0],])   
        users=cursor.fetchall()
        for user_list in users:
            print(user_list[0])

    except:
        print("Operation failed")
       

