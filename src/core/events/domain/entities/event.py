from dataclasses import dataclass, field
from typing import List, Optional, TypedDict

from src.core.common.domain.aggregate_root import AggregateRoot
from src.core.events.domain.entities.event_section import EventSection


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
    def create(event_input: 'EventInput') -> 'Event':
        return Event(
            name=event_input.name,
            description=event_input.description,
            date=event_input.date,
            total_spot=event_input.total_spot,
            partner_id=event_input.partner_id,
            sections=event_input.sections
        )
    
    def add_section(self, section: EventSection) -> None:
        self.sections.append(section)


@dataclass(frozen=True, slots=True, kw_only=True)
class EventInput:
    name: str
    description: Optional[str]
    date: str
    total_spot: int
    partner_id: str
    sections: Optional[List[EventSection]]
