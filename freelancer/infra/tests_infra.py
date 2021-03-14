from django.test import TestCase
from typing import List, Type
from freelancer.infra.repositories import FreelancerRepo
from freelancer.infra.serializers import FreelancerSearchedSerializer
from freelancer.domain.entities import Freelancer, Skill, ProcessedFreelancer


class RepositoryTestCase(TestCase):
    """
    Tests da camada de repositório
    """

    def setUp(self):
        """
           Montando dependencias para os testes
        """

        self.freelancer_one = Freelancer(
            id=1,
            user={"firstName": "teste1", "lastName": "1last", "jobTitle": "Teste JS Developer"},
            status="new",
            retribution=100,
            availability_date="2020-06-10T00:00:00+01:00",
            professional_experiences=self.return_payload_skills()
        )

        self.skills_list = [{"id": i, "nome": f"{i}_teste", "total_months": i + 10} for i, sk in enumerate(range(1, 5))]
        self.repo = FreelancerRepo()

    def return_payload_skills(self):
        """
             Payload de teste
        """

        return [
              {
                "id": 4,
                "companyName": "Okuneva, Kerluke and Strosin",
                "startDate": "2016-01-01T00:00:00+01:00",
                "endDate": "2018-05-01T00:00:00+01:00",
                "skills": [
                  {
                    "id": 241,
                    "name": "React"
                  },
                  {
                    "id": 270,
                    "name": "Node.js"
                  },
                  {
                    "id": 370,
                    "name": "Javascript"
                  }
                ]
              },
              {
                "id": 54,
                "companyName": "Hayes - Veum",
                "startDate": "2014-01-01T00:00:00+01:00",
                "endDate": "2016-09-01T00:00:00+01:00",
                "skills": [
                  {
                    "id": 470,
                    "name": "MySQL"
                  },
                  {
                    "id": 400,
                    "name": "Java"
                  },
                  {
                    "id": 370,
                    "name": "Javascript"
                  }
                ]
            }
        ]

    def test_create_skill_entity_by_list(self):
        list_skills_entity = self.repo.create_skill_entity_by_list(self.skills_list)
        self.assertIsInstance(list_skills_entity, List[Skill])
        self.assertEquals(len(list_skills_entity), 5)

    def test_create_searched_freelancer_entity(self):
        searched_freelancer_entity = self.repo.create_searched_freelancer_entity(id=1, skills=[])
        self.assertIsInstance(searched_freelancer_entity, Type[ProcessedFreelancer])
        self.assertEquals(searched_freelancer_entity.id, 1)
        self.assertEquals(len(searched_freelancer_entity.computed_skills), 0)

    def test_create_freelancer_entity(self):
        freelancer_entity = self.repo.create_freelancer_entity(
            id=1,
            user={"firstName": "teste1", "lastName": "1last", "jobTitle": "Teste JS Developer"},
            status="new",
            retribution=100,
            availability_date="2020-06-10T00:00:00+01:00",
            professional_experiences=[])
        self.assertIsInstance(freelancer_entity, Type[Freelancer])
        self.assertEquals(freelancer_entity.id, 1)
        self.assertEquals(freelancer_entity.user['firstName'], "teste1")
        self.assertEquals(freelancer_entity.status, "new")
        self.assertEquals(freelancer_entity.retribution, 100)
        self.assertEquals(freelancer_entity.availability_date, "2020-06-10T00:00:00+01:00")
        self.assertEquals(freelancer_entity.professional_experiences, [])

    def test_process_freelancer_experiences(self):
        processed_freelancer_entity = self.repo.process_freelancer_experiences(self.freelancer_one)
        self.assertIsInstance(processed_freelancer_entity, Type[ProcessedFreelancer])
        self.assertEquals(processed_freelancer_entity.id, 1)
        self.assertEquals(processed_freelancer_entity.computed_skills[0]['name'], "Javascript")
        self.assertEquals(processed_freelancer_entity.computed_skills[1]['name'], "Java")
        self.assertEquals(processed_freelancer_entity.computed_skills[2]['name'], "MySQL")
        self.assertEquals(processed_freelancer_entity.computed_skills[3]['name'], "Node.js")
        self.assertEquals(processed_freelancer_entity.computed_skills[4]['name'], "React")


class SerializersTestCase(TestCase):
    """
    Tests da camada de serialização
    """

    def setUp(self):
        """
            Montando dependencias para os testes
        """

        self.skils = [Skill(id=i, name=f"{i}_skill", duration_months=i + 10) for i in range(1, 5)]
        self.freelancer_one = ProcessedFreelancer(
            id=1,
            computed_skills=self.skils
        )
        self.serializer = FreelancerSearchedSerializer(self.freelancer_one)

    def test_serialize_object(self):
        payload = self.serializer.serialize_object()
        self.assertIsInstance(payload, dict)
        self.assertEquals(payload['id'], 1)
        self.assertEquals(len(payload['computed_skills']), 5)
        self.assertEquals(payload['computed_skills'][0]['id'], 1)
        self.assertEquals(payload['computed_skills'][0]['name'], '1_skill')
        self.assertEquals(payload['computed_skills'][0]['duration_months'], 11)
        self.assertEquals(payload['computed_skills'][2]['id'], 3)
        self.assertEquals(payload['computed_skills'][0]['name'], '3_skill')
        self.assertEquals(payload['computed_skills'][0]['duration_months'], 13)

    def test_set_nested_to_dict(self):
        payload = self.serializer.set_nested_to_dict(self.skils)
        self.assertIsInstance(payload, list)
        self.assertEquals(payload[0]['id'], 1)
        self.assertEquals(len(payload), 5)

    def test_mount_payload(self):
        payload = self.serializer.mount_payload(self.freelancer_one)
        self.assertIsInstance(payload['freelance'], dict)
        self.assertEquals(len(payload['freelance']['computedSkills']), 5)
        self.assertEquals(payload['freelance']['computedSkills'][0]['id'], 1)

