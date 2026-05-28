#!/usr/bin/env python3
"""Module that defines convert_csv_to_json function."""
import csv
import json


def convert_csv_to_json(csv_filename):
    """Convert a CSV file to JSON format."""
    try:
        with open(csv_filename, encoding="utf-8") as f:
            reader = csv.DictReader(f)
            data = list(reader)
        with open("data.json", "w", encoding="utf-8") as f:
            json.dump(data, f)
        return True
    except FileNotFoundError:
        return False
