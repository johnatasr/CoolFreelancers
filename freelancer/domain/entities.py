import enum
from typing import Type, List
import datetime


class Freelancer(object):
    """ Freelancer Entity """

    def __init__(self,
                 id: int,
                 user: dict,
                 status: str,
                 retribution: int,
                 availability_date: datetime,
                 professional_experiences: list):
        self._id = id
        self._user = user,
        self._status = status,
        self._retribution = retribution,
        self._availability_date = availability_date,
        self._professional_experiences = professional_experiences

    @property
    def id(self):
        return self._id

    @property
    def user(self):
        return self._user

    @property
    def retribution(self):
        return self._retribution

    @property
    def availability_date(self):
        return self._availability_date

    @property
    def professional_experiences(self):
        return self._professional_experiences

    @property
    def end(self):
        return self._end


class Skill(object):
    """ Skill Entity """

    def __init__(self, id: int, name: str, duration_months: int):
        self._id = id
        self._name = name
        self._duration_months = duration_months

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def duration_months(self):
        return self._duration_months


class ProcessedFreelancer(object):
    """ Experiance Entity """

    def __init__(self, id: int, computed_skills: List[Skill]):
        self._id = id
        self._computed_skills = computed_skills

    @property
    def id(self):
        return self._id

    @property
    def computed_skills(self):
        return self._computed_skills
