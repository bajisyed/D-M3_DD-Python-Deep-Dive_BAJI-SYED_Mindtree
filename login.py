#!"C:\\Python34\\python.exe"
import cgi,cgitb
import mysql.connector as mdb
import logging

class Login:
    def __init__(self):
        print("""
        <TITLE>ACCOUNT DETAILS</TITLE>
        """)
        logging.basicConfig(filename='my_account_app.log', level=logging.INFO,
                            format='%(asctime)s:%(levelname)s:%(filename)s:%(message)s')

        
    def readFormContent(self):
        frmObj=cgi.FieldStorage()
        UserName=str(frmObj.getvalue("username"))
        Password=str(frmObj.getvalue("password"))
        return UserName,Password
    
    def dbConnection(self):
        db=mdb.connect(host="localhost",
                       user="root",
                       passwd="",
                       db="testdb")
        cursor=db.cursor()
        return cursor,db
    
    def executeSelectQuery(self,cursor,UserName):
        self.cursor=cursor
        self.UserName=UserName
        select_acc_no_sql="SELECT * FROM bank_details WHERE UserName=('%s')" %(UserName)
        cursor.execute(select_acc_no_sql)
        Rows=cursor.fetchall()
        return Rows
    
    def credentialsValidation(self,Rows,UserName,Password):
        self.Rows=Rows
        self.Password=Password
        self.UserName=UserName
        
        if(Rows):
            if(Rows[0][5]==Password):
                logging.info("Login Successful UserName: {0}".format(UserName))
                return True
            else:
                print('<br><br><br><br><br><br><br><br><br><br>')
                print("<center><h3>Invalid Password!</h3></center>")
                logging.error("Login Failed.Invalid Password! UserName: {0}".format(UserName))
                print('<center><h3>Click here to <a href="http://localhost/M3_DD/login.html">Login</a></h3></center>')
        else:
            print('<br><br><br><br><br><br><br><br><br><br>')
            print("<center><h3>Invalid UserName!</h3></center>")
            logging.error("Login Failed.Invalid UserName! UserName: {0}".format(UserName))
            print('<center><h3>Click here to <a href="http://localhost/M3_DD/login.html">Login</a></h3></center>')
            
    def displayDashboard(self,Rows):
        self.Rows=Rows
        Account_Name=str(Rows[0][1])+" "+str(Rows[0][2])
        Acc_No=int(Rows[0][0])
        UserName=str(Rows[0][4])
        Account_Balance=int(Rows[0][6])
        print('<form action="logout.py" method="post">')
        print("""<br><br>&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;
                 &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;
                 &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;
                 &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;
                 &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;
                 &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;
                 <input type="submit" value="Logout">
             """)
        print('</form>')
        print('<br><br>')
        print('<center><h2>M3_DD Bank</h2></center>')
        print('<center><h2>ACCOUNT DETAILS</h2></center>')
        print("<center><b>Account Name : </b>{0}</br></br></center>".format(Account_Name))
        print("<center><b>Account Number : </b>{0}</br></br></center>".format(Acc_No))
        print("<center><b>Account Balance : </b>INR {0}</br></br></center>".format(Account_Balance))
                  
        print('<center><form action="add_payee_initial.py" method="post">')
        print('<input type="hidden" id="Acc_No" name="Acc_No" value="%s">' %(Acc_No))
        print('<input type="submit" value="Add Payee">')
        print('</form></center>')

        print('<center><form action="remove_payee_initial.py" method="post">')
        print('<input type="hidden" id="Acc_No" name="Acc_No" value="%s">' %(Acc_No))
        print('<input type="submit" value="Remove Payee">')
        print('</form></center>')
        
        print('<center><form action="deposit_money_initial.py" method="post">')
        print('<input type="hidden" id="UserName" name="UserName" value="%s">' %(UserName))
        print('<input type="submit" value="Deposit Money">')
        print('</form></center>')
        

        print('<center><form action="transfer_money_initial.py" method="post">')
        print('<input type="hidden" id="UserName" name="UserName" value="%s">' %(UserName))
        print('<input type="submit" value="Transfer Money">')
        print('</form></center>')
        
        
        payee_list_sql="SELECT * FROM payee_details WHERE Acc_No=('%s')" % (Acc_No)
        cursor.execute(payee_list_sql)
        Payee_Rows=cursor.fetchall()
        while(Payee_Rows):
            print('<center><b>Payee List :</b><br></center>')
            print('<center><b>Account Number &nbsp;&nbsp;&nbsp; Account Name &nbsp;&nbsp;&nbsp;Bank Name</b><br></center>')
            for row in Payee_Rows:
                print('<center><input type="radio" name="Payee_Acc_No" value="{0}">&emsp;{1}&emsp;&emsp;&emsp;&emsp;&emsp;{2}&emsp;&emsp;&emsp;{3}<br></center>'.format(row[2],row[2],row[3],row[4]))
            Payee_Rows=cursor.fetchone()
        
    def closeDBconnection(self,db):
        self.db=db
        db.close()


if __name__=="__main__":
    Login_Obj=Login()
    FormInput=Login_Obj.readFormContent()
    UserName=FormInput[0]
    Password=FormInput[1]
    cursorDB=Login_Obj.dbConnection()
    cursor=cursorDB[0]
    db=cursorDB[1]
    Rows=Login_Obj.executeSelectQuery(cursor,UserName)
    LoginResult=Login_Obj.credentialsValidation(Rows,UserName,Password)
    if (LoginResult):
        Login_Obj.displayDashboard(Rows)
    Login_Obj.closeDBconnection(db)
