from dataclasses import dataclass
from typing import Optional, TypedDict

from src.core.common.domain.entities import Entity


@dataclass(frozen=True, slots=True, kw_only=True)
class EventSectionCommand:
    name: str
    description: str
    total_spot: int
    price: float


@dataclass(frozen=True, slots=True, kw_only=True)
class EventSection(Entity):
    name: str
    description: Optional[str] = None
    is_published: bool
    total_spot: int
    total_spot_reserved: int
    price: float

    @staticmethod
    def create(command: EventSectionCommand) -> 'EventSection':
        try:
            return EventSection(
                name=command.name,
                description=command.description,
                total_spot=command.total_spot,
                price=command.price,
                is_published=False,
                total_spot_reserved=0
            )
        except TypeError as e:
            raise TypeError(f'Error creating EventSection: {e}') from e


