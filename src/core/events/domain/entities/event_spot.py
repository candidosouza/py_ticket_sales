from dataclasses import dataclass
from typing import TypedDict

from src.core.common.domain.entities import Entity


@dataclass(frozen=True, slots=True, kw_only=True)
class EventSpotCommand:
    location: str
    is_reserved: bool
    is_published: bool


@dataclass(frozen=True, slots=True, kw_only=True)
class EventSpot(Entity):
    location: str
    is_reserved: bool
    is_published: bool

    @staticmethod
    def create(command: EventSpotCommand) -> 'EventSpot':
        return EventSpot(
            location=command.location,
            is_reserved=command.is_reserved,
            is_published=command.is_published
        )
