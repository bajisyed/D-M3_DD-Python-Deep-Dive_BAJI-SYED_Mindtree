#!"C:\\Python34\\python.exe"
import cgi, cgitb
import mysql.connector as mdb

class logout():

    def __init__(self):
        print ("Content-Type: text/html")
        print("""
        <TITLE>Logout</TITLE>
        """)
        print('<br><br><br><br><br>')
        print('<center><h3>You have been successfully logged out!</h3></center>')
        
    def displayLogoutButton(self):
        print('<center>Click here to <a href="http://localhost/M3_DD/login.html">Login</a></center>')
    
logout_Object=logout();
logout_Object.displayLogoutButton()
