#!/usr/bin/env python3
"""
Module to convert CSV data to JSON format.
"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """Converts a CSV file to a JSON file (data.json)."""
    try:
        with open(csv_filename, "r", encoding="utf-8") as csv_f:
            reader = csv.DictReader(csv_f)
            data = list(reader)

        with open("data.json", "w", encoding="utf-8") as json_f:
            json.dump(data, json_f, indent=4)

        return True
    except Exception:
        return False
