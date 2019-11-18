#!"C:\\Python34\\python.exe"
import cgi,cgitb
import mysql.connector as mdb
import logging
from login import *

class Add_Payee_Final():

    def readFormContent(self):
        frmObj=cgi.FieldStorage()

        Acc_No=int(frmObj.getvalue("Acc_No"))
        Payee_Acc_No=int(frmObj.getvalue("payee_acc_no"))
        Payee_Name=str(frmObj.getvalue("payee_name"))
        Payee_Bank_Name=str(frmObj.getvalue("payee_bank_name"))
        Current_Date=str(frmObj.getvalue("Current_Date"))
        return Acc_No,Payee_Acc_No,Payee_Name,Payee_Bank_Name,Current_Date
    

    def addPayee(self,cursor,Acc_No,Payee_Acc_No,Payee_Name,Payee_Bank_Name,Current_Date):
        self.cursor=cursor
        self.Acc_No=Acc_No
        self.Payee_Acc_No=Payee_Acc_No
        self.Payee_Name=Payee_Name
        self.Payee_Bank_Name=Payee_Bank_Name
        self.Current_Date=Current_Date
        add_payee_sql="INSERT INTO payee_details VALUES(null,'%d','%d','%s','%s','%s')" % \
                       (Acc_No,Payee_Acc_No,Payee_Name,Payee_Bank_Name,Current_Date)
        cursor.execute(add_payee_sql)
        return True
        
    
print("Content-type: text/html")
print("""
     <TITLE>ADD PAYEE2</TITLE>
     """)

logging.basicConfig(filename='my_account_app.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(filename)s:%(message)s')
Add_Payee_Final_Object=Add_Payee_Final()
FormOutput=Add_Payee_Final_Object.readFormContent()
Acc_No=int(FormOutput[0])
Payee_Acc_No=int(FormOutput[1])
Payee_Name=FormOutput[2]
Payee_Bank_Name=FormOutput[3]
Current_Date=FormOutput[4]    #'2018-06-17 02:45:43.413234'
Current_Date=Current_Date[:19] #'2018-06-17 02:45:43'
cursorDB=Login().dbConnection()
cursor=cursorDB[0]
db=cursorDB[1]
addPayeeResult=Add_Payee_Final_Object.addPayee(cursor,Acc_No,Payee_Acc_No,Payee_Name,Payee_Bank_Name,Current_Date)
if (addPayeeResult):
    logging.info('Payee Added! Payer Acc No: {0} Payee Acc No: {1}'.format(Acc_No,Payee_Acc_No))
    print('<br><br><br><br><br>')
    print('<center><h2>Payee Added Successfully</h2></center>')

Login().closeDBconnection(db)
