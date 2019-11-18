#!"C:\\Python34\\python.exe"
import cgi, cgitb
import mysql.connector as mdb
from login import *
import logging

class Transfer_Money_Final():

    def readFormContent(self):
        frmObj=cgi.FieldStorage()
        Acc_No=frmObj.getvalue("Acc_No")
        Payee_Acc_No=frmObj.getvalue("payee_acc_no")
        Transfer_Money=frmObj.getvalue("transfer_money")
        UserName=frmObj.getvalue("UserName")
        return Acc_No,Payee_Acc_No,Transfer_Money,UserName

    def getCurrentBalance(self,Rows):
        self.Rows=Rows
        Current_Balance=Rows[0][6]
        return Current_Balance
    
    def getPayeeCurrentBalance(self,cursor,Payee_Acc_No):
        self.Payee_Acc_No=Payee_Acc_No
        self.cursor=cursor
        payee_current_balance_sql="SELECT * FROM bank_details WHERE Acc_No=('%d')" % (Payee_Acc_No)
        cursor.execute(payee_current_balance_sql)
        Rows=cursor.fetchall()
        return Rows[0][6]
        

    def transferMoney(self,Payer_Current_Balance,Payee_Current_Balance,Transfer_Money,Acc_No,Payee_Acc_No):
        self.Payer_Current_Balance=Payer_Current_Balance
        self.Payee_Current_Balance=Payee_Current_Balance
        self.Transfer_Money=Transfer_Money
        self.Acc_No=Acc_No
        self.Payee_Acc_No=Payee_Acc_No
        Payee_New_Balance=int(Payee_Current_Balance) + int(Transfer_Money)
        Payer_New_Balance=int(Payer_Current_Balance)-int(Transfer_Money)
        update_payee_acc_sql="UPDATE bank_details SET Balance=('%d') WHERE Acc_No=('%d')" %(Payee_New_Balance,Payee_Acc_No)
        update_payer_acc_sql="UPDATE bank_details SET Balance=('%d') WHERE Acc_No=('%d')" %(Payer_New_Balance,Acc_No)

        cursor.execute(update_payer_acc_sql)
        cursor.execute(update_payee_acc_sql)

        payer_final_balance_sql="SELECT * FROM bank_details WHERE Acc_No=('%d')" % (Acc_No)
        payee_final_balance_sql="SELECT * FROM bank_details WHERE Acc_No=('%d')" % (Payee_Acc_No)

        cursor.execute(payer_final_balance_sql)
        Rows=cursor.fetchall()
        Payer_Final_Balance=Rows[0][6]

        cursor.execute(payee_final_balance_sql)
        Rows=cursor.fetchall()
        Payee_Final_Balance=Rows[0][6]

        return Payer_Final_Balance,Payee_Final_Balance


logging.basicConfig(filename='my_account_app.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(filename)s:%(message)s')
transfer_money_final_object=Transfer_Money_Final()
FormOutput=transfer_money_final_object.readFormContent()
Acc_No=int(FormOutput[0])
Payee_Acc_No=int(FormOutput[1])
Transfer_Money=int(FormOutput[2])
UserName=str(FormOutput[3])

cursorDB=Login().dbConnection()
cursor=cursorDB[0]
db=cursorDB[1]
Rows=Login().executeSelectQuery(cursor,UserName)
Current_Balance=transfer_money_final_object.getCurrentBalance(Rows)
Payee_Current_Balance=transfer_money_final_object.getPayeeCurrentBalance(cursor,Payee_Acc_No)
Transfer_Money_Output=transfer_money_final_object.transferMoney(Current_Balance,Payee_Current_Balance,Transfer_Money,Acc_No,Payee_Acc_No)
Payer_Final_Balance=Transfer_Money_Output[0]
Payee_Final_Balance=Transfer_Money_Output[1]

print('<br><br><br><br><br>')
print('<center><h2>Transfer Successful!</h2></center>')
print('<center>INR <b>{0}</b> has been transferred to Account Number: <b>{1}</b></center>'.format(Transfer_Money,Payee_Acc_No))
print('<br><center>New Account Balance : <b>INR {0}</b></center>'.format(Payer_Final_Balance))
logging.info('Money Transfer Successful ! Payer Acc No: {0}  Payee Acc No: {1}'.format(Acc_No,Payee_Acc_No))

Login().closeDBconnection(db)

