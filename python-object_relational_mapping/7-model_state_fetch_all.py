#!/usr/bin/python3
"""
This module fetches and lists all State objects
from the database hbtn_0e_6_usa using SQLAlchemy.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # 1. Création du moteur de connexion SQLAlchemy
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )

    # 2. Configuration et ouverture de la session ORM
    Session = sessionmaker(bind=engine)
    session = Session()

    # 3. Requête ORM pour récupérer et trier tous les États
    states = session.query(State).order_by(State.id).all()

    # 4. Affichage des résultats
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # 5. Fermeture de la session
    session.close()
