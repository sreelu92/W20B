import dbcreds
import mariadb
import dataFunctions

conn=None
cursor=None


def user_choice(users):
    try:
        while True:
            print("1.Enter a new exploit")
            print("2.See all other exploits")
            print("3.See other's exploits")
            print("4.Update exploits")
            print("5.Exit")
            option=input("Enter your option: ")
            if(option=="1"):
                dataFunctions.insert_data(users)
            elif(option=="2"):
                dataFunctions.select_data(users)
            elif(option=="3"):
                dataFunctions.get_alldata(users)
            elif(option=="4"):
                dataFunctions.update_exploits()
            elif(option=="5"):
                break
            else:
                print("Invalid choice")
    except:
        print("Failed to show choice")        

try:
    conn=mariadb.connect(user=dbcreds.user, password=dbcreds.password, host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
    cursor=conn.cursor()
    print("1.Login")
    print("2.Sign up")
    print("-------------------------------------")
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
            user_choice(users)
            


        else:
            print("no matching user")

    if(choice=="2"):
        alias=input("Enter your alias: ")
        password=input("Enter your password: ")
        cursor.execute("INSERT INTO hackers(alias,password) VALUES(?,?)", [alias,password])
        conn.commit()
        if(cursor.rowcount==1):
            print("Created successfully")
            cursor.execute("SELECT * FROM hackers WHERE alias=? AND password=?",[alias,password,])
            users=cursor.fetchall()
            for user in users:
                user[0]
            user_choice(users)
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
