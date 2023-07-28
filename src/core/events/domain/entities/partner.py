from dataclasses import dataclass
from typing import TypedDict

from src.core.common.domain.aggregate_root import AggregateRoot


@dataclass
class PartnerCommand(TypedDict):
    name: str


@dataclass
class Partner(AggregateRoot):
    name: str

    @staticmethod
    def create(command: PartnerCommand) -> 'Partner':
        return Partner(
            name=command['name']
        )
