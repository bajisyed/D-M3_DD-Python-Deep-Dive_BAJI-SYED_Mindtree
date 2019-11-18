#!"C:\\Python34\\python.exe"
import cgi, cgitb
import mysql.connector as mdb
import login
from login import *
import logging

class Deposit_Money_Initial():
    def readFormContent(self):
        frmObj=cgi.FieldStorage()
        UserName=frmObj.getvalue("UserName")
        return UserName
    def displayDepositForm(self,Rows):
        self.Rows=Rows
        Account_Name=str(Rows[0][1])+" "+str(Rows[0][2])
        Acc_No=int(Rows[0][0])
        UserName=str(Rows[0][4])
        logging.info('Money Deposit initiated!  UserName: {0}'.format(UserName))
        print('<center><form action="deposit_money_final.py" method="post">')
        print('<br><br><br><br><br>')
        print('Account Number : <b>{0}</b>'.format(Rows[0][0]))
        print('<br><br>Name: <b>{0}</b>'.format(Account_Name))
        print('<br><input type="hidden" id="UserName" name="UserName" value="%s">'% (UserName))
        print('<br><input type="hidden" id="Acc_No" name="Acc_No" value="%s">' % (Acc_No))
        print('<br><br>Deposit Amount :<input type="text" name="Deposit_Money">')
        print('<br><br><input type="submit" value="Deposit">')
        print('</form></center>')

logging.basicConfig(filename='my_account_app.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(filename)s:%(message)s')
Money_Deposit_Initial_Obj=Deposit_Money_Initial()
cursorDB=Login().dbConnection()
cursor=cursorDB[0]
db=cursorDB[1]
UserName=Money_Deposit_Initial_Obj.readFormContent()
Rows=Login().executeSelectQuery(cursor,UserName)
Money_Deposit_Initial_Obj.displayDepositForm(Rows)
Login().closeDBconnection(db)
