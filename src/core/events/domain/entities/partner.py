from dataclasses import dataclass
from typing import TypedDict

from src.core.common.domain.aggregate_root import AggregateRoot


@dataclass
class PartnerInput(TypedDict):
    name: str


@dataclass
class Partner(AggregateRoot):
    name: str

    @staticmethod
    def create(input: PartnerInput) -> 'Partner':
        return Partner(
            name=input['name']
        )
