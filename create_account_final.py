#!"C:\\Python34\\python.exe"

import cgi, cgitb
import mysql.connector as mdb
import logging

class create_account_final():
    def __init__(self):
        print ("Content-Type: text/html")
        print("""
        <TITLE>Create Account</TITLE>
        """)

    def readFormContent(self):
        frmObj=cgi.FieldStorage()
        fname=str(frmObj.getvalue("fname"))
        lname=str(frmObj.getvalue("lname"))
        dob=str(frmObj.getvalue("dob"))
        username=str(frmObj.getvalue("username"))
        password=str(frmObj.getvalue("password"))
        #New Acc No will be the account number given to the next created account
        New_Acc_No=str(frmObj.getvalue("New_Acc_No"))
        return fname,lname,dob,username,password,New_Acc_No

    def dbConnection(self):
        db=mdb.connect(host="localhost",
                       user="root",
                       passwd="",
                       db="testdb")
        cursor=db.cursor()
        return db,cursor

    def executeInsertQuery(self,db,cursor,FormOutput):
        self.db=db
        self.cursor=cursor
        self.FormOutput=FormOutput
        Balance="0"
        sql_insert="INSERT INTO bank_details VALUES(null,'%s', '%s', '%s', '%s', '%s','%s')" %(FormOutput[0],FormOutput[1],FormOutput[2],FormOutput[3],FormOutput[4],Balance)
        cursor.execute(sql_insert)
        db.commit()

    def verifyAccountCreation(self,New_Acc_No,New_UserName):
        self.New_Acc_No=New_Acc_No
        self.New_UserName=New_UserName
        sql_retrive_Acc_No="SELECT * FROM bank_details ORDER BY Acc_No DESC LIMIT 1"
        cursor.execute(sql_retrive_Acc_No)
        DB_Fetch=cursor.fetchall()
        Acc_No=str(DB_Fetch[0][0])
        UserName=str(DB_Fetch[0][4])

        if Acc_No==New_Acc_No and UserName==New_UserName:
            print("<br><br><br><br><br>")
            print("<center><h3>Your Account has been created successfully!<h3></center>")
            print("<center>Your Account Number :<b>{0}</b></center>".format(Acc_No))
            logging.info('Account Creation is Successful ! UserName: {}'.format(New_UserName))
            print('<center>Click here to <a href="http://localhost/M3_DD/login.html">Login</a></center>')

    def closeDBconnection(self,db):
        self.db=db
        db.close()


logging.basicConfig(filename='my_account_app.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(filename)s:%(message)s')

create_account_final_Object=create_account_final()
FormOutput=create_account_final_Object.readFormContent()
cursorDB=create_account_final_Object.dbConnection()
db=cursorDB[0]
cursor=cursorDB[1]
create_account_final_Object.executeInsertQuery(db,cursor,FormOutput)
create_account_final_Object.verifyAccountCreation(FormOutput[5],FormOutput[3])
create_account_final_Object.closeDBconnection(db)
