from dataclasses import dataclass
from typing import Optional, TypedDict

from src.core.common.domain.aggregate_root import AggregateRoot


class EventCommand(TypedDict):
    name: str
    description: Optional[str]
    date: str
    total_spot: int
    partner_id: str


@dataclass
class Event(AggregateRoot):
    name: str
    description: Optional[str] = None
    date: str
    is_published: Optional[bool] = False
    total_spot: int
    total_spot_reserved: Optional[int] = 0
    partner_id: str

    def create(self, command: EventCommand) -> 'Event':
        return Event(
            name=command['name'],
            description=command['description'],
            date=command['date'],
            total_spot=command['total_spot'],
            partner_id=command['partner_id']
        )