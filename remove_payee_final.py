#!"C:\\Python34\\python.exe"
import cgi, cgitb
import mysql.connector as mdb
from login import *
import logging

class Remove_Payee_Final():
    
    def readFormContent(self):
        frmObj=cgi.FieldStorage()
        Acc_No=frmObj.getvalue("Acc_No")
        Payee_Acc_No=frmObj.getvalue("payee_acc_no")
        
        return Acc_No,Payee_Acc_No

    def removePayee(self,cursor,Acc_No,Payee_Acc_No):
        self.cursor=cursor
        self.Acc_No=Acc_No
        self.Payee_Acc_No=Payee_Acc_No
        remove_payee_sql="DELETE FROM payee_details WHERE Acc_No=(%d) AND Payee_Acc_No=(%d)" %(Acc_No,Payee_Acc_No)
        cursor.execute(remove_payee_sql)
        return True

logging.basicConfig(filename='my_account_app.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(filename)s:%(message)s')
Remove_Payee_Final_Object=Remove_Payee_Final()
FormOutput=Remove_Payee_Final_Object.readFormContent()
Acc_No=int(FormOutput[0])
Payee_Acc_No=int(FormOutput[1])

cursorDB=Login().dbConnection()
cursor=cursorDB[0]
db=cursorDB[1]

Remove_Payee_Result=Remove_Payee_Final_Object.removePayee(cursor,Acc_No,Payee_Acc_No)
if(Remove_Payee_Result):
    logging.info('Payee Removal Successful! Payer Acc No: {0} and Payee Acc No: {1}'.format(Acc_No,Payee_Acc_No))
    print('<br><br><br><br><br><br>')
    print('<center><h2>Account Number {0} has been removed from your payee list !</h2></center>'.format(Payee_Acc_No))
    
db.close()
