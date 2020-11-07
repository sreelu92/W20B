import dbcreds
import mariadb

conn=None
cursor=None

def insert_data():
    try:
        content=input("Write your content: ")
        cursor.execute("INSERT INTO exploits(content,user_id) VALUES(?,?)", [content,user[0],])
        conn.commit()
        if(cursor.rowcount==1):
            print(" Exploit created successfully")
            print("-----------------------------")
    except mariadb.ProgrammingError:
        print("Operation failed")
        
def select_data():
    try:
        cursor.execute("SELECT content FROM exploits WHERE user_id=?",[user[0],])
        users=cursor.fetchall()
        for user_list in users:
            print(user_list[0])
            print("--------------------------------")
    except mariadb.ProgrammingError:
        print("Operation failed")
       
def get_alldata():
    try:
        cursor.execute("SELECT * FROM exploits ex INNER JOIN hackers ha ON ex.user_id=ha.id WHERE user_id!=?",[user[0],])   
        users=cursor.fetchall()
        for user_list in users:
            print("Alias: "+str(user_list[4]))
                
            print("Content: "+str(user_list[1]))
            print("------------------")
    except mariadb.ProgrammingError:
        print("Operation failed")

def update_exploits():
    try:
        id=input("Enter your exploit's id to update: ")
        content=input("Enter the content to update: ")
        cursor.execute("UPDATE exploits SET content=? WHERE id=?", [content,id])
        conn.commit()    
        if(cursor.rowcount==1):
            print("Exploit updated successfully")
        elif(cursor.rowcount==0):
            print("Update failed")

    except mariadb.ProgrammingError:
        print("Operation failed")




try:
    conn=mariadb.connect(user=dbcreds.user, password=dbcreds.password, host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
    cursor=conn.cursor()
    print("1.Login")
    print("2.Sign up")
    choice= input("Enter your choice: ")
    if(choice=="1"):
        alias=input("Enter your alias: ")
        password=input("Enter your password: ")
        cursor.execute("SELECT * FROM hackers WHERE alias=? AND password=?",[alias,password,])
        users=cursor.fetchall()
        for user in users:
            user[0]
        if(cursor.rowcount==1):
            print("Login Success")
            while True:
                print("1.Enter a new exploit")
                print("2.See all other exploits")
                print("3.See other's exploits")
                print("4.Update exploits")
                print("5.Exit")
                option=input("Enter your option: ")
                if(option=="1"):
                    insert_data()
                elif(option=="2"):
                    select_data()
                elif(option=="3"):
                    get_alldata()
                elif(option=="4"):
                    update_exploits()
                if(option=="5"):
                    break


        else:
            print("no matching user")

    if(choice=="2"):
        alias=input("Enter your alias: ")
        password=input("Enter your password: ")
        cursor.execute("INSERT INTO hackers(alias,password) VALUES(?,?)", [alias,password])
        conn.commit()
        if(cursor.rowcount==1):
            print("Created successfully")
        else:
            print("Something went wrong")

except mariadb.ProgrammingError:
    print("You need lessons")
except mariadb.OperationalError:
    print("seems to be something wrong with the connection")

finally:
    if(cursor!=None):
        cursor.close()
    if(conn!=None):
        conn.rollback()
        conn.close()
