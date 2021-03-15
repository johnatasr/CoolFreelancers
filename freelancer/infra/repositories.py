from freelancer.presenters.exceptions import ConflictException
from freelancer.presenters.helpers import FreelancerHelpers
from freelancer.domain.entities import (
    Freelancer,
    Skill,
    ProcessedFreelancer
)
from typing import List


class FreelancerRepo:
    """
        Camada onde ocorre a interação do Interator com as Entidades e Modelos,
        Ocorre tambem grande parte da regra de negocio
    """

    helper = FreelancerHelpers()

    def create_skill_entity_by_list(self, skills: list):
        """
            Cria uma lista de Entidade Skills no formato final
        """
        try:
            list_of_skills: List[Skill] = []
            for skill in skills:
                list_of_skills.append(
                    Skill(
                        id=skill['id'],
                        name=skill['name'],
                        duration_months=skill['total_months'])
                )
            return list_of_skills
        except ConflictException as err:
            raise ConflictException(source='repository', code='conflit_in_create',
                                    message=f'Não possível skill, erro : {err}')

    def create_searched_freelancer_entity(self, freelancer_id: int, skills: list):
        """
            Cria a Entidade final para serializacao
        """
        return ProcessedFreelancer(
            id=freelancer_id,
            computed_skills=skills
        )

    def create_freelancer_entity(self, payload: dict):
        """
            Cria a Entidade base Freelance
        """
        return Freelancer(
            id=payload['id'],
            user=payload['user'],
            status=payload['status'],
            retribution=payload['retribution'],
            availability_date=payload['availabilityDate'],
            professional_experiences=payload['professionalExperiences']
        )

    def process_freelancer_experiences(self, freelancer: object):
        """
            Ocorre o processamento da busca com os meses totais de cada skill
        """
        try:
            skills: list = []
            empty_skills_list: bool = True
            sorted_experiances = self.helper.get_experiences_by_startdate(freelancer.professional_experiences)
            experiences = self.helper.update_date_experiences(sorted_experiances)
            for experience in experiences:
                months: int = self.helper.diff_beetween_dates(
                                            experience['startDate'], experience['endDate'])
                for skill in experience['skills']:
                    if empty_skills_list:
                        skills.append(self.helper.create_skill_dict(skill, months, experience))
                        empty_skills_list = False
                    else:
                        skill_update: bool = False
                        for index, sk in enumerate(skills):
                            if sk['id'] == skill['id']:
                                if sk['last_end_date'] < experience['startDate']:
                                    sk['total_months'] += months
                                else:
                                    sk = self.helper.update_skill_process(
                                        experience=experience,
                                        sk=sk,
                                        months=months
                                    )
                                sk = self.helper.set_last_skill_date(experience=experience, sk=sk)
                                skill_update = True

                        if not skill_update:
                            skills.append(self.helper.create_skill_dict(skill, months, experience))

            skills: list = self.create_skill_entity_by_list(skills)
            return self.create_searched_freelancer_entity(freelancer_id=freelancer.id, skills=skills)

        except ConflictException as err:
            raise ConflictException(source='repository', code='conflit_in_create',
                                          message=f'Não possível criar busca, erro : {err}')


