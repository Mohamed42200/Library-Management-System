import  mysql.connector
conn = mysql.connector.connect(
    host="localhost",       
    user="root",            
    password="620203",  
    database="library"   
)

cursor = conn.cursor()


def check_id_exists(id):
    cursor.execute('''select ID from Books where ID = %s''',(id,))
    result = cursor.fetchone()
    return result is not None

def check_data_exists():
   cursor.execute('''select count(*) from Books''')
   result = cursor.fetchone()
   return result[0]>0
        

class Book:
    def __init__(self,ID,Title ,Author,Category,Pub_year,Copies_available):
        self.id = ID
        self.title = Title
        self.author = Author
        self.category = Category
        self.pub_year= Pub_year
        self.copies_available= Copies_available
    


    def Add_Book(self):
        if check_id_exists(self.id):
            print(f"Error: Book with ID {self.id} already exists.")
        else:
            try: 

              cursor.execute('''INSERT INTO Books(ID,Title,Author,Category,Pub_year,Copies_available)values(%s,%s,%s,%s,%s,%s)'''
                             ,(self.id,self.title, self.author,self.category , self.pub_year, self.copies_available) )
              conn.commit()
              print("The book has been added")
            
            except Exception as e:
             print(f"Errorr : {e}")
             conn.rollback()

       
            


        
   
    def Update_book_information(self):
        if check_id_exists(self.id):
            
           try:
            cursor.execute(

            '''UPDATE books set Title = %s ,Author=%s,Category = %s,Pub_year = %s,Copies_available = %s where ID = %s'''
            , (self.title,self.author,self.category,self.pub_year, self.copies_available,self.id) )

            conn.commit()
            print("The book has been updated successfully.")

           except Exception as e:
              print(f"Error :{e}")
              conn.rollback()
        else:
            print(f"The ID {self.id} does not exist in the database.")
           

        
            


    @staticmethod
    def Delete_a_book(ID):
        if check_id_exists(ID):
           try:
            cursor.execute(
                '''delete from books where ID = %s 
                '''
                ,(ID,)
            )
            conn.commit()
            print("The book has been deleted")
           except Exception as e:
            print(f"Error : {e}")
            conn.rollback() 
        else:
          print(f"The ID {ID} does not exist in the database.")



    @staticmethod
    def close_connection():
        try:
            cursor.close()
            conn.close()
            print("Connection closed successfully.")

        except Exception as e:
            print(f"Error closing connection: {e}")


    @staticmethod
    def Display_Books():
       if check_data_exists()>0: 
          cursor.execute('''select * from Books''')
          Books = cursor.fetchall()

          if Books:
           print("Books in Database are : ")
           print("[ ID  |  Title  |   Author    |    Category  |  Pub_year  |  Copies_available ]\n")  
           for book in Books:
            print([book])
       else:
          print("No data in the database")

    

     
          

   
         
    
       
       

    




