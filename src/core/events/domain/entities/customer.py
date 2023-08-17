from dataclasses import dataclass

from src.core.common.domain.aggregate_root import AggregateRoot
from src.core.common.domain.value_objects import Cpf


@dataclass(frozen=True, slots=True, kw_only=True)
class Customer(AggregateRoot):
    cpf: Cpf
    name: str

    def change_name(self, name: str) -> None:
        if not name or not isinstance(name, str):
            raise ValueError('Nome Inválido')
        self._set('name', name)
