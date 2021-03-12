import enum
from typing import Type
import datetime


class User(object):
    """ User Entity """

    def __init__(self,
         first_name: str,
         last_name: str,
         job_title: str):

        self._first_name = first_name
        self._last_name = last_name,
        self._job_title = job_title

    @property
    def first_name(self):
        return self._first_name

    @property
    def description(self):
        return self._last_name

    @property
    def status(self):
        return self._job_title


class Freelancer(object):
    """ Freelancer Entity """

    def __init__(self,
                id: int,
                user: User,
                status: str,
                retribution: int,
                availability_date: Type[datetime],
                professional_experiences: list(object)):

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

    # def __repr__(self):
    #     return f"Freelancer: [name={self._user.first_name}, specie={self.specie}, user_id={self.user_id}]"
    #
    # def __eq__(self, other):
    #     if (
    #             self.id == other.id
    #             and self.name == other.name
    #             and self.specie == other.specie
    #             and self.age == other.age
    #             and self.user_id == other.user_id
    #     ):
    #         return True
    #     return False