# Dependacies
from buildDatabase import create_database
from pandas import read_sql_query
import sqlite3


# ============================== Convicts Class =================================

# create a class named  "Dungeon"
class Dungeon:

    def __init__(self, name, size):
        self.name = name
        self.size = size

    # Method to return data from the database
    def iformation_dungeon(self):

        with create_database() as con:

            try:
                df = read_sql_query("""                 
                         SELECT * FROM Dungeon;    
                """, con)
                return df

            except sqlite3.OperationalError as e:
                print(e)
            except Exception as e:
                print(e)

    def add_new_dungeon(self):

        with create_database() as con:

            try:
                cur = con.cursor()
                last_id = cur.execute("SELECT id FROM Dungeon ORDER BY 1 DESC LIMIT 1;").fetchall()
                if last_id == []:
                    cur.execute(f"""  
                            INSERT INTO Dungeon('id', 'name', 'size') VALUES(1, ?, ?);  
                    """, (self.name, self.size))
                else:
                    cur.execute(f"""  
                            INSERT INTO Dungeon('id', 'name', 'size') VALUES({last_id[-1][0] + 1}, ?, ?);  
                    """, (self.name, self.size))

            except sqlite3.OperationalError as e:
                 print(e)
            except Exception as e:
                 print(e)

    # methods to get properties "Getters Methods"
    def get_name(self):
        return self.name

    def get_size(self):
        return self.size

    # methods to set new value for properties "Setters Methods"
    def set_name_dungeon(self, name):
        self.name = name

    def set_size_dungeon(self, size):
        self.size = size


# Object
# dungeon = Dungeon("Solorina", 5.6)
# dungeon.add_new_dungeon()
# print(dungeon.iformation_dungeon())

















