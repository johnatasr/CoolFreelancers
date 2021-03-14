from datetime import datetime
from dateutil import relativedelta

class FreelancerHelpers:
    @staticmethod
    def get_experiences_by_startdate(experiaeces: list):
        try:
            experiences: dict = sorted(experiaeces, key=lambda experience: experience["startDate"], reverse=True)
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
    def create_skill_dict(skill, months, experience):
        return {
                'id': skill['id'],
                'name': skill['name'],
                'total_months': months,
                'start_date': experience['startDate'],
                'end_date': experience['endDate'],
                'id_exp': experience['id']
                }