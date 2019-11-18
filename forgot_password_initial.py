#!"C:\\Python34\\python.exe"
import cgi, cgitb
import mysql.connector as mdb
import logging

class Forgot_Password_Initial():
    def __init__(self):
        print('Content-Type: text/html')
        print("""
        <title>Reset Password</title>
        """)
        logging.basicConfig(filename='my_account_app.log', level=logging.INFO,
                            format='%(asctime)s:%(levelname)s:%(filename)s:%(message)s')
        

    def readFormContent(self):
        frmObj=cgi.FieldStorage()
        
    def displayForgotPasswordForm(self):
        logging.info('Forgot Password Initiated !')
        print('<center><form action="forgot_password_final.py" method="post">')
        print('</br></br></br></br></br></br>')
        print('UserName: <input type="text" name="username"></br></br>')
        print('Password: <input type="password" name="password"></br></br>')
        print('Repeat Password: <input type="password" name="re_password"></br></br>')
        print('<input type="submit" value="Reset">')
        print('<form></center>')


Forgot_Password_Initial_Object=Forgot_Password_Initial()
Forgot_Password_Initial_Object.readFormContent()
Forgot_Password_Initial_Object.displayForgotPasswordForm()

















