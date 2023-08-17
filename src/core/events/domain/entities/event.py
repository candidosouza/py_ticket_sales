from dataclasses import dataclass, field
from typing import List, Optional

from src.core.common.domain.aggregate_root import AggregateRoot
from src.core.events.domain.entities.event_section import EventSection


@dataclass(frozen=True, slots=True, kw_only=True)
class Event(AggregateRoot):
    name: str
    description: Optional[str] = None
    date: str
    is_published: Optional[bool] = False
    total_spot: Optional[int] = 0
    total_spot_reserved: Optional[int] = 0
    partner_id: str
    sections: Optional[List[EventSection]] = field(default_factory=list)

    def change_name(self, name: str) -> None:
        self._set('name', name)

    def change_description(self, description: str) -> None:
        self._set('description', description)

    def change_date(self, date: str) -> None:
        self._set('date', date)

    def publish_all(self) -> None:
        self.publish()
        for section in self.sections:
            section.publish_all()

    def un_publish_all(self) -> None:
        self.un_publish()
        for section in self.sections:
            section.un_publish_all()

    def publish(self) -> None:
        self._set('is_published', True)

    def un_publish(self) -> None:
        self._set('is_published', False)

    def add_section(self, section: EventSection) -> None:
        self.sections.append(section)
        total_spot = self.total_spot + section.total_spot
        self._set('total_spot', total_spot)
