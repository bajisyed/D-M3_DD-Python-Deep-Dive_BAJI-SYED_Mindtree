#!"C:\\Python34\\python.exe"
import cgi,cgitb
import mysql.connector as mdb
import datetime
import logging

class  Add_Payee_Initial():

    def readFormContent(self):
        #Creat the form object
        frmObj=cgi.FieldStorage()
        Acc_No=frmObj.getvalue("Acc_No")
        return Acc_No

    def displayAddPayeeForm(self,Acc_No,Current_Date):
        print("Content-type: text/html")
        print("""
        <TITLE>ADD PAYEE</TITLE>
        """)
        self.Acc_No=Acc_No
        self.Current_Date=Current_Date
        logging.info('Add Payee initiated ! Account Number: {}'.format(Acc_No))
        print('<br><br><br><br><br>')
        print('<center><form action="add_payee_final.py" method="post"><br>')
        print('Payee Account Number :<input type="text" name="payee_acc_no"><br><br>')
        print('Payee Name : <input type="text" name="payee_name"><br><br>')
        print('Payee Bank Name :<input type="text" name="payee_bank_name"><br><br>')
        print('<input type="hidden" id="Current_Date" name="Current_Date" value="%s">' % (Current_Date))
        print('<br><input type="hidden" id="Acc_No" name="Acc_No" value="%d">' %(Acc_No))
        print('<br><input type="submit" value="Add Payee">')
        print('</form></center>')

logging.basicConfig(filename='my_account_app.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(filename)s:%(message)s')
Add_Payee_Initial_Object=Add_Payee_Initial()
Acc_No=int(Add_Payee_Initial_Object.readFormContent())
CurrentDT=datetime.datetime.now()
Current_Date=str(CurrentDT)
Add_Payee_Initial_Object.displayAddPayeeForm(Acc_No,Current_Date)

