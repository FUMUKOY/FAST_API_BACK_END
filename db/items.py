import os
from dotenv import load_dotenv
import pyodbc

#Load the env file
load_dotenv()

config = {
    "db_host": os.getenv("DB_HOST"),
    "db_user": os.getenv("DB_USER"),
    "db_password": os.getenv("DB_PASSWORD"),
    "db_name": os.getenv("DB_NAME")
}

connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={config["db_host"]};DATABASE={config["db_name"]};UID={config["db_user"]};PWD={config["db_password"]}'
sql_server_connection = pyodbc.connect(connection_string)

query = """

    SELECT * FROM [STT].[dbo].[Invoice] 
    WHERE InvoiceID = ?                         

"""             #i need to do research here, understand the mechanism, how it works.
Data = None
ItemID = 3    #i need to do research here, understand the mechanism, how it works.

cursor = sql_server_connection.cursor()
cursor.execute(query, (ItemID,))
Data = cursor.fetchall()

def read_db_item(Data):

    if not Data:
        raise ValueError(f"Item with id {ItemID} not found.")

    for row in Data:
            print(f"InvoiceID: {row[0]}, "
                f"CustomerID: {row[1]}, "
                f"InvoiceNumber: {row[2]}, "
                f"CustomerID: {row[3]}, "
                f"CustAddrID: {row[4]}, "
                f"CreateUserID: {row[5]}, "
                f"AuthUserID: {row[6]}, "
                f"CustomerOrderNumber: {row[7]}, "
                f"OrderContactName: {row[8]}, "
                f"IncVatTotal: {row[9]}, "
                f"VatTotal: {row[11]}, "
                f"DueDate: {row[12]}, "
                f"Terms: {row[13]}, "
                f"Note: {row[14]}, "
                f"Status: {row[15]}, "
                f"UniqueID: {row[16]}, "
                f"ExtInvoiceNumber: {row[17]}, "
                f"ExtInvoiceNumber: {row[18]}, "
                f"ExtInvoiceNumber: {row[19]}, "
                f"ExtInvoiceNumber: {row[20]}, "
                f"ExtInvoiceNumber: {row[21]}, "
                f"ExtInvoiceNumber: {row[22]}, "
                f"ExtInvoiceNumber: {row[23]}, "
                f"ExtInvoiceNumber: {row[24]}, "
                f"ExtInvoiceNumber: {row[25]}, "
                f"ExtInvoiceNumber: {row[26]}, "
                f"ExtInvoiceNumber: {row[27]},")
            
            return Data

           
# Check if result is empty
  
result =read_db_item(Data)










