from freelancer.presenters.interfaces import IIterator
from freelancer.infra.serializers import FreelancerSearchedSerializer
from freelancer.presenters.validators import FreelancerValidator
from freelancer.infra.repositories import FreelancerRepo
from freelancer.presenters.exceptions import InteratorException


class FreelancerInterator(IIterator):
    """
        No interator ocorre a interação com grande parte dos modulos e libs
    """
    def __init__(self):
        """
            Inicializa a injecao de dependencia
        """
        self.validator: object = FreelancerValidator
        self.repo: object = FreelancerRepo
        self.serializer: object = FreelancerSearchedSerializer

    def set_params(self, frelancer_payload: (dict, list)):
        """
            Configura os paramentros
        """
        self.payload = frelancer_payload
        return self

    def execute(self):
        """
            Executa o fluxo a qual o interator foi designado
        """
        try:
            valided_payload = self.validator(self.payload).validate_payload()

            if valided_payload[0]:
                created_freelancer_entity: object = self.repo().create_freelancer_entity(valided_payload[1])
                precessed_freelancer_entity: object = self.repo().process_freelancer_experiences(created_freelancer_entity)
                serialized_freelancer = self.serializer(precessed_freelancer_entity).serialize_object()
                return serialized_freelancer
        except InteratorException as error:
            raise InteratorException(error)



