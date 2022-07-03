# Dependacies
from buildDatabase import create_database
from pandas import read_sql_query
import sqlite3


# ============================== Convicts Class =================================

# create a class named a "Convicts"
class Convicts:

    def __init__(self, from_date, to_date, person_id, offense_id):
        self.from_date = from_date
        self.to_date = to_date
        self.person_id = person_id
        self.offense_id = offense_id

    # Method to return information about the convict
    def information_of_convict(self):
        # To get all data about the convict
        # we will connect with our database
        # then we will make some query to get data of convict
        con = create_database()

        df = read_sql_query("SELECT * FROM Convicts;", con)
        return df  # dataframe

    # method to set data for convict
    def set_info_convect(self):
        # This method to add a person to the database
        # this will help us to give our database new data about persons in our prison
        # connect with the database
        # isnert data to the person table

        with create_database() as con:
            try:
                # insert data
                cur = con.cursor()
                # the last id
                last_id = cur.execute("SELECT id FROM Convicts ORDER BY 1 DESC LIMIT 1;").fetchall()
                last_person_id = cur.execute("SELECT person_id FROM Convicts ORDER BY 1 DESC LIMIT 1;").fetchall()
                last_offense_id = cur.execute("SELECT offense_id FROM Convicts ORDER BY 1 DESC LIMIT 1;").fetchall()

                if last_id == []:
                    cur.execute(f"""
                                INSERT INTO Convicts('id', 'from_date', 'to_date', 'person_id', 'offense_id')
                                 VALUES(1, ?, ?, ?, ?)
                        """, (self.from_date, self.to_date, self.person_id, self.offense_id))

                else:
                    cur.execute(f"""
                                INSERT INTO Convicts('id', 'from_date', 'to_date', 'person_id', 'offense_id')
                                 VALUES({last_id[-1][0] + 1}, ?, ?, ?, ?)
                        """, (self.from_date, self.to_date, self.person_id, self.offense_id))

            except sqlite3.OperationalError as e:
                print(e)
            except Exception as e:
                print(e)

    # Method to return name of prisoner based on offense
    def presoners_by_offense(self, offense_id):
        # this method return names of presoners
        # based on the offense they do
        # just name >> first and father and last names
        # name_offense >> name of the offense user entered

        with create_database() as con:
            try:
                df = read_sql_query(f"""
                            
                            WITH table1 as (
                                SELECT person_id FROM Convicts WHERE offense_id={offense_id}
                            ) SELECT (p.first_name || " " || p.father || " " || p.last_name) as names_of_presoners
                               FROM Person as p
                               JOIN table1 as t1
                               ON t1.person_id = p.id; 
                        """, con)
                return df

            except sqlite3.OperationalError as e:
                print(e)
            except Exception as e:
                print(e)

    # Method return presoners between two dates
    def presoners_between_dates(self, start_date, end_date):

        with create_database() as con:

            try:

                df = read_sql_query(f"""
                            SELECT * FROM Convicts WHERE from_date BETWEEN {start_date} and {end_date};
                        """, con)

                return df

            except sqlite3.OperationalError as e:
                print(e)
            except Exception as e:
                print(e)

    # methods to get properties "Getters Methods"
    def get_from_date(self):
        return self.from_date

    def get_to_date(self):
        return self.to_date

    def get_person_id(self):
        return self.person_id

    def get_offense_id(self):
        return self.offense_id

    # methods to set new value for properties "Setters Methods"
    def set_from_date(self, from_date):
        self.from_date = from_date

    def set_to_date(self, to_date):
        self.to_date = to_date

    def set_person_id(self, person_id):
        self.person_id = person_id

    def set_offense_id(self, offense_id):
        self.offense_id = offense_id


# Object
convict = Convicts('2-23-2005', '2-23-2007', 1, 1)
# convict.set_info_convect()
# print(convict.information_of_convict())
# print(convict.presoners_by_offense(1))
# print(convict.presoners_between_dates('1-12-2000', '10-12-2010'))
