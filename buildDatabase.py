import sqlite3


def create_database(name_db="presonDatabase.sqlite"):
    """
    Create the Database

    Database built using: sqlite3

    Name of the Database: presonDatabase.sqlite

    tables:
            1. Person
            2. Convicts
            3. Offense
            4. Visitings
            5. DungeonMoves
            6. Dungeon
    """

    # connect with the database
    try:
        con = sqlite3.connect(f"file:{name_db}?mode=rw", uri=True)  # uri >>  database is interpreted as a URI
    except sqlite3.OperationalError:
        con = sqlite3.connect(name_db)
        print("[Info] ==> Database created successfully...")
    # Return a cursor for the connection
    cur = con.cursor()

    # create tables and add columns of the tables
    cur.execute("""
        
        CREATE TABLE IF NOT EXISTS Person(id INTEGER PRIMARY KEY, first_name TEXT, father TEXT, last_name TEXT, 
                            gender TEXT, birth_year DATE, address TEXT)                             
    """)

    cur.execute("""
                CREATE TABLE IF NOT EXISTS Offense(id INTEGER PRIMARY KEY, name TEXT)
            """)

    cur.execute("""

            CREATE TABLE IF NOT EXISTS Convicts(id INTEGER PRIMARY KEY, from_date DATE, to_date DATE, 
                                person_id INTEGER NOT NULL,
                                offense_id INTEGER NOT NULL,
                                FOREIGN KEY(person_id) REFERENCES Person(id), 
                                FOREIGN KEY(offense_id) REFERENCES Offense(id))
        """)

    cur.execute("""
                    CREATE TABLE IF NOT EXISTS Dungeon(id INTEGER PRIMARY KEY, name TEXT, size FLOAT)
                """)

    cur.execute("""
                    CREATE TABLE IF NOT EXISTS DungeonMoves(id INTEGER PRIMARY KEY,
                     from_date DATE,
                     dungeon_id INTEGER NOT NULL,
                     person_id INTEGER NOT NULL,
                     FOREIGN KEY(dungeon_id) REFERENCES Dungeon(id),
                     FOREIGN KEY(person_id) REFERENCES Person(id)
                     )
                      
                """)

    cur.execute("""
                    CREATE TABLE IF NOT EXISTS Visitings(id INTEGER PRIMARY KEY, date_visited DATE,
                      Visitor_name TEXT,
                      mountin_muinutes INTEGER,
                      person_id INTEGER NOT NULL,
                      FOREIGN KEY(person_id) REFERENCES Person(id) 
                      )
                      
                """)

    con.commit()

    # return the database that we created once then connect with it to use it in other classees
    return con


# call function >> create_database()

# create_database()
# print("[Info] ==> Database created, you can connect with it")




