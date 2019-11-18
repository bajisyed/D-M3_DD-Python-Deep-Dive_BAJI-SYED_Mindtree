#!"C:\\Python34\\python.exe"
import cgi, cgitb
import mysql.connector as mdb
from login import *
import logging

class Deposit_Money_Final():
    def readFormContent(self):
        frmObj=cgi.FieldStorage()
        Deposit_Money=int(frmObj.getvalue("Deposit_Money"))
        Acc_No=frmObj.getvalue("Acc_No")
        UserName=frmObj.getvalue("UserName")
        return Deposit_Money,Acc_No,UserName

    def getCurrentBalance(self,Rows):
        self.Rows=Rows
        Current_Balance=Rows[0][6]
        return Current_Balance
        
    def depositMoney(self,cursor,Current_Balance,Deposit_Amount,Acc_No):
        self.cursor=cursor
        self.Current_Balance=Current_Balance
        self.Deposit_Amount=Deposit_Amount
        self.Acc_No=Acc_No
        Updated_Balance=int(Current_Balance)+int(Deposit_Amount)
        deposit_money_sql="UPDATE bank_details SET Balance=('%s') WHERE Acc_No=('%d')" % (Updated_Balance,Acc_No)
        cursor.execute(deposit_money_sql)
        return True
        

    def getFinalBalance(self,cursor,Acc_No):
        self.cursor=cursor
        self.Acc_No=Acc_No
        final_balance_sql="SELECT Balance FROM bank_details WHERE Acc_No=('%d')" % (Acc_No)
        cursor.execute(final_balance_sql)
        Rows=cursor.fetchall()
        Final_Balance=Rows[0][0]
        return Final_Balance


logging.basicConfig(filename='my_account_app.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(filename)s:%(message)s')
Money_Deposit_Final_Obj=Deposit_Money_Final()
FormOutput=Money_Deposit_Final_Obj.readFormContent()
Deposit_Money=FormOutput[0]
Acc_No=int(FormOutput[1])
UserName=FormOutput[2]
cursorDB=Login().dbConnection()
cursor=cursorDB[0]
db=cursorDB[1]
Rows=Login().executeSelectQuery(cursor,UserName)
Current_Balance=Money_Deposit_Final_Obj.getCurrentBalance(Rows)
Deposit_Money_Status=Money_Deposit_Final_Obj.depositMoney(cursor,Current_Balance,Deposit_Money,Acc_No)
if (Deposit_Money_Status):
    print('<br><br><br><br><br>')
    print("<center><h3>INR&emsp;{0} Deposited to Account Number :{1} Successfully</h3></center>".format(Deposit_Money,Acc_No))
    Final_Balance=str(Money_Deposit_Final_Obj.getFinalBalance(cursor,Acc_No))
    print("<center>Final Balance :<b>{0}</b></center>".format(Final_Balance))
    logging.info('Money Deposit Successful! UserName: {0} Deposit Amount: {1}'.format(UserName,Deposit_Money))

Login().closeDBconnection(db)
