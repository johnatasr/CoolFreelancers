from freelancer.presenters.interfaces import ISerializer


class FreelancerSearchedSerializer(ISerializer):
    def __init__(self, freelancer: object):
        self.freelancer = freelancer

    def serialize_object(self):
        return self.mount_payload(self.freelancer)

    def set_nested_to_dict(self, skills: list):
        list_skills = []
        for skill in skills:
            sk = {
                "id": skill.id,
                "name": skill.name,
                "durationInMonths": skill.duration_months
            }
            list_skills.append(sk)
            list_skills = sorted(list_skills, key=lambda sk: sk["id"])

        return list_skills

    def mount_payload(self, freelance: object):
        return {
            'freelance': {
                'id': freelance.id,
                'computedSkills': self.set_nested_to_dict(freelance.computed_skills)
            }
        }
