import datetime
import mysql.connector

conn = mysql.connector.Connect(
    host = "localhost",
    user = "root",
    password = "620203",
    database = "library"
    ) 

cursor = conn.cursor()


class Loans:
    @staticmethod
    def borrow_book(ClientID,BookID):
        loan_date = datetime.date.today()
        return_date = loan_date + datetime.timedelta(days=7)
        try:
            cursor.execute('''select title from Books where id = %s''',
                           (BookID,))
            book = cursor.fetchone()
            if book:
                cursor.execute('''insert into loans(ClientID,BookID,LoanDate,ReturnDate,status) values(%s,%s,%s,%s,%s)''',
                               (ClientID,BookID,loan_date,return_date,"On borrowed"))
               
                print(f"The book has been successfully borrowed. Expected return date: {return_date}")
            else:
                print("Sorry, the book is currently unavailable.")

            conn.commit()
            
            
            
        except Exception as e:
            print(f"Error : {e}")



    @staticmethod
    def close_connection():
        try:
            cursor.close()
            conn.close()
            print("Connection closed successfully.")

        except Exception as e:
            print(f"Error closing connection: {e}")

        
        