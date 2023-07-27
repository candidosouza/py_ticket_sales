import json
import uuid
from abc import ABC
from dataclasses import dataclass, field, fields

from src.core.common.domain.exceptions import InvalidUuidException, InvalidCpfException


@dataclass(frozen=True, slots=True)
class ValueObject(ABC):

    def __str__(self):
        fields_name = [field.name for field in fields(self)]
        return str(getattr(self, fields_name[0])) \
            if len(fields_name) == 1 \
            else json.dumps({field_name: getattr(self, field_name) for field_name in fields_name})


@dataclass(frozen=True, slots=True)
class IdUUID(ValueObject):
    id: str = field(
        default_factory=lambda: str(uuid.uuid4())
    )

    def __str__(self):
        return f"{self.id}"

    def __post_init__(self):
        id_value = str(self.id) if isinstance(self.id, uuid.UUID) else self.id
        object.__setattr__(self, 'id', id_value)
        self.__validate()

    def __validate(self):
        try:
            uuid.UUID(self.id)
        except ValueError as ex:
            raise InvalidUuidException() from ex


@dataclass(frozen=True, slots=True)
class Cpf(ValueObject):
    cpf: str

    def __post_init__(self):
        self.__validate()

    def __validate(self):
        if not isinstance(self.cpf, str):
            raise InvalidCpfException("CPF deve ser uma string")

        cpf_digits = ''.join(filter(str.isdigit, self.cpf))

        if len(cpf_digits) != 11:
            raise InvalidCpfException("CPF deve ter 11 dígitos")

        if cpf_digits == cpf_digits[0] * 11:
            raise InvalidCpfException("CPF inválido")

        if not self.__validate_first_digit(cpf_digits) or not self.__validate_second_digit(cpf_digits):
            raise InvalidCpfException("CPF inválido")

        return True

    @staticmethod
    def __validate_first_digit(cpf: str) -> bool:
        total = sum(int(cpf[i]) * (10 - i) for i in range(9))
        remainder = total % 11
        first_digit = 0 if remainder < 2 else 11 - remainder
        return int(cpf[9]) == first_digit

    @staticmethod
    def __validate_second_digit(cpf: str) -> bool:
        total = sum(int(cpf[i]) * (11 - i) for i in range(10))
        remainder = total % 11
        second_digit = 0 if remainder < 2 else 11 - remainder
        return int(cpf[10]) == second_digit
