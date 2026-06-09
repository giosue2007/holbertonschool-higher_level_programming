#!/usr/bin/python3
"""
This module prints the first State object from the database hbtn_0e_6_usa
using SQLAlchemy.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # Connexion à la base de données MySQL
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )

    # Ouverture de la session ORM
    Session = sessionmaker(bind=engine)
    session = Session()

    # Requête ORM pour récupérer uniquement le premier État par son ID
    first_state = session.query(State).order_by(State.id).first()

    # Affichage du résultat selon s'il existe ou non
    if first_state is None:
        print("Nothing")
    else:
        print("{}: {}".format(first_state.id, first_state.name))

    # Fermeture de la session
    session.close()
