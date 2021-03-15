from freelancer.presenters.helpers import FreelancerHelpers
from rest_framework import status
from rest_framework.test import APITestCase
from django.test import TestCase
from datetime import datetime


class HelpersTests(TestCase):
    """
        Testes das helpers
    """


    def setUp(self) -> None:
        self.helper = FreelancerHelpers()
        self.exps = [
              {
                "id": 4,
                "companyName": "Okuneva, Kerluke and Strosin",
                "startDate": datetime.strptime("2016-01-01T00:00:00+01:00".split('T')[0], '%Y-%m-%d'),
                "endDate":  datetime.strptime("2018-05-01T00:00:00+01:00".split('T')[0], '%Y-%m-%d'),
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
                "startDate": datetime.strptime("2014-01-01T00:00:00+01:00".split('T')[0], '%Y-%m-%d'),
                "endDate": datetime.strptime("2017-01-01T00:00:00+01:00".split('T')[0], '%Y-%m-%d'),
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

        self.sk = {
                'id': 1,
                'name': 'Golang',
                'total_months': 10,
                'last_start_date': datetime.strptime("2014-01-01T00:00:00+01:00".split('T')[0], '%Y-%m-%d'),
                'last_end_date': datetime.strptime("2016-09-01T00:00:00+01:00".split('T')[0], '%Y-%m-%d')
                }

    """
        Testes de métodos de freelancer.presenters.helpers
    """

    def test_get_experiences_by_startdate(self):
        sorted_dates = self.helper.get_experiences_by_startdate(self.exps)
        self.assertEquals(sorted_dates[0]['startDate'], datetime(2014, 1, 1))
        self.assertEquals(sorted_dates[0]['id'], 54)

    def test_diff_beetween_dates(self):
        start_date = datetime.strptime("2014-01-01T00:00:00+01:00".split('T')[0], '%Y-%m-%d')
        end_date = datetime.strptime("2016-09-01T00:00:00+01:00".split('T')[0], '%Y-%m-%d')
        result = self.helper.diff_beetween_dates(start_date, end_date)
        self.assertEquals(result, 32)

    def test_update_date_experiences(self):
        exp = [{
            "startDate": "2014-01-01T00:00:00+01:00",
            "endDate": "2016-09-01T00:00:00+01:00"
        }]
        result = self.helper.update_date_experiences(exp)
        self.assertEquals(result[0]['startDate'], datetime(2014, 1, 1))
        self.assertEquals(result[0]['endDate'], datetime(2016, 9, 1))

    def test_update_skill_process(self):
        skill = self.helper.update_skill_process(self.exps[0], self.sk, 14)
        self.assertEquals(skill['total_months'], 16)

    def test_set_last_skill_date(self):
        skill = self.helper.set_last_skill_date(self.exps[0], self.sk)
        self.assertEquals(skill['last_start_date'], datetime(2016, 1, 1))
        self.assertEquals(skill['last_end_date'], datetime(2018, 5, 1))


class FreelancerViewSetTestCase(APITestCase):
    """
       Testes para API Viewset
    """

    def setUp(self):
        self.data = {
          "freelance": {
            "id": 42,
            "user": {
              "firstName": "Hunter",
              "lastName": "Moore",
              "jobTitle": "Fullstack JS Developer"
            },
            "status": "new",
            "retribution": 650,
            "availabilityDate": "2018-06-13T00:00:00+01:00",
            "professionalExperiences": [
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
              },
              {
                "id": 80,
                "companyName": "Harber, Kirlin and Thompson",
                "startDate": "2013-05-01T00:00:00+01:00",
                "endDate": "2014-07-01T00:00:00+01:00",
                "skills": [
                  {
                    "id": 370,
                    "name": "Javascript"
                  },
                  {
                    "id": 400,
                    "name": "Java"
                  }
                ]
              }
            ]
          }
        }


    def test_get_freelance_empty_data(self):
        """
            Teste de requisicao sem dados
        """

        response = self.client.post('/freelancers/send-freelance')
        self.assertEqual(response.status_code, status.HTTP_422_UNPROCESSABLE_ENTITY)

    def test_get_freelance_whith_data(self):
        """
            Teste de requisicao com dados
        """

        response = self.client.post('/freelancers/send-freelance', data=self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['freelance']['id'], 42)
        processed_skills_list = response.data['freelance']['computedSkills']
        self.assertEquals(len(processed_skills_list), 5)

