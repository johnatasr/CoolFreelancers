from django.test import TestCase
from freelancer.infra.repositories import FreelancerRepo
from freelancer.infra.serializers import FreelancerSearchedSerializer
from freelancer.domain.entities import Freelancer, Skill, ProcessedFreelancer
from datetime import datetime


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
            availability_date=datetime.strptime("2020-06-10T00:00:00+01:00".split('T')[0], '%Y-%m-%d'),
            professional_experiences=self.return_payload_skills()
        )

        self.skills_list = [{"id": i, "name": f"{i}_teste", "total_months": i + 10} for i, sk in enumerate(range(1, 5))]
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

    """
        Testes de métodos de freelancer.infra.repositories
    """

    def test_create_skill_entity_by_list(self):
        list_skills_entity = self.repo.create_skill_entity_by_list(self.skills_list)
        self.assertIsInstance(list_skills_entity, list)
        self.assertEquals(len(list_skills_entity), 4)

    def test_create_searched_freelancer_entity(self):
        searched_freelancer_entity = self.repo.create_searched_freelancer_entity(freelancer_id=1, skills=[])
        self.assertIsInstance(searched_freelancer_entity, object)
        self.assertEquals(searched_freelancer_entity.id, 1)
        self.assertEquals(len(searched_freelancer_entity.computed_skills), 0)

    def test_create_freelancer_entity(self):
        freelancer_entity = self.repo.create_freelancer_entity({
                    "id": 42,
                    "user": {
                      "firstName": "Hunter",
                      "lastName": "Moore",
                      "jobTitle": "Fullstack JS Developer"
                    },
                    "status": "new",
                    "retribution": 650,
                    "availabilityDate": "2018-06-13T00:00:00+01:00",
                    "professionalExperiences": []
              })
        self.assertIsInstance(freelancer_entity, object)
        self.assertEquals(freelancer_entity.id, 42)
        self.assertEquals(freelancer_entity.user[0]['firstName'], "Hunter")
        self.assertEquals(freelancer_entity.status[0], "new")
        self.assertEquals(freelancer_entity.retribution[0], 650)
        self.assertEquals(freelancer_entity.availability_date[0], "2018-06-13T00:00:00+01:00")
        self.assertEquals(freelancer_entity.professional_experiences, [])

    def test_process_freelancer_experiences(self):
        processed_freelancer_entity = self.repo.process_freelancer_experiences(self.freelancer_one)
        self.assertIsInstance(processed_freelancer_entity, object)
        self.assertEquals(processed_freelancer_entity.id, 1)
        self.assertEquals(processed_freelancer_entity.computed_skills[0].name, "MySQL")
        self.assertEquals(processed_freelancer_entity.computed_skills[1].name, "Java")
        self.assertEquals(processed_freelancer_entity.computed_skills[2].name, "Javascript")
        self.assertEquals(processed_freelancer_entity.computed_skills[3].name, "React")
        self.assertEquals(processed_freelancer_entity.computed_skills[4].name, "Node.js")


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

    """
          Testes de métodos de freelancer.infra.serializers
    """

    def test_serialize_object(self):
        payload = self.serializer.serialize_object()
        self.assertIsInstance(payload, dict)
        self.assertEquals(payload['freelance']['id'], 1)
        self.assertEquals(len(payload['freelance']['computedSkills']), 4)
        self.assertEquals(payload['freelance']['computedSkills'][0]['id'], 1)
        self.assertEquals(payload['freelance']['computedSkills'][0]['name'], '1_skill')
        self.assertEquals(payload['freelance']['computedSkills'][0]['durationInMonths'], 11)
        self.assertEquals(payload['freelance']['computedSkills'][2]['id'], 3)
        self.assertEquals(payload['freelance']['computedSkills'][2]['name'], '3_skill')
        self.assertEquals(payload['freelance']['computedSkills'][2]['durationInMonths'], 13)

    def test_set_nested_to_dict(self):
        payload = self.serializer.set_nested_to_dict(self.skils)
        self.assertIsInstance(payload, list)
        self.assertEquals(payload[0]['id'], 1)
        self.assertEquals(len(payload), 4)

    def test_mount_payload(self):
        payload = self.serializer.mount_payload(self.freelancer_one)
        self.assertIsInstance(payload['freelance'], dict)
        self.assertEquals(len(payload['freelance']['computedSkills']), 4)
        self.assertEquals(payload['freelance']['computedSkills'][0]['id'], 1)

