# Dependacies
from buildDatabase import create_database
from pandas import read_sql_query
import sqlite3


# ============================== Convicts Class =================================

# create a class named a "offense"
class Offense:
    """
        one attribute: name
        method to return data from database: information_of_offense
        mathod add offense: add_new_offense
    """

    def __init__(self, name):
        self.name = name

    def information_of_offense(self):

        with create_database() as con:
            try:

                df = read_sql_query("""          
                                SELECT * FROM Offense; 
                        """, con)

                return df

            except sqlite3.OperationalError as e:
                print(e)
            except Exception as e:
                print(e)

    def add_new_offense(self):
        with create_database() as con:
            try:
                cur = con.cursor()
                last_id = cur.execute("SELECT id FROM Offense ORDER BY 1 DESC LIMIT 1;").fetchall()
                if last_id == []:
                    print(True)
                    cur.execute(F"""          
                                      INSERT INTO Offense('id', 'name') VALUES(1, ?); 
                                """, (self.name,))
                else:
                    cur.execute(F"""          
                                    INSERT INTO Offense('id', 'name') VALUES({last_id[-1][0] + 1}, ?); 
                            """, (self.name,))

            except sqlite3.OperationalError as e:
                print(e)
            except Exception as e:
                print(e)

    # methods to get properties "Getters Methods"
    def get_name(self):
        return self.name

    # methods to set new value for properties "Setters Methods"
    def set_name_offense(self, name_offense):
        self.name = name_offense


# Object
offense = Offense('Nour')
# offense.add_new_offense()
# print(offense.information_of_offense())


