#!"C:\\Python34\\python.exe"
import cgi, cgitb
import mysql.connector as mdb
from login import *

class Remove_Payee_Initial():

    def readFormContent(self):
        frmObj=cgi.FieldStorage()
        Acc_No=frmObj.getvalue("Acc_No")
        return Acc_No
    
    def displayRemovePayeeForm(self,Acc_No):

        self.Acc_No=Acc_No
        logging.info('Remove Payee initiated ! Payer Acc_No: {}'.format(Acc_No))
        print('<br><br><br><br><br>')
        print('<center><form action="remove_payee_final.py" method="post">')
        print('Payee Account Number:<input type="text" name="payee_acc_no">')
        print('</br><br><br><input type="hidden" id="Acc_No" name="Acc_No" value="%s">' %(Acc_No))
        print('<input type="submit" value="Remove Payee">')
        input('</form></center>')

print ("Content-Type: text/html")
print("""
<TITLE>REMOVE PAYEE</TITLE>
""")
logging.basicConfig(filename='my_account_app.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(filename)s:%(message)s')
Remove_Payee_Initial_Object=Remove_Payee_Initial()
Acc_No=Remove_Payee_Initial_Object.readFormContent()
Remove_Payee_Initial_Object.displayRemovePayeeForm(Acc_No)
        
