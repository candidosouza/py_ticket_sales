from dataclasses import dataclass, field
from typing import List, Optional, TypedDict

from src.core.common.domain.aggregate_root import AggregateRoot
from src.core.events.domain.entities.event_section import EventSection


@dataclass(frozen=True, slots=True, kw_only=True)
class EventCommand:
    name: str
    description: Optional[str]
    date: str
    total_spot: int
    partner_id: str
    sections: Optional[List[EventSection]]


@dataclass(frozen=True, slots=True, kw_only=True)
class Event(AggregateRoot):
    name: str
    description: Optional[str] = None
    date: str
    is_published: Optional[bool] = False
    total_spot: int
    total_spot_reserved: Optional[int] = 0
    partner_id: str
    sections: Optional[List[EventSection]] = field(default_factory=list)

    @staticmethod
    def create(command: EventCommand) -> 'Event':
        return Event(
            name=command.name,
            description=command.description,
            date=command.date,
            total_spot=command.total_spot,
            partner_id=command.partner_id,
            sections=command.sections
        )
