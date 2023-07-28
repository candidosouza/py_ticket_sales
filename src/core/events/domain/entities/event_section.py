from dataclasses import dataclass
from typing import Optional, TypedDict

from src.core.common.domain.entities import Entity


@dataclass
class EventSectionCommand(TypedDict):
    name: str
    description: str
    total_spot: int
    price: float


@dataclass
class EventSection(Entity):
    name: str
    description: Optional[str] = None
    is_published: bool
    total_spot: int
    total_spot_reserved: int
    price: float

    def create(self, command: EventSectionCommand) -> 'EventSection':
        return EventSection(
            name=command['name'],
            description=command['description'],
            total_spot=command['total_spot'],
            price=command['price'],
            is_published=False,
            total_spot_reserved=0
        )


