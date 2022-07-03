# Dependacies
from buildDatabase import create_database
from pandas import read_sql_query
import sqlite3


# ============================== Visitings Class =================================

# create a class named  "Visitings"
class Visitings:

    def __init__(self, date_visited, person_id, visitor_name, mountin_minutes):
        self.date_visited = date_visited
        self.person_id = person_id
        self.visitor_name = visitor_name
        self.mountin_minutes = mountin_minutes

    # Method to return data from the database
    def iformation_visitings(self):

        with create_database() as con:

            try:
                df = read_sql_query("""                 
                         SELECT * FROM Visitings;    
                """, con)
                return df

            except sqlite3.OperationalError as e:
                print(e)
            except Exception as e:
                print(e)

    # Method to add data to visitings table in database
    def add_new_visiting(self):

        with create_database() as con:

            try:
                cur = con.cursor()
                last_id = cur.execute("SELECT id FROM Visitings ORDER BY 1 DESC LIMIT 1;").fetchall()

                if last_id == []:
                    cur.execute(f"""  
                                INSERT INTO Visitings('id', 'date_visited', 'person_id', 'visitor_name', 'mountin_minutes') VALUES(1, ?, ?, ?, ?);  
                        """, (self.date_visited, self.person_id, self.visitor_name, self.mountin_minutes))
                else:
                    cur.execute(f"""  
                                INSERT INTO Visitings('id', 'date_visited', 'person_id', 'visitor_name', 'mountin_minutes') VALUES({last_id[-1][0] + 1}, ?, ?, ?, ?);  
                        """, (self.date_visited, self.person_id, self.visitor_name, self.mountin_minutes))

            except sqlite3.OperationalError as e:
                print(e)
            except Exception as e:
                print(e)

    def info_visitings_date(self, first_date, last_date):

        with create_database() as con:

            try:
                df = read_sql_query(f"""                 
                         SELECT * FROM Visitings WHERE (date_visited BETWEEN '{first_date}' AND '{last_date}');    
                """, con)
                return df

            except sqlite3.OperationalError as e:
                print(e)
            except Exception as e:
                print(e)

    # methods to get properties "Getters Methods"
    # date_visited, person_id, visitor_name, mountin_minutes
    def get_date_visited(self):
        return self.date_visited

    def get_person_id(self):
        return self.person_id

    def get_visitor_name(self):
        return self.visitor_name

    def get_mountin_minutes(self):
        return self.mountin_minutes

    # methods to set new value for properties "Setters Methods"
    def set_date_visited(self, date_visited):
        self.date_visited = date_visited

    def set_person_id(self, person_id):
        self.person_id = person_id

    def set_visitor_name(self, visitor_name):
        self.visitor_name = visitor_name

    def set_mountin_minutes(self, mountin_minutes):
        self.mountin_minutes = mountin_minutes


# Object
# visiting = Visitings(date_visited="2002-5-20", person_id=1, visitor_name='Naser Salem Hadi', mountin_minutes=5)
# visiting = Visitings(date_visited="2013-3-28", person_id=1, visitor_name='Abdullah Salem Hadi', mountin_minutes=10)
# visiting = Visitings(date_visited="2014-6-28", person_id=1, visitor_name='Ayah Waleed Rami', mountin_minutes=15)
# visiting = Visitings(date_visited="2020-4-15", person_id=1, visitor_name='Sars Nadeem Rawaad', mountin_minutes=10)
# visiting = Visitings(date_visited="2020-6-20", person_id=1, visitor_name='Hadi Khaled deeb', mountin_minutes=8)
# visiting.add_new_visiting()
# print(visiting.iformation_visitings())
# print(visiting.info_visitings_date("2002-5-20", "2020-4-15"))

# I made rename for the column mountin_minutes the query below
# ALTER TABLE Visitings
# RENAME COLUMN mountin_muinutes to mountin_minutes;
