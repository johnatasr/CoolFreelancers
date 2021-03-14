from freelancer.domain.entities import Freelancer, Skill, ProcessedFreelancer
from datetime import datetime
from django.test import TestCase
from typing import List
import datetime


class FreelancerEnttityTestCase(TestCase):
    """
    Testes da Entidade Freelancer
    """

    def setUp(self):
        self.freelancer_one = Freelancer(
            id=1,
            user= { "firstName": "teste1",  "lastName": "1last", "jobTitle": "Teste JS Developer" },
            status="new",
            retribution=100,
            availability_date= "2020-06-10T00:00:00+01:00",
            professional_experiences=[]
        )

        self.freelancer_two = Freelancer(
            id=2,
            user={"firstName": "teste2", "lastName": "2last", "jobTitle": "Teste Python Developer"},
            status="new",
            retribution=200,
            availability_date=datetime.datetime("2021-06-10T00:00:00+01:00"),
            professional_experiences=[]
        )

    def test_isistance_freelancer(self):
        self.assertIsInstance(self.freelancer_one, object)
        self.assertIsInstance(self.freelancer_two, object)

    def test_atributes_values_freelancer(self):
        user1 = { "firstName": "teste1",  "lastName": "1last", "jobTitle": "Teste JS Developer" }
        user2 = {"firstName": "teste2", "lastName": "2last", "jobTitle": "Teste Python Developer"}

        self.assertEquals(self.freelancer_one.id, 1)
        self.assertEquals(self.freelancer_one.user, user1)
        self.assertEquals(self.freelancer_one.status, 'new')
        self.assertEquals(self.freelancer_one.retribution, 100)
        self.assertEquals(self.freelancer_one.availability_date, datetime.datetime("2020-06-10T00:00:00+01:00"))
        self.assertEquals(self.freelancer_one.professional_experiences, [])

        self.assertEquals(self.freelancer_two.id, 2)
        self.assertEquals(self.freelancer_two.user, user2)
        self.assertEquals(self.freelancer_one.status, 'new')
        self.assertEquals(self.freelancer_one.retribution, 200)
        self.assertEquals(self.freelancer_one.availability_date, datetime.datetime("2021-06-10T00:00:00+01:00"))
        self.assertEquals(self.freelancer_one.professional_experiences, [])

    def test_atributes_type_freelancer(self):
        self.assertIsInstance(self.freelancer_one.id, int)
        self.assertIsInstance(self.freelancer_one.user, dict)
        self.assertIsInstance(self.freelancer_one.status, str)
        self.assertIsInstance(self.freelancer_one.retribution, int)
        self.assertIsInstance(self.freelancer_one.availability_date, datetime)
        self.assertIsInstance(self.freelancer_one.professional_experiences, list)

        self.assertIsInstance(self.freelancer_two.id, int)
        self.assertIsInstance(self.freelancer_two.user, dict)
        self.assertIsInstance(self.freelancer_one.status, str)
        self.assertIsInstance(self.freelancer_one.retribution, int)
        self.assertIsInstance(self.freelancer_one.availability_date, datetime)
        self.assertIsInstance(self.freelancer_one.professional_experiences, list)


class SkillEnttityTestCase(TestCase):
    """
    Testes da entidade Skill
    """
    def setUp(self):
        self.skill_one = Skill(
            id=1,
            name='React',
            duration_months=300,
        )

        self.skill_two = Skill(
            id=2,
            name='Django',
            duration_months=400,
        )

    def test_isistance_skill(self):
        self.assertIsInstance(self.skill_one, object)
        self.assertIsInstance(self.skill_two, object)


    def test_atributes_values_skill(self):
        self.assertEquals(self.skill_one.id, 1)
        self.assertEquals(self.skill_one.name, 'React')
        self.assertEquals(self.skill_one.duration_months, 300)

        self.assertEquals(self.skill_two.id, 2)
        self.assertEquals(self.skill_two.name, 'Django')
        self.assertEquals(self.skill_two.duration_months, 400)

    def test_atributes_type_skill(self):
        self.assertIsInstance(self.skill_one.id, int)
        self.assertIsInstance(self.skill_one.name, str)
        self.assertIsInstance(self.skill_one.duration_months, int)

        self.assertIsInstance(self.skill_two.id, int)
        self.assertIsInstance(self.skill_two.name, str)
        self.assertIsInstance(self.skill_two.duration_months, int)


class ProcessedFreelancerEnttityTestCase(TestCase):
    """
    Testes da entidade ProcessedFreelancer
    """

    def setUp(self):
        self.skill_one = Skill(
            id=1,
            name='React',
            duration_months=300,
        )

        self.skill_two = Skill(
            id=2,
            name='Django',
            duration_months=400,
        )

        self.proc_freelancer_one = ProcessedFreelancer(
            id=1,
            computed_skills=[self.skill_one]
        )

        self.proc_freelancer_two = ProcessedFreelancer(
            id=2,
            computed_skills=[self.skill_two]
        )

    def test_isistance_skill(self):
        self.assertIsInstance(self.proc_freelancer_one, object)
        self.assertIsInstance(self.proc_freelancer_two, object)

    def test_atributes_values_skill(self):
        self.assertEquals(self.proc_freelancer_one.id, 1)
        for skill in self.proc_freelancer_one:
            self.assertEquals(skill.name, 'React')

        self.assertEquals(self.proc_freelancer_two.id, 2)
        for skill in self.proc_freelancer_two:
            self.assertEquals(skill.name, 'Django')

    def test_atributes_type_skill(self):
        self.assertIsInstance(self.proc_freelancer_one.id, int)
        self.assertIsInstance(self.proc_freelancer_one.computed_skills, List[Skill])

        self.assertIsInstance(self.proc_freelancer_two.id, int)
        self.assertIsInstance(self.proc_freelancer_two.computed_skills, List[Skill])


