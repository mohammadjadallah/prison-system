# Dependacies
from personClass import Person
from convictsClass import Convicts
from offenseClass import Offense
from dungeonClass import Dungeon
from dungeonMoves import DungeonMoves
from visitingsClass import Visitings

# =====================  Main  =================

if __name__ == "__main__":

    # HERE YOU CAN CREATE OBJECTS FROM CLASSES AND USE THEM

    # Object
    # visiting = Visitings(date_visited="2002-5-20", person_id=1, visitor_name='Naser Salem Hadi', mountin_minutes=5)
    # visiting = Visitings(date_visited="2013-3-28", person_id=1, visitor_name='Abdullah Salem Hadi', mountin_minutes=10)
    # visiting = Visitings(date_visited="2014-6-28", person_id=1, visitor_name='Ayah Waleed Rami', mountin_minutes=15)
    # visiting = Visitings(date_visited="2020-4-15", person_id=1, visitor_name='Sars Nadeem Rawaad', mountin_minutes=10)
    visiting = Visitings(date_visited="2020-6-20", person_id=1, visitor_name='Hadi Khaled deeb', mountin_minutes=8)
    # visiting.add_new_visiting()
    # print(visiting.iformation_visitings())
    print(visiting.info_visitings_date("2002-5-20", "2020-4-15"))

