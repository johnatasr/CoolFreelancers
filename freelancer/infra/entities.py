import enum
from typing import Type
import datetime


class Freelancer(object):
    """ Freelancer Entity """

    def __init__(self,
            id: int,
            user: object,
            status: str,
            retribution: int,
            availability_date: Type[datetime],
            professional_experiences: list(object)):
        self.id = id
        self.user = user,
        self.status = status,
        self.retribution = retribution,
        self.availabilityDate = availability_date,
        self.professionalExperiences = professional_experiences

    def __repr__(self):
        return f"Pet: [name={self.name}, specie={self.specie}, user_id={self.user_id}]"

    def __eq__(self, other):
        if (
                self.id == other.id
                and self.name == other.name
                and self.specie == other.specie
                and self.age == other.age
                and self.user_id == other.user_id
        ):
            return True
        return False