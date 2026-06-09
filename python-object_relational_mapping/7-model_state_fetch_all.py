#!/usr/bin/python3
"""
This module lists all State objects from the database hbtn_0e_6_usa
using SQLAlchemy.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # Configuration du moteur de connexion à MySQL
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )

    # Création de la session pour interagir avec la base de données
    Session = sessionmaker(bind=engine)
    session = Session()

    # Récupération de tous les États, triés par ID de manière croissante
    states = session.query(State).order_by(State.id).all()

    # Affichage strict au format "id: name" demandé par le sujet
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # Fermeture propre de la session
    session.close()
