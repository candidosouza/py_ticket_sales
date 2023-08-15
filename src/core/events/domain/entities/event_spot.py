from dataclasses import dataclass
from src.core.common.domain.entities import Entity


@dataclass(frozen=True, slots=True, kw_only=True)
class EventSpot(Entity):
    location: str
    is_reserved: bool
    is_published: bool
