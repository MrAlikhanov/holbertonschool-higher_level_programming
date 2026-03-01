#!/usr/bin/python3
"""
This module defines an abstract base class Animal and its subclasses.
It demonstrates the use of the abc module to enforce method implementation.
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract base class representing an animal.
    """

    @abstractmethod
    def sound(self):
        """
        Abstract method that must be implemented by subclasses.
        """
        pass


class Dog(Animal):
    """
    Subclass of Animal representing a dog.
    """

    def sound(self):
        """
        Returns the sound a dog makes.
        """
        return "Bark"


class Cat(Animal):
    """
    Subclass of Animal representing a cat.
    """

    def sound(self):
        """
        Returns the sound a cat makes.
        """
        return "Meow"
