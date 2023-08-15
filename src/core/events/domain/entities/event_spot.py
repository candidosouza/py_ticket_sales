from dataclasses import dataclass
from typing import TypedDict

from src.core.common.domain.entities import Entity


@dataclass(frozen=True, slots=True, kw_only=True)
class EventSpotInput:
    location: str
    is_reserved: bool
    is_published: bool


@dataclass(frozen=True, slots=True, kw_only=True)
class EventSpot(Entity):
    location: str
    is_reserved: bool
    is_published: bool

    @staticmethod
    def create(input: EventSpotInput) -> 'EventSpot':
        return EventSpot(
            location=input.location,
            is_reserved=input.is_reserved,
            is_published=input.is_published
        )
