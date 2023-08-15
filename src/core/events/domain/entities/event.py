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
    
    def add_section(self, section: EventSection) -> None:
        self.sections.append(section)
