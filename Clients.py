import mysql.connector

conn = mysql.connector.Connect(
    host = "localhost",
    user = "root",
    password = "620203",
    database = "library"
)

cursor = conn.cursor()
@staticmethod
def doesIdExist(id):
    cursor.execute(
        '''select Id from clients where Id = %s''',(id,)
    )
    result = cursor.fetchone()
    return result is not None

def check_data_exists():
    cursor.execute('''select count(*) from clients''')
    results = cursor.fetchone()
    return results[0]>0




class client:
    def __init__(self,ID,Name,Email,Phone):
        self.id = ID
        self.name = Name
        self.email = Email
        self.phone = Phone
        

    
    def Add_client(self):
        if doesIdExist(self.id):
           print(f"The ID {self.id} already exists. Please choose another ID.")
        else:
            try:
                cursor.execute(
                    '''insert into clients(Id,Name,Email,Phone)values(%s,%s,%s,%s)''',
                    (self.id,self.name,self.email,self.phone)
                    )
                conn.commit()
                print("The client has been added successfully.")
            except Exception as e:
                print(f"Error : {e}")

    @staticmethod
    def remove_client(ID):
        if doesIdExist(ID):
            try:
                cursor.execute('''delete from clients where Id = %s ''',(ID,))
                conn.commit()
                print(f"The client with ID {ID} has been removed successfully.")
            except Exception as e:
                print(f"Error : {e}")
        else:
            print(f"The client with ID {ID} does not exist in the database.")


    
    def update_client_information(self):

        if doesIdExist(self.id):
            cursor.execute('''update clients set Name = %s,Email = %s,Phone = %s where Id = %s''',
            (self.name,self.email,self.phone,self.id))
            conn.commit()
            print(f"The client with ID {self.id} has been successfully updated.")
        else:
            print(f"The client with ID {self.id} does not exist in the database.")




            
       




    @staticmethod
    def close_connection():

        try:

           conn.close()
           cursor.close()
           print("Connection closed successfully.")
        except  Exception as e:
           print(f"Error : {e}")



    @staticmethod
    def Display_clients():
       if check_data_exists()>0: 
          cursor.execute('''select * from clients''')
          clients = cursor.fetchall()

          if clients:
           print("Books in Database are : ")
           print("[ ID  |  Name  |   Email    |    Phone  ]\n")  
           for client in clients:
            print([client])
       else:
          print("No data in the database")

    

     




