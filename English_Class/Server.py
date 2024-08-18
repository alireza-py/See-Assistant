import mysql.connector

class Server:
    def __init__(self) -> None:
        self.recently_database_use = False
        self.all_databases = None
        self.all_tables = None
        self.my_cursor = None
        self.database = None
        self.out_data = None
        self.table = None
        self.spl = None

    def get_connection(self, ipaddress='127.0.0.1', usr='root', passwd='root23231'):
        self.spl = mysql.connector.connect(user = usr, password = passwd,
                                                        host = ipaddress)
        self.my_cursor = self.spl.cursor()
        return self.my_cursor

    def databases(self, database:str, table:str, size_table:int=6000):
        self.database = database.lower()
        self.table = table.lower()
        self.get_connection()
        if not self.recently_database_use == self.database:
            self.my_cursor.execute("SHOW DATABASES")
            self.all_databases = list(map(lambda x:x[0] ,self.my_cursor))
            
            if not self.database in self.all_databases:
                self.my_cursor.execute(f"CREATE DATABASE {self.database}")

            self.my_cursor.execute(f"USE {self.database};")
            self.my_cursor.execute("SHOW TABLES")
            self.all_tables = list(map(lambda x:x[0] ,self.my_cursor))

            if not self.table in self.all_tables:
                self.my_cursor.execute(f"CREATE TABLE {self.table}(Part_One VARCHAR({size_table}),Part_Two VARCHAR({size_table}) COLLATE utf8mb4_persian_ci);")

        self.my_cursor.execute(f"USE {self.database};")
        self.my_cursor.execute(f"SELECT * FROM {self.table};")
        self.out_data = []
        self.out_data = dict(self.my_cursor)
        self.recently_database_use = self.database
        self.spl.close()
        return self.out_data
    
    def add_in_database(self, data:list) -> bool:
        self.get_connection()
        if not self.database and not self.table:
            return False
        self.my_cursor.execute(f"USE {self.database};") 
        if data[0] in self.out_data.keys():
            list_per = []
            edit_string = self.out_data[data[0]][1:-1].replace("'", '')
            list_per.append(edit_string.split(','))
            print(list_per)
            if not data[1] in list_per:
                list_per.append(data[1])
                self.out_data[data[0]] = list_per
                print(list_per)
                self.my_cursor.execute(f'UPDATE {self.table} SET Part_Two = "{self.out_data[data[0]]}" WHERE Part_One = "{data[0]}"')
            self.spl.commit()
            self.spl.close()
            return True
        
        try:
            self.my_cursor.execute('INSERT INTO %s VALUES("%s" , "%s")' %(self.table , data[0], [data[1]]))
        except:
            return False
        self.spl.commit()
        self.spl.close()
        return True
    
