import unittest
import json
import sys

sys.path.append("..")
from app.models.Freelancer import Freelancer


class FreelancerTest(unittest.TestCase):
    def loadJson(self, fileName):
        with open(f'./jsonTests/{fileName}.json') as json_file:
            data = json.load(json_file)
            return data

    def test_calculate_diff_success(self):
        '''
            Test json payload in perfect situation - must success
        '''
        # Arrange
        data = self.loadJson("freelancer")
        freelancer = Freelancer()
        # Act
        freelancer.processExperiences(data["freelance"])
        result = freelancer.computedSkills
        # Assert
        self.assertEqual(result[0].durationInMonths, 28)
        self.assertEqual(result[1].durationInMonths, 28)
        self.assertEqual(result[2].durationInMonths, 60)
        self.assertEqual(result[3].durationInMonths, 32)
        self.assertEqual(result[4].durationInMonths, 40)

    def test_calculate_diff_months_overlap_success(self):
        '''
            Test json payload when have a months overlap - must success
        '''
        # Arrange
        data = self.loadJson("freelancerOverlap")
        freelancer = Freelancer()
        # Act
        freelancer.processExperiences(data["freelance"])
        result = freelancer.computedSkills

        # Assert
        self.assertEqual(result[0].durationInMonths, 27)
        self.assertEqual(result[1].durationInMonths, 27)
        self.assertEqual(result[2].durationInMonths, 60)
        self.assertEqual(result[3].durationInMonths, 29)
        self.assertEqual(result[4].durationInMonths, 38)

    def test_calculate_diff_months_gap_success(self):
        '''
            Test json payload when have a gap months spaced  - must success
        '''
        # Arrange
        data = self.loadJson("freelancerGapSituation")
        freelancer = Freelancer()
        # Act
        freelancer.processExperiences(data["freelance"])
        result = freelancer.computedSkills

        # Assert
        self.assertEqual(result[0].durationInMonths, 21)
        self.assertEqual(result[1].durationInMonths, 21)
        self.assertEqual(result[2].durationInMonths, 53)
        self.assertEqual(result[3].durationInMonths, 24)
        self.assertEqual(result[4].durationInMonths, 32)

    def test_calculate_diff_months_random_date_experiences_success(self):
        '''
            Test json payload when the experiences have a random date orders - must success
        '''
        # Arrange
        data = self.loadJson("freelancerRandomSortExperiencesSituation")
        freelancer = Freelancer()
        # Act
        freelancer.processExperiences(data["freelance"])
        result = freelancer.computedSkills

        # Assert
        self.assertEqual(result[0].durationInMonths, 28)
        self.assertEqual(result[1].durationInMonths, 28)
        self.assertEqual(result[2].durationInMonths, 60)
        self.assertEqual(result[3].durationInMonths, 32)
        self.assertEqual(result[4].durationInMonths, 40)