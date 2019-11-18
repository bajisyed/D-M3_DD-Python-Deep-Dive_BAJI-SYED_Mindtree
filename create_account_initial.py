#!"C:\\Python34\\python.exe"
import cgi,cgitb
import mysql.connector as mdb
import logging

class create_account_initial():
    def __init__(self):
        print('Content-Type: text/html')
        print("""
        <title>Create Account</title>
        """)

    def readFormContent(self):
        frmObj=cgi.FieldStorage()
    
    def displayCreateAccountForm(self,New_Acc_No):
        self.New_Acc_No=New_Acc_No
        logging.info('Account Creation is initiated !')
        print('<center><b>Your account number will be: {0}</b></center></br>'.format(New_Acc_No))
        print('<center><form action="create_account_final.py" method="post"></center>')
        print('<center>First Name: <input type="text" name="fname"/></br></center></br>')
        print('<center>Last Name: <input type="text" name="lname"/></center></br></br>')
        print('<center>Date of Birth: <input type="text" name="dob"/></center></br></br>')
        print('<center>UserName: <input type="text" name="username"/></center></br></br>')
        print('<center>Password: <input type="password" name="password"/></center></br></br>')
        print('<center>Repeat Password: <input type="password" name="password2"/></center></br></br>')
        print('<center><input type="hidden" id="New_Acc_No" name="New_Acc_No" value="%s"></center>' %(New_Acc_No))
        print('<center><input type="submit" value="Register"/></center>')
        print('</form>')

    def getNewAccountNumber(self,cursor):
        get_New_Acc_No_Sql="SELECT * FROM bank_details ORDER BY Acc_No DESC LIMIT 1"
        cursor.execute(get_New_Acc_No_Sql)
        Rows=cursor.fetchall()
        New_Acc_No=int(Rows[0][0])+1
        return New_Acc_No

    def dbConnection(self):
        db=mdb.connect(host="localhost",
                       user="root",
                       passwd="",
                       db="testdb")
        cursor=db.cursor()
        return db,cursor

    def closeDBconnection(self,db):
        self.db=db
        db.close()

logging.basicConfig(filename='my_account_app.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(filename)s:%(message)s')
create_account_initial_Object=create_account_initial()
create_account_initial_Object.readFormContent()
cursorDB=create_account_initial_Object.dbConnection()
db=cursorDB[0]
cursor=cursorDB[1]
New_Acc_No=create_account_initial_Object.getNewAccountNumber(cursor)
create_account_initial_Object.displayCreateAccountForm(New_Acc_No)
create_account_initial_Object.closeDBconnection(db)
