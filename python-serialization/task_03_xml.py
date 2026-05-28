#!/usr/bin/env python3
"""Module for serializing and deserializing Python dictionaries to/from XML."""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary: dict, filename: str) -> None:
    """Serializes a Python dictionary into an XML file."""
    # 1. On crée la balise principale (le root) <data>
    root = ET.Element("data")

    # 2. On boucle sur le dictionnaire pour créer les sous-balises
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    # 3. On enregistre le tout dans le fichier
    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename: str) -> dict:
    """Reads an XML file and reconstructs it into a Python dictionary."""
    try:
        # 1. On ouvre et on analyse le fichier XML
        tree = ET.parse(filename)
        root = tree.getroot()

        # 2. On reconstruit le dictionnaire en lisant chaque balise enfant
        result_dict = {}
        for child in root:
            result_dict[child.tag] = child.text

        return result_dict

    except Exception:
        return {}
