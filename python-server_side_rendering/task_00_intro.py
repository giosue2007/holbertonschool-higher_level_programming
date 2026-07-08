#!/usr/bin/python3
"""Module for generating personalized invitation files from a template."""


def generate_invitations(template, attendees):
    """Generate invitation files from a template and a list of attendees.

    Args:
        template (str): The invitation template with placeholders.
        attendees (list): A list of dictionaries, each containing
            attendee data (name, event_title, event_date,
            event_location).

    Behavior:
        - Logs an error and stops if template is not a string.
        - Logs an error and stops if attendees is not a list of dicts.
        - Logs a specific message and stops if template is empty.
        - Logs a specific message and stops if attendees is empty.
        - Replaces any missing/None value with "N/A".
        - Writes one file per attendee: output_1.txt, output_2.txt, ...
    """
    # 1. Vérification des types
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return

    if not isinstance(attendees, list) or not all(
        isinstance(a, dict) for a in attendees
    ):
        print("Error: Attendees must be a list of dictionaries.")
        return

    # 2. Vérification des entrées vides
    if not template:
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    # 3. Traitement de chaque participant + écriture du fichier
    placeholders = ["name", "event_title", "event_date", "event_location"]

    for index, attendee in enumerate(attendees, start=1):
        output = template
        for key in placeholders:
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            output = output.replace("{" + key + "}", str(value))

        filename = f"output_{index}.txt"
        with open(filename, "w") as f:
            f.write(output)
