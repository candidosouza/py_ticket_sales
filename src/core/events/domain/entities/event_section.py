from dataclasses import dataclass, field
from typing import Optional, List

from src.core.common.domain.entities import Entity
from src.core.events.domain.entities.event_spot import EventSpot


@dataclass(frozen=True, slots=True, kw_only=True)
class EventSectionInput:
    name: str
    description: str
    total_spot: int
    price: float
    spot: Optional[List[EventSpot]]


@dataclass(frozen=True, slots=True, kw_only=True)
class EventSection(Entity):
    name: str
    description: Optional[str] = None
    is_published: bool
    total_spot: int
    total_spot_reserved: int
    price: float
    spot: Optional[List[EventSpot]] = field(default_factory=list) 

    @staticmethod
    def create(input: EventSectionInput) -> 'EventSection':
        try:
            return EventSection(
                name=input.name,
                description=input.description,
                total_spot=input.total_spot,
                price=input.price,
                is_published=False,
                total_spot_reserved=0,
                spot=input.spot
            )
        except TypeError as e:
            raise TypeError(f'Error creating EventSection: {e}') from e


