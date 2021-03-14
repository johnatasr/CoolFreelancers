from freelancer.presenters.exceptions import ConflictException
from freelancer.presenters.helpers import FreelancerHelpers
from .entities import (
    Freelancer,
    Skill,
    ProcessedFreelancer
)
from typing import List


class FreelancerRepo:

    helper = FreelancerHelpers()

    def create_skill_entity_by_list(self, skills: list):
        try:
            list_of_skills: List[Skill] = []
            for skill in skills:
                list_of_skills.append(
                    Skill(
                        id=skill['id'],
                        name=skill['name'],
                        duration_months=skill['months'])
                )
            return list_of_skills
        except ConflictException as err:
            raise ConflictException(source='repository', code='conflit_in_create',
                                    message=f'Não possível skill, erro : {err}')

    def create_searched_freelancer_entity(self, freelancer_id: int, skills: list):
        return ProcessedFreelancer(
            id=freelancer_id,
            computed_skills=skills
        )

    def create_freelancer_entity(self, payload: dict):
        return Freelancer(
            id=payload['id'],
            user=payload['user'],
            status=payload['status'],
            retribution=payload['retribution'],
            availability_date=payload['availabilityDate'],
            professional_experiences=payload['professionalExperiences']
        )

    def process_freelancer_experiances(self, freelancer: object):
        try:
            skills: list = []
            sorted_experiances = self.helper.get_experiences_by_startdate(freelancer.professional_experiences)
            experiences = self.helper.update_date_experiences(sorted_experiances)
            for experience in experiences:
                months = self.helper.diff_beetween_dates(experience['startDate'], experience['endDate'])
                for skill in experience['skills']:
                    if len(skills) > 0:
                        for sk in skills:
                            if sk['id'] == skill['id'] and sk['id_exp'] != experience['id']:
                                if sk['end_date'] < experience['startDate']:
                                    sk['total_months'] += months
                                else:
                                    sk['total_months'] = self.helper.diff_beetween_dates(sk['start_date'],
                                                                                         experience['endDate'])
                                sk['start_date'] = experience["startDate"]
                                sk['end_date'] = experience["endDate"]
                            else:
                                skills.append(self.helper.create_skill_dict(skill, months, experience))
                    else:
                        skills.append(self.helper.create_skill_dict(skill, months, experience))

            skills: list = self.create_skills_entity_list(skills)
            return self.create_searched_freelancer_entity(freelancer_id=freelancer.id, skills=skills)

        except ConflictException as err:
            raise ConflictException(source='repository', code='conflit_in_create',
                                          message=f'Não possível criar busca , erro : {err}')


