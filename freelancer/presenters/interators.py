from freelancer.presenters.interfaces import IIterator
from freelancer.infra.serializers import FreelancerSearchedSerializer
from freelancer.presenters.validators import FreelancerValidator
from freelancer.infra.repositories import FreelancerRepo


class FreelancerInterator(IIterator):

    def __init__(self):
        self.validator: object = FreelancerValidator
        self.repo: object = FreelancerRepo
        self.serializer: object = FreelancerSearchedSerializer

    def set_params(self, frelancer_payload: (dict, list)):
        self.payload = frelancer_payload
        return self

    def execute(self):
        valided_payload = self.validator(self.payload).validate_payload()

        if valided_payload[0]:
            created_freelancer_entity: object = self.repo().create_freelancer_entity(valided_payload[1])
            precessed_freelancer_entity: object = self.repo().process_freelancer_experiences(created_freelancer_entity)
            serialized_freelancer = self.serializer(precessed_freelancer_entity).serialize_object()
            return serialized_freelancer



