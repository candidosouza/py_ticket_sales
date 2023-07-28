from dataclasses import dataclass
from typing import TypedDict

from src.core.common.domain.entities import Entity


@dataclass
class EventSpotCommand(TypedDict):
    location: str
    is_reserved: bool
    is_published: bool


@dataclass
class EventSpot(Entity):
    location: str
    is_reserved: bool
    is_published: bool

    def create(self, command: EventSpotCommand) -> 'EventSpot':
        return EventSpot(
            location=command['location'],
            is_reserved=command['is_reserved'],
            is_published=command['is_published']
        )
