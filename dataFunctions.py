import dbcreds
import mariadb 
conn=None
cursor=None

def insert_data(users):
    for user in users:
        user[0]
    try:
        conn=mariadb.connect(user=dbcreds.user, password=dbcreds.password, host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
        cursor=conn.cursor()
        content=input("Write your content: ")
        cursor.execute("INSERT INTO exploits(content,user_id) VALUES(?,?)", [content,user[0],])
        conn.commit()
        if(cursor.rowcount==1):
            print(" Exploit created successfully")
            print("-----------------------------")
    except mariadb.ProgrammingError:
        print("Operation failed")

    finally:
        if(cursor!=None):
            cursor.close()
        if(conn!=None):
            conn.rollback()
            conn.close()
        
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
            print("--------------------------------")
    except mariadb.ProgrammingError:
        print("Operation failed")
    finally:
        if(cursor!=None):
            cursor.close()
        if(conn!=None):
            conn.rollback()
            conn.close()
       
def get_alldata(users):
    for user in users:
        user[0]
    try:
        conn=mariadb.connect(user=dbcreds.user, password=dbcreds.password, host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM exploits ex INNER JOIN hackers ha ON ex.user_id=ha.id WHERE user_id!=?",[user[0],])   
        users=cursor.fetchall()
        for user_list in users:
            print("Alias: "+str(user_list[4]))
                
            print("Content: "+str(user_list[1]))
            print("------------------")
    except mariadb.ProgrammingError:
        print("Operation failed")
    finally:
        if(cursor!=None):
            cursor.close()
        if(conn!=None):
            conn.rollback()
            conn.close()

def update_exploits():
    try:
        conn=mariadb.connect(user=dbcreds.user, password=dbcreds.password, host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
        cursor=conn.cursor()
        id=input("Enter your exploit's id to update: ")
        content=input("Enter the content to update: ")
        cursor.execute("UPDATE exploits SET content=? WHERE id=?", [content,id])
        conn.commit()    
        if(cursor.rowcount==1):
            print("Exploit updated successfully")
           
        elif(cursor.rowcount==0):
            print("Update failed")
        print("---------------------------------")

    except mariadb.ProgrammingError:
        print("Operation failed")
    finally:
        if(cursor!=None):
            cursor.close()
        if(conn!=None):
            conn.rollback()
            conn.close()