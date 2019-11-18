#!"C:\\Python34\\python.exe"
import cgi, cgitb
import mysql.connector as mdb
import login
from login import *

class Forgot_Password():

    def readFormContent(self):
        frmObj=cgi.FieldStorage()
        UserName=str(frmObj.getvalue("username"))
        Password=str(frmObj.getvalue("password"))
        Re_Password=str(frmObj.getvalue("re_password"))
        return UserName,Password,Re_Password
    
    def executeForgotPasswordQuery(self,cursor,UserName,Password,Re_Password):
        self.cursor=cursor
        self.UserName=UserName
        self.Password=Password
        self.Re_Password=Re_Password
        sql_check_user="SELECT * FROM bank_details WHERE UserName=('%s')" % (UserName)
        cursor.execute(sql_check_user)
        Rows=cursor.fetchall()
        if (Rows):
            if (Password==Re_Password):
                cursor.execute("UPDATE bank_details SET Password=('%s') WHERE UserName=('%s')" % (Password,UserName))
                print('</br></br></br></br></br>')
                print("<center><h3>Password has been updated successfully!</h3></center>")
                logging.info("Password has been updated successfully! UserName: {0}".format(UserName))
                print('<center>Click here to <a href="http://localhost/M3_DD/login.html">Login</a></center>')    
            else:
                print('</br></br></br></br></br>')
                print("<center><h3>Passwords did not match!</h3></center>")
                logging.error("Passwords did not match! UserName: {0}".format(UserName))
                print('<center>Click here to <a href="http://localhost/M3_DD/forgot_password_initial.py">try again</a></center>')
        else:
            print('</br></br></br></br></br>')
            print("<center><h3>Invalid UserName!</h3></center>")
            logging.error("Invalid UserName! UserName: {0}".format(UserName))
            print('<center>Click here to <a href="http://localhost/M3_DD/forgot_password_initial.py">try again</a></center>')


print ("Content-Type: text/html")
print("""
    <TITLE>Reset Password</TITLE>
    """)
logging.basicConfig(filename='my_account_app.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(filename)s:%(message)s')
Forgot_Password_Object=Forgot_Password()
FormOutput=Forgot_Password_Object.readFormContent()
UserName=FormOutput[0]
Password=FormOutput[1]
Re_Password=FormOutput[2]

cursorDB=Login().dbConnection()
cursor=cursorDB[0]
db=cursorDB[1]
Forgot_Password_Object.executeForgotPasswordQuery(cursor,UserName,Password,Re_Password)
db.close()




















