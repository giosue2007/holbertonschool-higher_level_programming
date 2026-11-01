#!/usr/bin/python3
"""Generate personalized invitation files from a template."""


def generate_invitations(template, attendees):
    """Create one output file per attendee by filling in the template."""
    if not isinstance(template, str):
        print("Invalid input: template must be a string.")
        return
    if not isinstance(attendees, list):
        print("Invalid input: attendees must be a list of dictionaries.")
        return
    for person in attendees:
        if not isinstance(person, dict):
            print("Invalid input: attendees must be a list of dictionaries.")
            return

    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return
    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    placeholders = ["name", "event_title", "event_date", "event_location"]

    for index, person in enumerate(attendees, start=1):
        text = template
        for key in placeholders:
            value = person.get(key)
            if value is None:
                value = "N/A"
            text = text.replace("{" + key + "}", str(value))

        filename = f"output_{index}.txt"
        try:
            with open(filename, "w") as file:
                file.write(text)
        except OSError as error:
            print(f"Error: could not write {filename}: {error}")
