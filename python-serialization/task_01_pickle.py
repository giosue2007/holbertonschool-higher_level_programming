#!/usr/bin/env python3
"""
Module defining a CustomObject class with pickle serialization/deserialization.
"""
import pickle


class CustomObject:
    """A custom class with attributes and pickle persistence capabilities."""

    def __init__(self, name: str, age: int, is_student: bool):
        """Initialize the CustomObject with name, age, and student status."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display the attributes of the object."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize the current object instance and save it to a file using pickle."""
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Load and deserialize an instance of CustomObject from a file."""
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except Exception:
            return None
