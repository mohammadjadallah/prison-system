# Dependacies
from buildDatabase import create_database
from pandas import read_sql_query
import sqlite3


# ============================== DungeonMoves Class =================================

# create a class named  "DungeonMoves"
class DungeonMoves:

    def __init__(self, from_date, dungeon_id, person_id):
        self.dungeon_id = dungeon_id
        self.person_id = person_id
        self.from_date = from_date

    # Method to return data from the database
    def iformation_dungeon_moves(self):

        with create_database() as con:

            try:
                df = read_sql_query("""                 
                         SELECT * FROM DungeonMoves;    
                """, con)
                return df

            except sqlite3.OperationalError as e:
                print(e)
            except Exception as e:
                print(e)

    def add_new_dungeon_moves(self):

        with create_database() as con:

            try:
                cur = con.cursor()
                last_id = cur.execute("SELECT id FROM DungeonMoves ORDER BY 1 DESC LIMIT 1;").fetchall()

                if last_id == []:
                    cur.execute(f"""  
                                INSERT INTO DungeonMoves('id', 'from_date', 'dungeon_id', 'person_id') VALUES(1, ?, ?, ?);  
                        """, (self.from_date, self.dungeon_id, self.person_id))
                else:
                    cur.execute(f"""  
                                INSERT INTO DungeonMoves('id', 'from_date', 'dungeon_id', 'person_id') VALUES({last_id[-1][0] + 1}, ?, ?, ?);  
                        """, (self.from_date, self.dungeon_id, self.person_id))

            except sqlite3.OperationalError as e:
                print(e)
            except Exception as e:
                print(e)

    def info_persons_inside_dungeons(self, person_id):

        with create_database() as con:

            try:
                df = read_sql_query(f"""                 
                         SELECT * FROM DungeonMoves WHERE person_id = {person_id};    
                """, con)
                return df

            except sqlite3.OperationalError as e:
                print(e)
            except Exception as e:
                print(e)

    # methods to get properties "Getters Methods"
    def get_from_date(self):
        return self.from_date

    def get_person_id(self):
        return self.person_id

    def get_dungeon_id(self):
        return self.dungeon_id

    # methods to set new value for properties "Setters Methods"
    def set_from_date(self, from_date):
        self.from_date = from_date

    def set_person_id(self, person_id):
        self.person_id = person_id

    def set_dungeon_id(self, dungeon_id):
        self.dungeon_id = dungeon_id


# Object
# dungeon = DungeonMoves("5-2-1999", 1, 1)
# dungeon.add_new_dungeon_moves()
# print(dungeon.iformation_dungeon_moves())
# print(dungeon.info_persons_inside_dungeons(1))

