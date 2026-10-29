
from abc import ABC, abstractmethod


class AcademicElement(ABC):

    def __init__(self, name, title):
        self.name = name
        self.title = title

    @abstractmethod
    def calculate_average(self):
        pass

    @abstractmethod
    def calculate_credits(self):
        pass
