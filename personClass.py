# Dependacies
import sqlite3
from buildDatabase import create_database
from pandas import read_sql_query

# ============================== Person Class =================================

# create a class named a "Person"
class Person:

    """
        Person class:
            Attributes:
                    first_name,
                    father,
                    last_name,
                    gender,
                    birth_year,
                    address

            methods:
                 first_name,
                    father,
                    last_name,
                    gender,
                    birth_year,
                    address
        """

    # initialize the object
    def __init__(self, first_name, father, last_name, gender, birth_year, address):
        # instance Attributs
        self.first_name = first_name
        self.father = father
        self.last_name = last_name
        self.gender = gender
        self.birth_year = birth_year
        self.address = address

    # Method to return information about the prisoner
    def information_of_prisoner(self):
        # To get all data about the prisoner
        # we will connect with our database
        # then we will make some query to get data of prisoner
        con = create_database()

        df = read_sql_query("SELECT * FROM Person;", con)
        return df  # dataframe

    # method to set data for person
    def set_info_person(self):
        # This method to add a person to the database
        # this will help us to give our database new data about persons in our prison
        # connect with the database
        # isnert data to the person table

        with create_database() as con:
            try:
                # insert data
                cur = con.cursor()
                # the last id
                last_id = cur.execute("SELECT id FROM Person ORDER BY 1 DESC LIMIT 1;").fetchall()
                if last_id == []:
                    cur.execute(f"""
                                INSERT INTO Person('id', 'first_name', 'father', 'last_name', 'gender', 'birth_year', 'address')
                                 VALUES(1, ?, ?, ?, ?, ?, ?)
                        """, (self.first_name, self.father, self.last_name, self.gender, self.birth_year,
                                self.address))

                else:
                    cur.execute(f"""
                                INSERT INTO Person('id', 'first_name', 'father', 'last_name', 'gender', 'birth_year', 'address')
                                 VALUES({last_id[-1][0] + 1}, ?, ?, ?, ?, ?, ?)
                        """, (self.first_name, self.father, self.last_name, self.gender, self.birth_year,
                                self.address))
            except sqlite3.OperationalError as e:
                print(e)
            except Exception as e:
                print(e)

    # methods to get properties "Getters Methods"
    def get_first_name(self):
        return self.first_name

    def get_father(self):
        return self.father

    def get_last_name(self):
        return self.last_name

    def get_gender(self):
        return self.gender

    def get_birth_year(self):
        return self.birth_year

    def get_address(self):
        return self.address

    # methods to set new value for properties "Setters Methods"
    def set_first_name(self, fname):
        self.first_name = fname

    def set_father(self, father_name):
        self.father = father_name

    def set_last_name(self, lname):
        self.last_name = lname

    def set_gender(self, gender):
        self.gender = gender

    def set_birth_year(self, byear):
        self.birth_year = byear

    def set_address(self, address):
        self.address = address

# Object
# person = Person("Mosa", "Samer", "Momani", "Male", '2-20-2000', 'Sweeden')  # put the data of new prisoner
# person.set_info_person()  # call it ti set new data
# print(person.information_of_prisoner())  # see the data of the prisoner table
