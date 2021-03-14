from datetime import date, datetime
from ninja import Schema
from typing import List


class Skill(Schema):
    id: int
    name: str


class Experience(Schema):
    id: int
    company_name: str
    start_date: datetime
    end_date: datetime
    skills: List[Skill]


class User(Schema):
    first_name: str
    last_name: str
    job_title: str


class Freelancer(Schema):
    id: int = None
    user: User
    status: str
    retribution: str
    availability_date: str
    professional_experiences: List[Experience]
