from .interfaces import IValidator
from .exceptions import InvalidPayloadException
import json


class FreelancerValidator(IValidator):
    def __init__(self, payload):
        self.payload_raw = payload

    @staticmethod
    def valid(value: bool) -> bool:
        return value

    def check_experiences(self, professional_exps: list):
        for experiance in professional_exps:
            if 'startDate' not in experiance:
                raise InvalidPayloadException(source='validator', code='field_not_exists',
                                              message='Campo obrigatório: startDate')
            if 'endDate' not in experiance:
                raise InvalidPayloadException(source='validator', code='field_not_exists',
                                              message='Campo obrigatório: endDate')
            if 'skills' not in experiance:
                raise InvalidPayloadException(source='validator', code='field_not_exists',
                                              message='Campo obrigatório: skills')
            if len(experiance['skills']) <= 0:
                raise InvalidPayloadException(source='validator', code='empty_field',
                                              message='Campo obrigatório não pode estar vazio: skills')
            for skill in experiance['skills']:
                if 'name' not in skill:
                    raise InvalidPayloadException(source='validator', code='field_not_exists',
                                                  message='Campo obrigatório: skills')
        return True

    def is_raw_payload(self):
        ...

    def is_empty_payload(self) -> bool:
        if isinstance(self.payload_raw, (dict, object, list, bytes)):
           return True
        else:
            raise InvalidPayloadException(source='validator', code='empty_payload',
                                          message='Payload de requisição não pode ser vazio')

    def validate_payload(self) -> list:
        try:
            if not self.is_empty_payload():
                self._transform_to_json()

            if 'freelance' not in self.payload_raw:
                raise InvalidPayloadException(source='validator', code='field_not_exists',
                                              message='Campo obrigatório: freelance')
            payload = self.payload_raw['freelance']

            if 'id' not in payload:
                raise InvalidPayloadException(source='validator', code='field_not_exists',
                                              message='Campo obrigatório: user')
            if 'user' not in payload:
                raise InvalidPayloadException(source='validator', code='field_not_exists',
                                              message='Campo obrigatório: user')
            if 'professionalExperiences' not in payload:
                raise InvalidPayloadException(source='validator', code='field_not_exists',
                                              message='Campo obrigatório: professionalExperiences')
            if len(payload['professionalExperiences']) <= 0:
                raise InvalidPayloadException(source='validator', code='empty_field',
                                              message='Campo obrigatório tem que conter dados: professionalExperiences')
            try:
                self.check_experiences(payload['professionalExperiences'])
                return [self.valid(True), payload]

            except Exception as error:
                raise InvalidPayloadException(source='validator', code=error.code,
                                              message=error.args[0])

        except Exception as error:
            raise InvalidPayloadException(source='validator', code=error.code,
                                          message=error.args[0])

    def _transform_to_json(self):
        payload = json.dumps(self.payload_raw)
        return payload



