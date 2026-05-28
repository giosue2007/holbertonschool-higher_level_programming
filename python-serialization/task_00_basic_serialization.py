#!/usr/bin/env python3
"""Module that defines serialization functions."""
import json


def serialize_and_save_to_file(data, filename):
    """Serialize a dictionary to a JSON file."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """Load and deserialize a JSON file to a dictionary."""
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
