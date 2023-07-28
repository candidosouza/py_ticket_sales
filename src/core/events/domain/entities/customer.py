from dataclasses import dataclass
from typing import TypedDict
from src.core.common.domain.aggregate_root import AggregateRoot
from src.core.common.domain.value_objects import Cpf


@dataclass
class CustomerCommand(TypedDict):
    cpf: str
    name: str


@dataclass(frozen=True, slots=True, kw_only=True)
class Customer(AggregateRoot):
    cpf: Cpf
    name: str

    @staticmethod
    def create(command: CustomerCommand) -> 'Customer':
        return Customer(
            cpf=Cpf(command['cpf']),
            name=command['name']
        )
    
    def change_name(self, name: str) -> None:
        if not name or not isinstance(name, str):
            raise ValueError("Nome Inválido")
        self._set('name', name)

    def to_dict(self):
        return {
            'id': self.id,
            'cpf': self.cpf.cpf,
            'name': self.name
        }
