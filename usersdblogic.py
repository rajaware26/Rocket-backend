import mysql.connector
import user
from datetime import date, datetime, timedelta

config = {
    'user': 'rocket',
    'password': 'r0ck3t',
    'host': 'nickarli.com',
    'database': 'rocket'
}
db = mysql.connector.connect(**config)
cursor=db.cursor()


def Create_User(first: str, last: str, username :str, password: str):        #This function takes in name(first and last) username and password and adds them to the database
    myDate = date.today()
    add_user = ("INSERT INTO users "
                "(USERSFIRSTNAME, USERSLASTNAME, USERSDATEADDED, USERSUSERNAME, USERSPASSWORD) "
                "VALUES (%(USERSFIRSTNAME)s, %(USERSLASTNAME)s, %(USERSDATEADDED)s, %(USERSUSERNAME)s, %(USERSPASSWORD)s)")
    user_info = {
    'USERSFIRSTNAME': first,
    'USERSLASTNAME': last,
    'USERSDATEADDED': myDate,
    'USERSUSERNAME': username,
    'USERSPASSWORD': password
    }
    cursor.execute(add_user,user_info)
    db.commit()
    cursor.close()
    db.close()
#Create_User("Elle","Cain","eac","321")  #Calling function with generic args to test it works





def select_User(id : int):  #function to select user given userId param
    userId = str(id)
    query = "SELECT * FROM users where USERSID = " + userId
    cursor.execute(query)
    for(USERSID,USERSFIRSTNAME, USERSLASTNAME, USERSDATEADDED) in cursor:
        myUser = user.User(USERSID, USERSFIRSTNAME, USERSLASTNAME, USERSDATEADDED)
    cursor.close()
    print(myUser.outputFields())
    db.close()
#select_User(7)

def select_User_By_Name(first : str,last : str)->int:  #function to return userId given first and last name param
    query = "SELECT USERSID FROM users WHERE USERSFIRSTNAME = '" + first + "' AND USERSLASTNAME = '" + last + "';"
    cursor.execute(query)
    for(USERSID) in cursor:
        cursor.close()
        db.close()
        return USERSID[0]
    
#print(select_User_By_Name("Ron","Cain"))

def select_User_By_Login_Info(username : str,password : str)->int:  #function to return userid given username and password as params
    query = "SELECT USERSID FROM users WHERE USERSUSERNAME = '" + username + "' AND USERSPASSWORD = '" + password + "';"
    cursor.execute(query)
    for(USERSID) in cursor:
        cursor.close()
        db.close()
        if USERSID is None:
                return None
        else:
            return USERSID[0]

def Login(username : str,password : str)->bool: #this function will be called from front end when users try to login
    if select_User_By_Login_Info(username, password) is None:
        print("The username and password entered were incorrect")
        return False
    else:
        print("Login was successful for user with username " + username + "!")
        return True
#print(Login("eac","321"))

