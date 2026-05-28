#!/usr/bin/env python3
"""Module for serializing and deserializing custom Python objects."""
import pickle


class CustomObject:
    """A custom class with serialize and deserialize methods."""

    def __init__(self, name: str, age: int, is_student: bool):
        """Initializes attributes."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self) -> None:
        """Prints out the object's attributes."""
        print(f"Name: {self.name}Age: {self.age}Is Student: {self.is_student}")

    def serialize(self, filename: str) -> None:
        """Saves the object to a file."""
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename: str):
        """Loads the object from a file."""
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except Exception:
            return None
