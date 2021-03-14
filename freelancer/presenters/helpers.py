from datetime import datetime
from dateutil import relativedelta


class FreelancerHelpers:
    @staticmethod
    def get_experiences_by_startdate(experiaeces: list):
        try:
            experiences: dict = sorted(experiaeces, key=lambda experience: experience["startDate"])
            return experiences
        except:
            raise Exception("Error when sorting the list")

    @staticmethod
    def diff_beetween_dates(start, end):
        result = relativedelta.relativedelta(end, start)
        return (result.years * 12) + result.months

    @staticmethod
    def update_date_experiences(experiences):
        for exp in experiences:
            exp['startDate'] = datetime.strptime(exp['startDate'].split('T')[0], '%Y-%m-%d')
            exp["endDate"] = datetime.strptime(exp["endDate"].split('T')[0], '%Y-%m-%d')
        return experiences

    @staticmethod
    def create_skill_dict(skill: dict, months: int, experience: object):
        return {
                'id': skill['id'],
                'name': skill['name'],
                'total_months': months,
                'last_start_date': experience['startDate'],
                'last_end_date': experience['endDate']
                }

    def update_skill_process(self, experience: object, sk: dict, months: int):
        diff: int = self.diff_beetween_dates(experience['startDate'],
                                            sk['last_end_date'])
        sk['total_months'] += (months - diff)
        return sk

    @staticmethod
    def set_last_skill_date(experience: object, sk: dict):
        sk['last_start_date'] = experience["startDate"]
        sk['last_end_date'] = experience["endDate"]
        return sk