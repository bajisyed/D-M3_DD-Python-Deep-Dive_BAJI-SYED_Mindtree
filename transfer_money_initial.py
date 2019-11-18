#!"C:\\Python34\\python.exe"
import cgi, cgitb
import mysql.connector as mdb
from login import *
import logging

class Transfer_Money_Initial():
    
    def readFormContent(self):
        frmObj=cgi.FieldStorage()
        UserName=frmObj.getvalue("UserName")
        return UserName

    def displayTransferForm(self,Rows):
        self.Rows=Rows
        Acc_No=int(Rows[0][0])
        UserName=str(Rows[0][4])
        logging.info('Transfer Money initiated! UserName: {}'.format(UserName))
        print('<br><br><br><br><br>')
        print('<center><form action="transfer_money_final.py" method="post">')
        print('Payer Account Number : {0}'.format(Rows[0][0]))
        print('<br><br>Payee Account Number :<input type="text" name="payee_acc_no">')
        print('<br><br>Transfer Amount :<input type="text" name="transfer_money"></br><br>')
        print('<br><input type="hidden" id="Acc_No" name="Acc_No" value="%d">' %(Acc_No))
        print('<br><input type="hidden" id="UserName" name="UserName" value="%s">' %(UserName))
        print('<input type="submit" value="Transfer Money">')
        print('</form></center>')
        

print ("Content-Type: text/html")
print("""
<TITLE>ACCOUNT DETAILS</TITLE>
""")

logging.basicConfig(filename='my_account_app.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(filename)s:%(message)s')
transfer_money_Initial_object=Transfer_Money_Initial()
cursorDB=Login().dbConnection()
cursor=cursorDB[0]
db=cursorDB[1]
UserName=transfer_money_Initial_object.readFormContent()
Rows=Login().executeSelectQuery(cursor,UserName)
transfer_money_Initial_object.displayTransferForm(Rows)

Login().closeDBconnection(db)

    
